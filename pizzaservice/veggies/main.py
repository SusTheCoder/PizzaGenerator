import json

from pizzaservice.config.main import KafkaConfig
from pizzaservice.pizza.pizza import Topping


# Configuration of the Kafka client
kafka = KafkaConfig(service="veggies")
producer_config = kafka.config()[0]
consumer_config = kafka.config()[0]

# Create a Kafka producer
veggies_producer = kafka.producer(producer_config)
# Create a Kafka consumer
pizza_consumer = kafka.consumer(consumer_config)
# Subscribe to the Kafka topic.
pizza_consumer.subscribe(["pizza-with-meats"])


def start_service():
    while True:
        msg = pizza_consumer.poll(0.1)
        if msg is None:
            pass
        elif msg.error():
            pass
        else:
            # Get pizza from the topic
            pizza = json.loads(msg.value())
            # Create topping and add to the pizza
            topping = Topping(order_id=msg.key(),
                              pizza=pizza,
                              topping="veggies")
            pizza_with_topping = topping.add_topping()
            # Add pizza with topping to the new topic
            veggies_producer.produce(topic="pizza-with-veggies",
                                     key=msg.key(),
                                     value=json.dumps(pizza_with_topping))
            veggies_producer.flush()


if __name__ == '__main__':
    start_service()
