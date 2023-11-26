import pika
import time

connected = False

while not connected:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('172.20.0.4'))
        channel = connection.channel()
        channel.exchange_declare(
            exchange='video_to_process_exchange', exchange_type='direct')
        channel.queue_declare(queue='video_queue')
        channel.queue_declare(queue='stats_queue')
        channel.queue_bind(
            queue='video_queue', exchange='video_to_process_exchange', routing_key='video')
        channel.queue_bind(
            queue='stats_queue', exchange='video_to_process_exchange', routing_key='stats')
        connected = True
    except pika.exceptions.AMQPConnectionError:
        print("Ошибка подключения. Повторная попытка через 5 секунд...")
        time.sleep(5)

counter = 0

def send_message(message, routing_key):
    global counter
    counter += 1
    channel.basic_publish(exchange='video_to_process_exchange', routing_key=routing_key, body=message)
    print(f"Сообщение успешно отправлено №{counter}")

while True:
    video_message = "Видео для обработки"
    stats_message = "Статистика для обработки"
    send_message(video_message, routing_key='video')
    send_message(stats_message, routing_key='stats')
    time.sleep(0.5)

connection.close()