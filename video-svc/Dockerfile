FROM python:3.11-slim-buster

COPY requirements.txt /app/video-svc/requirements.txt

RUN pip install -r /app/video-svc/requirements.txt

COPY video-svc /app/video-svc

WORKDIR /app/video-svc

CMD ["python", "video-svc.py"]
