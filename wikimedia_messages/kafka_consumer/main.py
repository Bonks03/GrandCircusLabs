from confluent_kafka import Consumer

def main():
    c = Consumer({
        'bootstrap.servers': 'broker:9092',
        'group.id': 'consumer_group',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe(['latest_events'])

    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print('Received message: {}'.format(msg.value().decode('utf-8')))

    c.close()

if __name__ == '__main__':
    main()