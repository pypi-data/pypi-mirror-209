from collections import namedtuple
from typing import Any, Dict, Iterable, List, Optional

import pandas as pd
from airflow.models import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.context import Context

from airflow_commons.hooks.clickhouse_hook import ClickHouseHook

TablePartition = namedtuple('TablePartition', 'table partition')

_OPTIMIZE_QUERY = """OPTIMIZE TABLE {table} ON CLUSTER '{{cluster}}' PARTITION {partition} FINAL
                                  SETTINGS distributed_ddl_task_timeout = 1500;"""


class PostgresToClickhouseOperator(BaseOperator):
    """Operator to transfer data from Postgres using sql query to Clickhouse table."""

    template_fields = ('sql', 'partitions_to_optimize')
    template_fields_renderers = {'sql': 'sql'}
    template_ext = ('.sql',)

    def __init__(
        self,
        *,
        sql: str,
        postgresql_hook: PostgresHook,
        clickhouse_hook: ClickHouseHook,
        clickhouse_table: str,
        column_list: Optional[Iterable[str]] = None,
        truncate: Optional[bool] = False,
        query_id: Optional[str] = None,
        external_tables: Optional[List[Dict]] = None,
        partitions_to_optimize: Optional[List[TablePartition]] = None,
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Base constructor to create operator.

        Args:
            sql: the sql statement to be executed (str) or path to sql file
            postgresql_hook: Postgresql hook from connection
            clickhouse_hook: clickhouse hook from connection
            clickhouse_table: table in clickhouse to fill data
            column_list: list of column_names to use in insert query to clickhouse. default all columns
            truncate: if specified then target table will be truncated
            query_id: the query identifier. It will be generated in case of absence. String but real type is uuid
            external_tables: external tables6 that can be used in query
            partitions_to_optimize: partitions that will execute optimize in clickhouse
            **kwargs: additional keyword arguments for parent constructor of BaseOperator
        """
        super().__init__(**kwargs)
        self.sql = sql
        self.clickhouse_table = clickhouse_table
        self.column_list = column_list or ('*',)
        self.truncate = truncate
        self.query_id = query_id
        self.external_tables = external_tables
        self.clickhouse_hook = clickhouse_hook
        self.postgres_hook = postgresql_hook
        self.partitions_to_optimize: List[TablePartition] = partitions_to_optimize or []

    def execute(self, context: Context) -> None:
        if self.truncate:
            self.clickhouse_hook.run(
                'TRUNCATE TABLE {clickhouse_table}'.format(
                    clickhouse_table=self.clickhouse_table,
                ),
            )

        self.log.info('Start selecting data from Postgres')
        if self.sql.endswith('.sql'):
            try:
                df = self._try_to_open_and_execute()
            except FileNotFoundError as error:
                self.log.error(
                    'Error {error}: path to sql file not found'.format(
                        error=self.sql,
                    ),
                )
                raise error
        else:
            self.log.info(
                'Start executing PostgreSQL query:\n{sql}'.format(
                    sql=self.sql,
                ),
            )
            df: pd.DataFrame = self.postgres_hook.get_pandas_df(sql=self.sql)

        if df.shape[0] == 0:
            self.log.info('Dataframe is empty. Nothing to insert.')
        else:
            self.log.info(
                'DataFrame from query has {rows_amount} rows'.format(
                    rows_amount=df.shape[0],
                ),
            )

            self.log.info('Start loading dataframe into Clickhouse')

            rows_inserted = self.clickhouse_hook.insert_dataframe(
                query='INSERT INTO {target_table} ({inserted_values}) VALUES'.format(
                    target_table=self.clickhouse_table,
                    inserted_values=','.join(map(str, self.column_list)),
                ),
                dataframe=df,
                external_tables=self.external_tables,
                query_id=self.query_id,
            )
            self.log.info(
                '{rows_inserted} rows inserted into table {clickhouse_table}'.format(
                    rows_inserted=rows_inserted,
                    clickhouse_table=self.clickhouse_table,
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
                self.clickhouse_hook.run(_OPTIMIZE_QUERY.format(table=table, partition=partition))

    def _try_to_open_and_execute(self) -> pd.DataFrame:
        with open(self.sql, 'r') as query:
            self.log.info(
                'Start executing PostgreSQL query from file_path: {query_path}'.format(
                    query_path=self.sql,
                ),
            )
            return self.postgres_hook.get_pandas_df(sql=query.read())
