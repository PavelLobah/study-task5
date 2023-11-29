FROM python:3.11-slim-buster

COPY requirements.txt /app/feed-svc/requirements.txt

RUN pip install -r /app/feed-svc/requirements.txt

COPY feed-svc /app/feed-svc

WORKDIR /app/feed-svc

CMD ["python", "feed-svc.py"]
