from confluent_kafka import Producer
import requests

def main(url):
    p = Producer({'bootstrap.servers': 'broker:9092'})
    s = requests.Session()

    def delivery_report(err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


    with s.get(url, stream=True) as resp:
        for line in resp.iter_lines():
            if line:
                p.poll(0)
                line_str = line.decode('utf-8')
                p.produce('latest_events', line_str.encode('utf-8'), callback=delivery_report)

    p.flush()
    
if __name__ == '__main__':
    url = 'https://stream.wikimedia.org/v2/stream/recentchange'
    main(url)