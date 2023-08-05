import os
from typing import List, Optional
from urllib.parse import quote

from airflow.models import Variable
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.providers.telegram.operators.telegram import TelegramOperator
from airflow.utils.context import Context

_SLACK_NOTIFICATION = 'slack'

_SLACK_NOTIFICATION_TEMPLATE = """
    {message_title}
    *Owner*: {owner}
    *Dag*: {dag}
    *Task*: {task}
    *Environment*: {environment}
    *Execution Date*: {execution_date}
    *Log link*: <{log_link}|Ссылка>
"""

_TELEGRAM_NOTIFICATION_TEMPLATE = """
    {message_title}
    <b>Owner</b>: {owner}
    <b>Dag</b>: {dag}
    <b>Task</b>: {task}
    <b>Environment</b>: {environment}
    <b>Execution Date</b>: {execution_date}
    <b>Log link</b>: <a href="{log_link}">Ссылка</a>
"""


def send_alert_to_slack(context: Context, slack_webhook_connections: Optional[List[str]] = None) -> None:
    # Always send alerts to this conn id
    alert_sender = Alert(
        context=context,
        receiver_type='slack',
        conn_id='slack_default_webhook',
    )
    alert_sender.send()
    # Also send alerts to another conn ids
    if slack_webhook_connections:
        for conn_id in slack_webhook_connections:
            Alert(context=context, receiver_type='slack', conn_id=conn_id).send()


class Alert:
    """Class for alerting in airflow."""

    def __init__(
        self,
        context: Context,
        receiver_type: str,
        conn_id: str,
        message: str = None,
        channel: str = None,
    ) -> None:
        """
        Base constructor to create instance of alerts system.

        Args:
            context: Dag context for getting templated variables
            receiver_type: can be slack or telegram
            conn_id: connection id in airflow for sending alert
            message: custom message if user want to add to basic text
            channel: customize channel where to send. bot should be added to channel
        """
        self.conn_id = conn_id
        self.channel = channel
        self.receiver_type = receiver_type
        self.context = context

        self.dag_owner = context.get('dag').owner
        self.slack_owners = Variable.get('slack_owners', deserialize_json=True)
        self.task_instance = context.get('ti')
        self.dag_id = self.task_instance.dag_id
        self.task_id = self.task_instance.task_id
        self.execution_date = str(self.task_instance.execution_date).replace(' ', 'T')
        self.task_state = self.task_instance.state
        self.task_log_link = (
            '{airflow_webserver_base_url}/log?dag_id={dag_id}&task_id={task_id}&execution_date={execution_date}'.format(
                airflow_webserver_base_url=os.environ.get('AIRFLOW__WEBSERVER__BASE_URL'),
                dag_id=self.dag_id,
                task_id=self.task_id,
                execution_date=quote(self.execution_date),
            )
        )

        if self.task_state == 'failed':
            self.message_title = (
                ':collision: Task Failed'
                if self.receiver_type == _SLACK_NOTIFICATION
                else '\U0001F4A5: Task Failed'
            )
        elif self.task_state == 'success':
            self.message_title = (
                ':done: Task Successful'
                if self.receiver_type == _SLACK_NOTIFICATION
                else '\u2705: Task Successful'
            )
        self.environment = Variable.get('env', default_var='env is not defined')
        self.message = self.generate_message(message)

    # TODO: Why is it public? Is it used somewhere except __init__?
    def generate_message(self, message: str) -> str:
        """
        Return generated message with added custom message.

        Args:
            message: text of message in alert

        Returns:
            templated html or tg content
        """
        if self.receiver_type == _SLACK_NOTIFICATION:
            basic_content = _SLACK_NOTIFICATION_TEMPLATE.format(
                message_title=self.message_title,
                owner=self.slack_owners.get(self.dag_owner, self.dag_owner),
                dag=self.dag_id,
                task=self.task_id,
                environment=self.environment,
                execution_date=self.execution_date,
                log_link=self.task_log_link,
            )
        else:
            basic_content = _TELEGRAM_NOTIFICATION_TEMPLATE.format(
                message_title=self.message_title,
                owner=self.dag_owner,
                dag=self.dag_id,
                task=self.task_id,
                environment=self.environment,
                execution_date=self.execution_date,
                log_link=self.task_log_link,
            )

        if message:
            return basic_content + '{basic_content}\n   {message}'.format(
                basic_content=basic_content,
                message=message,
            )
        return basic_content

    # TODO: Why is it public? Is it used somewhere except send?
    def slack_alert(self, context: Context) -> None:
        """
        Return executing slack alert.

        Args:
            context: Airflow context
        """
        alert = SlackWebhookOperator(
            task_id='slack_notify',
            http_conn_id=self.conn_id,
            message=self.message,
            channel=self.channel,
        )

        alert.execute(context)

    # TODO: Why is it public? Is it used somewhere except send?
    def telegram_alert(self, context: Context) -> None:
        """
        Return executing telegram alert.

        Args:
            context: Airflow context
        """
        alert = TelegramOperator(
            task_id='telegram_notify',
            telegram_conn_id=self.conn_id,
            chat_id=self.channel,
            text=self.message,
        )
        alert.execute(context)

    def send(self) -> None:
        if self.receiver_type == _SLACK_NOTIFICATION:
            self.slack_alert(self.context)
        self.telegram_alert(self.context)
