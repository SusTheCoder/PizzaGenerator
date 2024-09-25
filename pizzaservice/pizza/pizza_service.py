import json
from confluent_kafka import Consumer

from pizza import Pizza, PizzaOrder
from pizzaservice.config.main import KafkaConfig

# Configuration of the Kafka client
kafka = KafkaConfig(service="pizza")
producer_config = kafka.config()[0]
consumer_config = kafka.config()[0]
# Configure and update the Kafka consumer
consumer_config.update(kafka.config()[1]['consumer'])

pizza_producer = kafka.producer(producer_config)

pizza_warmer = {}


def order_pizzas(count: int) -> PizzaOrder:
    '''
    Get the pizza order and create a new event to the "pizza" topic.

    Parameters:
    -----------
    count : int
        The number of pizzas to order.

    Returns:
    --------
    PizzaOrder
    '''
    # Create a new order
    order = PizzaOrder(count)
    # Append the order to a dictionary
    pizza_warmer[order.id] = order
    for i in range(count):
        new_pizza = Pizza()
        new_pizza.order_id = order.id
        pizza_producer.produce('pizza', key=order.id, value=new_pizza.toJSON())
    pizza_producer.flush()
    return order.id


def get_order(order_id):
    order = pizza_warmer[order_id]
    if order is None:
        return "Order not found, perhaps it's not ready yet."
    else:
        return order.toJSON()


def load_orders():
    pizza_consumer = Consumer(consumer_config)
    pizza_consumer.subscribe(['pizza-with-veggies'])
    while True:
        event = pizza_consumer.poll(1.0)
        if event is None:
            pass
        elif event.error():
            print(f'Bummer - {event.error()}')
        else:
            pizza = json.loads(event.value())
            add_pizza(pizza['order_id'], pizza)


def add_pizza(order_id, pizza):
    if order_id in pizza_warmer.keys():
        order = pizza_warmer[order_id]
        order.add_pizza(pizza)
