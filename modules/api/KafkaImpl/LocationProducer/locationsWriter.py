import grpc
import locations_pb2
import locations_pb2_grpc
import logging

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:30003")
stub = locations_pb2_grpc.LocationServiceStub(channel)

location1 = locations_pb2.LocationMessage(
    pid=122,
    latitude=55,
    longitude=110
)

location2 = locations_pb2.LocationMessage(
    pid=123,
    latitude=65,
    longitude=90
)

sent_response_1 = stub.Create(location1)
sent_response_2 = stub.Create(location2)

print("data points uploaded")
logging.info(sent_response_1)
print("response 1", sent_response_1)
print("response 2", sent_response_2)
