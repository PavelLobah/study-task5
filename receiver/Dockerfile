# Dockerfile для получателя (receiver)
FROM python:3.11-slim-buster

WORKDIR /app/receiver

COPY receiver/consumer.py .

RUN pip install pika

CMD ["python", "consumer.py"]