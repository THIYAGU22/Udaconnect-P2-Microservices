FROM python:3.8-slim

WORKDIR /LocationConsumer

COPY . .

ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

CMD [ "python3", "location_consumer_service.py" ]