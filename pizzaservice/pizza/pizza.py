import json
import uuid
import random


class Pizza:
    '''
    A class to represent a pizza, with various customizable attributes.

    Attributes
    ----------
    order_id : str
        The unique identifier for the order associated with the pizza.
    sauce : str
        The type of sauce on the pizza.
    cheese : str
        The type of cheese on the pizza.
    meats : str
        The type of meat toppings on the pizza.
    veggies : str
        The type of vegetable toppings on the pizza.

    Methods
    -------
    toJSON() -> str:
        Returns a formatted JSON string representation of the Pizza object.
    __str__() -> str:
        Returns a JSON string representation of the Pizza object.
    '''
    def __init__(self):
        self.order_id = ''
        self.sauce = ''
        self.cheese = ''
        self.meats = ''
        self.veggies = ''

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)

    def __str__(self):
        return json.dumps(self.__dict__)


class PizzaOrder:
    '''
    A class to represent a pizza order, which can contain multiple pizzas.

    Attributes
    ----------
    id : str
        A unique identifier for the order, generated using UUID.
    count : int
        The number of pizzas in the order.
    pizzas : list
        A list to store the pizzas included in the order.

    Methods
    -------
    add_pizza(pizza):
        Adds a pizza to the order.
    get_pizzas() -> list:
        Returns the list of pizzas in the order.
    __str__() -> str:
        Returns a JSON string representation of the PizzaOrder object.
    toJSON() -> str:
        Returns a formatted JSON string representation of the
        PizzaOrder object.
    '''
    def __init__(self, count):
        self.id = str(uuid.uuid4().int)
        self.count = count
        self.pizzas = []

    def add_pizza(self, pizza) -> None:
        '''
        Adds a pizza to the order.

        Parameters
        ----------
        pizza : object
            An object representing a pizza to be added to the order.
        '''
        self.pizzas.append(pizza)

    def get_pizzas(self) -> list:
        '''
        Adds a pizza to the order.

        Returns
        -------
        list
            A list of pizzas that have been added to the order.
        '''
        return self.pizzas

    def __str__(self) -> str:
        '''
        Returns a JSON string representation of the PizzaOrder object.

        Returns
        -------
        str
            A JSON string that represents the PizzaOrder object.
        '''
        return json.dumps(self.__dict__)

    def toJSON(self) -> str:
        '''
        Returns a formatted JSON string representation of the
        PizzaOrder object.

        Returns
        -------
        str
            A formatted JSON string that represents the PizzaOrder object.
        '''
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


class Topping:
    '''
    A class to represent a pizza topping and handle the logic for
    adding it to a pizza.

    Attributes
    ----------
    order_id : int
        The unique identifier for the order.
    pizza : dict
        A dictionary representing the pizza, where keys are topping types
        and values are specific toppings.
    topping : str
        The type of topping to be added (e.g., 'sauce', 'cheese', 'meats',
        'veggies').

    Methods
    -------
    add_topping():
        Adds the selected topping to the pizza.
    select_topping() -> str:
        Randomly selects a topping from a predefined list based on the
        topping type.
    '''
    def __init__(self, order_id: int, pizza: dict, topping: str):
        self.order_id = order_id
        self.pizza = pizza
        self.topping = topping

    def add_topping(self) -> None:
        '''
        Add topping to the pizza and write the event message to the topic.
        '''
        self.pizza[self.topping] = self.select_topping()

        return self.pizza

    def select_topping(self) -> str:
        '''
        Randomly selects a topping from a list.

        Return:
        -------
        str
        '''
        i = random.randint(0, 6)

        sauces = [
            'regular', 'light', 'extra', 'none', 'alfredo', 'regular',
            'light', 'extra', 'alfredo'
            ]
        cheeses = [
            'extra', 'none', 'three cheese', 'goat cheese', 'extra',
            'three cheese', 'goat cheese'
            ]
        meats = [
            'pepperoni', 'sausage', 'ham', 'anchovies', 'salami',
            'bacon', 'pepperoni', 'sausage', 'ham', 'anchovies',
            'salami', 'bacon'
            ]
        veggies = [
            'tomato', 'olives', 'onions', 'peppers', 'pineapple',
            'mushrooms', 'tomato', 'olives', 'onions', 'peppers',
            'pineapple', 'mushrooms'
            ]

        if self.topping == 'sauce':
            return sauces[i]
        if self.topping == 'cheese':
            return cheeses[i]
        if self.topping == 'meats':
            return meats[i]
        if self.topping == 'veggies':
            return veggies[i]
