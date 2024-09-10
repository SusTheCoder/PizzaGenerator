from configparser import ConfigParser
from confluent_kafka import Producer, Consumer


class KafkaConfig:
    '''
    Class to configure and instantiate the Kafka producer and consumers.

    Attribute:
    ----------
    service (str):
        The specific service of the pizza (e.g. pizza-with-sauce, etc.)

    Method:
    -------
    config():
        Confgure the Kafka client based on the config.properties file.
    producer():
        Create a Kafka producer.
    consumer():
        Create a Kafka consumer.
    subscribe():
        Subscribe to a Kafka topic.
    '''
    def __init__(self, service: str):
        self.service = service

    def config(self):
        # Configuration of the Kafka client
        config_parser = ConfigParser(interpolation=None)
        config_file = open(
            f'pizzaservice/{self.service}/config.properties', 'r')
        config_parser.read_file(config_file)
        client_config = dict(config_parser['kafka_client'])

        return client_config, config_parser

    def producer(self, config) -> Producer:
        'Create a Kafka producer.'

        return Producer(config)

    def consumer(self, config) -> Consumer:
        'Create a Kafka consumer.'

        return Consumer(config)
