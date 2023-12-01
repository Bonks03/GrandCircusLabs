import time
from confluent_kafka import Producer
import requests

def main(url):
    p = Producer({'bootstrap.servers': 'broker:9092'})

    def delivery_report(err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.text
        except requests.exceptions.RequestException as e:
            print(f'Error making request: {e}')
            data = None

        if data:
            p.poll(0)
            p.produce('temperature', data.encode('utf-8'), callback=delivery_report)

        time.sleep(1)

    p.flush()

if __name__ == '__main__':
    url = 'http://oven:80/oven'
    main(url)