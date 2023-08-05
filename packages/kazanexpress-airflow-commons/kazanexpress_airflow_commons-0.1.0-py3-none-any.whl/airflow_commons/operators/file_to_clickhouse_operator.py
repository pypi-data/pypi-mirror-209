import os
import pathlib
from collections import namedtuple
from typing import Any, Callable, Dict, Iterable, List, Optional

import pandas as pd
from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.utils.context import Context

from airflow_commons.hooks.clickhouse_hook import ClickHouseHook

TablePartition = namedtuple('TablePartition', 'table partition')

_OPTIMIZE_QUERY = """OPTIMIZE TABLE {table} ON CLUSTER '{{cluster}}' PARTITION {partition} FINAL
                                  SETTINGS distributed_ddl_task_timeout = 1500;"""


class FileToClickhouseOperator(BaseOperator):
    """
    Operator to insert data from s3 to clickhouse in csv format.

    It will read file from s3 bucket with specified key as csv and insert it into Clickhouse table.
    It uses s3fs besides S3Hook.
    """

    template_ext = ('.sql',)

    template_fields = (
        'target_table',
        'filename',
        'filepath',
        'partitions_to_optimize',
        'transform_df',
    )

    def __init__(
        self,
        ch_hook: ClickHouseHook,
        target_table: str,
        filename: str,
        filepath: str = '/opt/airflow/s3fs/{{ dag.dag_id }}/{{ run_id }}',
        column_list: Optional[Iterable[str]] = None,
        truncate: bool = False,
        transform_df: Callable[[pd.DataFrame, Context], pd.DataFrame] = None,
        query_id: Optional[str] = None,
        external_tables: Optional[List[Dict]] = None,
        partitions_to_optimize: Optional[List[TablePartition]] = None,
        pd_read_csv_kwargs: Optional[Dict[str, str]] = None,
        pd_read_parquet_kwargs: Optional[Dict[str, str]] = None,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ):
        """
        Base constructor to create operator.

        Args:
            ch_hook: connection id in airflow to clickhouse db
            target_table: table in clickhouse to fill data
            filename: name of file in filesystem
            filepath: path to download file from s3
            column_list: list of column_names to use in insert query to clickhouse. default all columns
            truncate: if specified then target table will be truncated
            transform_df: python function to do transformation with dataframe
            query_id: the query identifier. It will be generated in case of absence. String but real type is uuid
            external_tables: external tables that can be used in query
            partitions_to_optimize: partitions that will execute optimize in clickhouse
            pd_read_csv_kwargs: dict of pandas pd.read_csv() method arguments
            pd_read_parquet_kwargs: dict of pandas pd.read_parquet() method arguments
            *args: additional arguments for parent constructor of BaseOperator
            **kwargs: additional keyword arguments for parent constructor of BaseOperator
        """
        super().__init__(*args, **kwargs)

        self.hook = ch_hook
        self.target_table = target_table
        self.filename = filename
        self.filepath = filepath
        self.column_list = column_list or ('*',)
        self.truncate = truncate
        self.transform_df = transform_df
        self.query_id = query_id
        self.external_tables = external_tables
        self.pd_read_csv_kwargs = pd_read_csv_kwargs or {'encoding": "UTF-8'}
        self.pd_read_parquet_kwargs = pd_read_parquet_kwargs or {}
        self.partitions_to_optimize = partitions_to_optimize or []

    def execute(self, context: Context) -> None:
        full_path = os.path.join(self.filepath, self.filename)
        if os.path.isfile(full_path):
            self.log.info(
                'Start read csv from s3 with path {filepath}'.format(
                    filepath=self.filepath,
                ),
            )
            if pathlib.Path(self.filename).suffix == '.csv':
                df = pd.read_csv(full_path, **self.pd_read_csv_kwargs)
            else:
                df = pd.read_parquet(full_path, **self.pd_read_parquet_kwargs)
        else:
            raise AirflowException(
                'File does not exist in path {full_path}'.format(
                    full_path=full_path,
                ),
            )

        if df.empty:
            self.log.info(
                'Dataframe from {filepath} is empty. Nothing to do.'.format(
                    filepath=self.filepath,
                ),
            )
        else:
            self.log.info(
                'Dataframe from {filepath} has {rows_amount} rows'.format(
                    filepath=self.filepath,
                    rows_amount=df.shape[0],
                ),
            )
            self.log.info(
                'First 5 rows of dataframe\n: {first_five_rows}'.format(
                    first_five_rows=df.head(),
                ),
            )

            if self.transform_df:
                old_shape = df.shape
                self.log.info(
                    'Shape before transforming - {old_shape}'.format(
                        old_shape=old_shape,
                    ),
                )
                df = self.transform_df(df, context)
                self.log.info(
                    'Dataframe was transformed from {old_shape} to {new_shape}'.format(
                        old_shape=old_shape,
                        new_shape=df.shape,
                    ),
                )

            if self.truncate:
                self.log.info('Start to truncate target table in Clickhouse')
                self.hook.run(
                    "TRUNCATE TABLE {target_table} ON CLUSTER '{{cluster}}'".format(
                        target_table=self.target_table,
                    ),
                )
                self.log.info('Table successfully truncated')

            self.log.info('Start loading dataframe into Clickhouse')

            rows_inserted = self.hook.insert_dataframe(
                query='INSERT INTO {target_table} ({inserted_values}) VALUES'.format(
                    target_table=self.target_table,
                    inserted_values=','.join(map(str, self.column_list)),
                ),
                dataframe=df,
                external_tables=self.external_tables,
                query_id=self.query_id,
            )
            self.log.info(
                '{rows_inserted} rows inserted into table {target_table}'.format(
                    rows_inserted=rows_inserted,
                    target_table=self.target_table,
                ),
            )

            # Call OPTIMIZE. Useful in case of ReplacingMergeTree Engine
            # when we need to ensure that no duplicates are to remain after ETL
            for table, partition in self.partitions_to_optimize:
                self.log.info(
                    'Executing optimize on table {table} and partition {partition}'.format(
                        table=table,
                        partition=partition,
                    ),
                )
                self.hook.run(_OPTIMIZE_QUERY.format(table=table, partition=partition))
