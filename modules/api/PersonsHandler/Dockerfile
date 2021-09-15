FROM python:3.7-alpine

WORKDIR /PersonsHandler

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

EXPOSE 5000

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]