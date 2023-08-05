from collections import namedtuple
from typing import Any, Dict, List, Optional

from airflow.models import BaseOperator
from airflow.utils.context import Context

from airflow_commons.hooks.clickhouse_hook import ClickHouseHook

TablePartition = namedtuple('TablePartition', 'table partition')

_OPTIMIZE_QUERY = """OPTIMIZE TABLE {table} ON CLUSTER '{{cluster}}' PARTITION {partition} FINAL
                                  SETTINGS distributed_ddl_task_timeout = 1500;"""


class ClickhouseExecuteOperator(BaseOperator):
    """Operator for executing sql in Clickhouse Database."""

    template_fields = ('sql', 'partitions_to_optimize')
    template_ext = ('.sql',)
    ui_color = '#fc0'

    def __init__(
        self,
        *,
        sql: str,
        ch_hook: ClickHouseHook,
        query_id: Optional[str] = None,
        partitions_to_optimize: Optional[List[TablePartition]] = None,
        external_tables: Optional[List[Dict]] = None,
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Base constructor to create operator.

        Args:
            sql: SQL query to execute. Only one query
            ch_hook: instance of ClickHouseHook
            query_id: the query identifier. It will be generated in case of absence. String but real type is uuid
            partitions_to_optimize: partitions that will execute optimize in clickhouse
            external_tables: external tables6 that can be used in query. Sets to query
            **kwargs: additional keyword arguments for parent constructor of BaseOperator
        """
        super().__init__(**kwargs)
        self.hook = ch_hook
        self.sql = sql
        self.query_id = query_id
        self.external_tables = external_tables
        self.partitions_to_optimize: List[TablePartition] = partitions_to_optimize or []

    def execute(self, context: Context) -> None:
        if self.sql.endswith('.sql'):
            try:
                self._try_to_open_and_execute()
            except FileNotFoundError as error:
                self.log.error(
                    'Error {error}: path to sql file not found'.format(
                        error=error,
                    ),
                )
                raise error
        else:
            self.log.info(
                'Start executing query:\n{sql} in Clickhouse'.format(
                    sql=self.sql,
                ),
            )
            self.hook.run(
                self.sql,
                query_id=self.query_id,
                external_tables=self.external_tables,
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

    def _try_to_open_and_execute(self) -> None:
        with open(self.sql, 'r') as query:
            self.log.info(
                'Start executing query from file_path: {file_path}'.format(
                    file_path=self.sql,
                ),
            )
            self.hook.run(
                query.read(),
                query_id=self.query_id,
                external_tables=self.external_tables,
            )
