FROM python:3.11-slim-buster

COPY requirements.txt /app/receiver/requirements.txt

RUN pip install -r /app/receiver/requirements.txt
RUN pip install pika
COPY receiver /app/receiver

WORKDIR /app/receiver

CMD ["python", "consumer.py"]
