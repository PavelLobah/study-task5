# Dockerfile для отправителя (sender)
FROM python:3.11-slim-buster

WORKDIR /app/sender

COPY sender/producer.py .

RUN pip install pika

CMD ["python", "producer.py"]
