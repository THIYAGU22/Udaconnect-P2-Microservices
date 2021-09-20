FROM python:3.8-slim

WORKDIR /LocationProducer


EXPOSE 5005

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "main_grpc.py" ]