import pika
import time
import random
import datetime

connected = False
# Устанавливаем соединение с RabbitMQ
while not connected:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('172.20.0.4'))
        channel = connection.channel()
        connected = True
    except pika.exceptions.AMQPConnectionError:
        print("Ошибка подключения producer. Повторная попытка через 5 секунд...")
        time.sleep(6)

channel.queue_declare(queue='actor_queue')

counter = 0

def send_message(message):
    global counter
    counter += 1
    channel.basic_publish(exchange='', routing_key='actor_queue', body=message)
    print(f"Сообщение успешно отправлено №{counter}")

def random_message():
    choices = ['Видео', 'Картинка']
    return random.choice(choices)

while True:
    message_type = random_message()
    if message_type == 'Видео':
        video_message = {
            'message': 'Видео',
            'created_at': str(datetime.datetime.now()),
            'published_at': ''
        }
        send_message(str(video_message))
    else:
        image_message = {
            'message': 'Изображение',
            'created_at': str(datetime.datetime.now()),
            'published_at': ''
        }
        send_message(str(image_message))
    time.sleep(1)

connection.close()