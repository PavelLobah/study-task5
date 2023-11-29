import pika
import time
import random

connected = False

# Устанавливаем соединение с RabbitMQ
while not connected:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('172.20.0.4'))
        channel = connection.channel()
        connected = True
    except pika.exceptions.AMQPConnectionError:
        print("Ошибка подключения video-svc. Повторная попытка через 5 секунд...")
        time.sleep(5)

counter1 = 0

channel.exchange_declare(exchange='video_ready_exchange', exchange_type='direct')
channel.queue_declare(queue='feed_queue')
channel.queue_declare(queue='stats_queue')
channel.queue_bind(queue='feed_queue', exchange='video_to_process_exchange', routing_key='feed')
channel.queue_bind(queue='stats_queue', exchange='video_to_process_exchange', routing_key='stats')

def callback(ch, method, properties, body):
    global counter1
    counter1 += 1
    print(f"Получено сообщение в видео сервисе: #{counter1}", body.decode())
    time.sleep(10)
    print(f"Видеопроигрыватель обработал сообщение: #{counter1}", body.decode())

    if random.choice([True, False]):
        channel.basic_publish(exchange='video_ready_exchange', routing_key='stats', body=body)
    else:
        channel.basic_publish(exchange='video_ready_exchange', routing_key='feed', body=body)

channel.basic_consume(queue='video_queue', on_message_callback=callback, auto_ack=True)

print('Ожидание сообщений. Для выхода нажмите CTRL+C')

channel.start_consuming()