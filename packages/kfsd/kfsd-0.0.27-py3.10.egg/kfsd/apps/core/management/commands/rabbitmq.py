from django.core.management.base import BaseCommand
from kfsd.apps.core.utils.dict import DictUtils
from kfsd.apps.core.middleware.config import KubefacetsConfigMiddleware
from kfsd.apps.core.msmq.rabbitmq.base import RabbitMQ


class Command(BaseCommand):
    help = "Listens to a RabbitMQ topic"

    def getConnectionArguments(self):
        connectionConfig = DictUtils.get_by_path(
            self.__config, "services.rabbitmq.connect"
        )
        authCredentials = connectionConfig.pop("credentials")
        connectionConfig["credentials"] = RabbitMQ.constructCredentials(
            DictUtils.get(authCredentials, "username"),
            DictUtils.get(authCredentials, "pwd"),
        )
        return connectionConfig

    def handle(self, *args, **options):
        configHandler = KubefacetsConfigMiddleware(None)
        self.__config = configHandler.getConfig().getFinalConfig()
        connectionConfig = self.getConnectionArguments()
        msmqHandler = RabbitMQ(connectionConfig)

        exchangeName = DictUtils.get_by_path(
            self.__config, "services.rabbitmq.consume.hello.exchange_name"
        )
        queueName = DictUtils.get_by_path(
            self.__config, "services.rabbitmq.consume.hello.queue_name"
        )
        routingKey = DictUtils.get_by_path(
            self.__config, "services.rabbitmq.consume.hello.routing_key"
        )

        msmqHandler.publish_msg(
            exchangeName, queueName, routingKey, "hi this is my first msg"
        )

        def callback(ch, method, properties, body):
            print("Msg Body: {}".format(body))

        msmqHandler.consume_msgs(callback, exchangeName, queueName, routingKey)
