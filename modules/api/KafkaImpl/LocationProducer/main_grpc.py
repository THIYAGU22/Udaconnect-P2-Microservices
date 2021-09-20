import os
import logging
from concurrent import futures
from kafka import KafkaProducer
import grpc
from json import dumps
import locations_pb2
import locations_pb2_grpc

# kafka_url = os.environ['KAFKA_BROKER']
# kafka_topic = os.environ['KAFKA_TOPIC']

kafka_url = os.environ['KAFKA_BROKER']
kafka_topic = os.environ['KAFKA_TOPIC']
producer = KafkaProducer(bootstrap_servers=kafka_url, value_serializer=lambda x: dumps(x).encode('utf-8'))


class LocationEventServicer(locations_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Received a message!")
        data = {
            "pid": int(request.pid),
            "latitude": int(request.latitude),
            "longitude": int(request.longitude)
        }
        logging.info('processing entity ', data)
        print(data)
        producer.send(kafka_topic, value=data)
        return locations_pb2.LocationMessage(**data)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
locations_pb2_grpc.add_LocationServiceServicer_to_server(LocationEventServicer(), server)

print("Server starting on port 30003...")
server.add_insecure_port("[::]:30003")
server.start()
server.wait_for_termination()
