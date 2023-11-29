FROM python:3.11-slim-buster

COPY requirements.txt /app/stats-svc/requirements.txt

RUN pip install -r /app/stats-svc/requirements.txt

COPY stats-svc /app/stats-svc

WORKDIR /app/stats-svc

CMD ["python", "stats-svc.py"]
