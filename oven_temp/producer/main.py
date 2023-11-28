from confluent_kafka import Producer
import requests
import time

producer = Producer({'bootstrap.servers': 'broker:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

while True:
    oven_reading = requests.get("http://127.0.0.1:8000/oven").json()
    producer.produce('oven', value=str(oven_reading["temperature"]), callback=delivery_report)
    producer.poll(0)
    time.sleep(1)
