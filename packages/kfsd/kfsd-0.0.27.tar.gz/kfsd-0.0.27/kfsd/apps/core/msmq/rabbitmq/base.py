import pika
from kfsd.apps.core.common.logger import Logger, LogLevel

logger = Logger.getSingleton(__name__, LogLevel.DEBUG)


class RabbitMQ:
    def __init__(self, connectionParams):
        connection_params = pika.ConnectionParameters(**connectionParams)
        self.__connection = pika.BlockingConnection(connection_params)
        self.__channel = self.__connection.channel()
        self.__queueName = ""
        self.__exchangeName = ""
        self.__routingKey = ""
        self.__exchangeType = "topic"
        self.__isQueueExclusive = True
        self.__queue = None
        self.__exchange = None
        self.__autoAck = True
        self.__queueDurable = True
        self.__exchangeDurable = True

    @staticmethod
    def constructCredentials(username, pwd):
        return pika.PlainCredentials(username, pwd)

    def setQueueName(self, queueName):
        self.__queueName = queueName

    def setAutoAck(self, ack):
        self.__autoAck = ack

    def setQueueExclusive(self, exclusiveVal):
        self.__isQueueExclusive = exclusiveVal

    def setExchangeType(self, exchangeType):
        self.__exchangeType = exchangeType

    def setExchangeName(self, exchangeName):
        self.__exchangeName = exchangeName

    def setRoutingKey(self, routingKey):
        self.__routingKey = routingKey

    def declareQueue(self):
        self.__queue = self.__channel.queue_declare(
            queue=self.__queueName, exclusive=self.__isQueueExclusive, durable=self.__queueDurable
        )

    def declareExchange(self):
        self.__exchange = self.__channel.exchange_declare(
            exchange=self.__exchangeName, exchange_type=self.__exchangeType, durable=self.__exchangeDurable
        )

    def queueBind(self):
        self.__channel.queue_bind(
            exchange=self.__exchangeName,
            queue=self.__queueName,
            routing_key=self.__routingKey,
        )

    def publish(self, msg):
        self.__channel.basic_publish(
            exchange=self.__exchangeName, routing_key=self.__routingKey, body=msg
        )

    def publish_msg(self, exchangeName, queueName, routingKey, msg):
        self.setExchangeName(exchangeName)
        self.setQueueName(queueName)
        self.setRoutingKey(routingKey)
        self.declareExchange()
        self.declareQueue()
        self.publish(msg)

    def consume_msgs(self, callback, exchangeName, queueName, routingKey):
        self.setExchangeName(exchangeName)
        self.setQueueName(queueName)
        self.setRoutingKey(routingKey)
        self.declareExchange()
        self.declareQueue()
        self.queueBind()
        self.consume(callback)
        self.startConsuming()

    def consume(self, callback):
        self.__channel.basic_consume(
            queue=self.__queueName,
            on_message_callback=callback,
            auto_ack=self.__autoAck,
        )

    def closeConnection(self):
        self.__connection.close()

    def startConsuming(self):
        self.__channel.start_consuming()
