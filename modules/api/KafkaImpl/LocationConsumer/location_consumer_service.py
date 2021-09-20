from kafka import KafkaConsumer
from json import loads
import psycopg2
import os

kafka_url = os.environ['KAFKA_CONSUMER']
kafka_topic = os.environ['KAFKA_TOPIC']

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

consumer = KafkaConsumer(kafka_topic,
                         bootstrap_servers = kafka_url,
                         value_deserializer=lambda x: loads(x.decode('utf-8'))
                        )

conn = psycopg2.connect( database=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST, port= DB_PORT)
cursor = conn.cursor()

for message in consumer:
    message = message.value
    print(message)
    person_id = int(message['pid'])
    latitude = int(message['latitude'])
    longitude = int(message['longitude'])

    insert_query = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))"\
                    .format(person_id,latitude,longitude)

    cursor.execute(insert_query)
    conn.commit()
conn.close()