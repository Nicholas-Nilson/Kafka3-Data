from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: dumps(m).encode('ascii'))

for e in range(1000):
    data = {'number' : e, 'special' : 'nick', 'language' : 'duhhhhrrrrr'}
    print(data)
    producer.send('test', value=data)
    sleep(5)
