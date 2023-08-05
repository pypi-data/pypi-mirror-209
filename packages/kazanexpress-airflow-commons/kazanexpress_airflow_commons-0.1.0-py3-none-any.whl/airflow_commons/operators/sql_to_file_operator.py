import os
import pathlib
from typing import Any, Dict, Iterable, Optional, Union

import pandas as pd
from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.context import Context

from airflow_commons.hooks.clickhouse_hook import ClickHouseHook


class SQLToFileOperator(BaseOperator):
    """Operator to execute query either in PostgreSQL or CLickhouse and load it into s3fs."""

    template_ext = ('.sql',)

    template_fields = ('sql', 'filename', 'filepath')

    def __init__(
        self,
        sql: str,
        filename: str,
        db_hook: Union[PostgresHook, ClickHouseHook],
        filepath: Optional[str] = None,
        pd_to_csv_kwargs: Optional[Dict[str, str]] = None,
        pd_to_parquet_kwargs: Optional[Dict[str, str]] = None,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Base constructor to create operator.

        Args:
            sql: the sql statement to be executed (str) or path to sql file
            filename: name of file
            db_hook: database hook for execute sql query
            filepath: path to file in s3 if specified and default path if not
            pd_to_csv_kwargs: dict of pandas pd.read_csv() method arguments
            pd_to_parquet_kwargs: dict of pandas pd.read_parquet() method arguments
            *args: additional arguments for parent constructor of BaseOperator
            **kwargs: additional keyword arguments for parent constructor of BaseOperator
        """
        super().__init__(*args, **kwargs)
        self.sql = sql
        self.filepath = filepath or '/opt/airflow/s3fs/{{ dag.dag_id }}/{{ run_id }}'
        self.db_hook = db_hook
        self.filename = filename
        self.pd_to_csv_kwargs = pd_to_csv_kwargs or {}
        self.pd_to_parquet_kwargs = pd_to_parquet_kwargs or {}

    def execute(self, context: Context) -> None:
        if isinstance(self.db_hook, (ClickHouseHook, PostgresHook)):
            raise AirflowException('DB Hook should be Postgres or Clickhouse')

        if self.sql.endswith('.sql'):
            try:
                df = self._try_to_open_and_execute()
            except FileNotFoundError as error:
                self.log.error('Error {error}: path to sql file not found'.format(error=error))
                raise error
        else:
            self.log.info('Start executing query:\n{query} in Postgres'.format(query=self.sql))
            df = self.db_hook.get_pandas_df(self.sql)

        self.log.info('DataFrame from query has {rows_amount} rows'.format(rows_amount=df.shape[0]))
        self.log.info('First 5 rows of dataframe\n: {first_five_rows}'.format(first_five_rows=df.head()))

        full_path = os.path.join(self.filepath, self.filename)
        if not os.path.isdir(self.filepath):
            os.makedirs(self.filepath)

        if os.path.isfile(full_path):
            self.log.info('Start to delete object in s3 with path - {full_path}'.format(full_path=full_path))
            os.remove(full_path)
            self.log.info('Object {full_path} successfully deleted'.format(full_path=full_path))

        self.log.info('Start to load new object')
        if pathlib.Path(self.filename).suffix == '.csv':
            df.to_csv(full_path, **self.pd_to_csv_kwargs)
        else:
            df.to_parquet(full_path, **self.pd_to_parquet_kwargs)
        self.log.info(
            'File {full_path} successfully loaded to s3'.format(
                full_path=full_path,
            ),
        )

    def _try_to_open_and_execute(self) -> pd.DataFrame:
        with open(self.sql, 'r') as query:
            self.log.info(
                'Start executing query from file_path: {query_path}'.format(
                    query_path=self.sql,
                ),
            )
            return self.db_hook.get_pandas_df(query.read())
