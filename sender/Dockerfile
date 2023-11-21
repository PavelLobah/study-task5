FROM python:3.11-slim-buster

COPY requirements.txt /app/sender/requirements.txt

RUN pip install -r /app/sender/requirements.txt

COPY sender /app/sender

WORKDIR /app/sender

CMD ["python", "producer.py"]
