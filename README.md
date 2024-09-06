# 🍕 Random Pizza Generator
An event-driven microservices demo with Python and Kafka.

## Description

This demo consists of the following projects:

  - *pizza-service* a Flask app with Kafka support.
  - *sauce-service* a basic Python app with Kafka.
  - *cheese-service* a basic Python app with Kafka.
  - *meat-service* a basic Python app with Kafka.
  - *veggie-service* a basic Python app with Kafka.
  - *front-end* a basic front-end interface with Flask (TODO).

## Pre-requisites
Ensure that you have Kafka installed on your local computer and that you have started the Kafka zookeeper and brokers. The configuration of the Kafka systems is up to your preference.

This demo will be run on local Kafka broker clusters.

## Running the demo

- Before running this demo, you will need to update the `config.properties` file in each project. Replace the fields marked with `< >` using values from your local Kafka cluster.
- Also, you will need to create 5 topics in Confluent Cloud. They can each have 1 partion (or more if you so desire): `pizza`, `pizza-with-sauce`, `pizza-with-cheese`, `pizza-with-meat`, and `pizza-with-veggies`. 

Once all five services are up and running, you can issue the following `curl` command to send an order for 3 random pizzas.
`curl -X POST http://localhost:5000/order/5`  

This will trigger a series of events which will result in a completed pizza order with the five pizzas, and it will return a UUID of that pizza order.

To see your pizzas run the following `curl` command using the UUID returned from the first call.

curl http://localhost:5000/order/{{pizza-order-UUID}}

## Install Dependencies
To install the required dependencies for this project, run `pip install -r requirements.txt`.