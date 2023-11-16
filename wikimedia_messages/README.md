# Wikimedia Kafka Producer and Consumer

This Python project consists of a Kafka producer and a Kafka consumer that work together to fetch real-time events from the Wikimedia recent changes stream and process them through a Kafka topic.

## Prerequisites

Before running the program, ensure you have the following installed:

- [Python](https://www.python.org/) (version 3.x recommended)
- [pip](https://pip.pypa.io/) (Python package installer)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Bonks03/GrandCircusLabs/tree/main/wikimedia_messages
    cd wikimedia_messages
    ```

2. Create and activate a virtual environment in kafka_consumer:

    ```bash
    cd kafka_consumer
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Create and activate a virtual environment in kafka_producer:

    ```bash
    cd kafka_producer
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4. Build all images (this will automatically install required libraries):

    ```bash
    cd kafka_broker
    docker build -t broker:latest .
    cd ../kafka_zookeeper
    docker build -t zookeeper:latest .
    cd ../kafka_producer
    docker build -t producer:latest .
    cd ../kafka_consumer
    docker build -t consumer:latest .
    ```

## Docker Compose Setup

The project includes Docker Compose configurations to run Zookeeper, Kafka broker, Kafka producer, and Kafka consumer. Before running, ensure your Docker daemon is up and running.

```bash
docker-compose up
```

This command will start Zookeeper, Kafka broker, Kafka producer, Kafka consumer services, and create a topic named `latest_events`.

## Usage

### Kafka Producer

The consumer is included in the Docker Compose setup. It will start fetching events from the Wikimedia recent changes stream and publish them to the `latest_events` topic.

### Kafka Consumer

The consumer is included in the Docker Compose setup. It will automatically consume messages from the `latest_events` topic.

## Configuration

Ensure that your Kafka broker and topic are correctly configured in `producer.py` and `consumer.py`. Update the Kafka broker address and topic name as needed.

```python
# producer.py
p = Producer({'bootstrap.servers': 'your-kafka-broker:9092'})
p.produce('your-kafka-topic', message.encode('utf-8'), callback=delivery_report)
```

```python
# consumer.py
consumer_conf = {
    'bootstrap.servers': 'your-kafka-broker:9092',
    'group.id': 'consumer_group',
    'auto.offset.reset': 'earliest'
}
```