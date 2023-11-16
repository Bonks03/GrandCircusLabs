# Wikimedia Kafka Producer and Consumer

This Python project consists of a Kafka producer and a Kafka consumer that work together to fetch real-time events from the Wikimedia recent changes stream and process them through a Kafka topic.

## Prerequisites

Before running the program, ensure you have the following installed:

- [Python](https://www.python.org/) (version 3.x recommended)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone <repository-url>
    cd wikimedia-kafka
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Docker Compose Setup

The project includes Docker Compose configurations to run Zookeeper, Kafka broker, Kafka producer, and Kafka consumer. Before running, ensure your Docker daemon is up and running.

```bash
docker-compose up
```

This command will start Zookeeper, Kafka broker, Kafka producer, and Kafka consumer services.

## Usage

### Kafka Producer

Run the Kafka producer separately:

```bash
python producer.py
```

The producer will start fetching events from the Wikimedia recent changes stream and publish them to the Kafka topic.

### Kafka Consumer

The consumer is included in the Docker Compose setup. It will automatically consume messages from the Kafka topic.

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
    'group.id': 'your-consumer-group',
    'auto.offset.reset': 'earliest'
}
```

## Contributing

If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

---

Replace `<repository-url>` with the actual URL of your Git repository. Customize sections based on the specific features and requirements of your Kafka producer and consumer. This README provides users and contributors with information on how to set up and use the entire project with Docker Compose.