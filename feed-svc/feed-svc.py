import random
import pika
import time

connected = False
# Устанавливаем соединение с RabbitMQ
while not connected:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('172.20.0.4'))
        channel = connection.channel()
        connected = True
    except pika.exceptions.AMQPConnectionError:
        print("Ошибка подключения feed-svc. Повторная попытка через 5 секунд...")
        time.sleep(5)

counter1 = 0

channel.exchange_declare(
    exchange='video_to_process_exchange', exchange_type='direct')
channel.queue_declare(queue='video_queue')
channel.queue_declare(queue='stats_queue')
channel.queue_bind(
    queue='video_queue', exchange='video_to_process_exchange', routing_key='video')
channel.queue_bind(
    queue='stats_queue', exchange='video_to_process_exchange', routing_key='stats')


def callback(ch, method, properties, body):
    global counter1
    counter1 += 1
    message = eval(body.decode())
    print(f"Получено сообщение в feed-svc сервисе: #{counter1}", message['message'])
    if message['message'] == "Видео":
        channel.basic_publish(exchange='video_to_process_exchange', routing_key='video', body=body)
    elif message['message'] == "Изображение":
        channel.basic_publish(exchange='video_to_process_exchange', routing_key='stats', body=body)


channel.basic_consume(queue='actor_queue',
                      on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='feed_queue',
                      on_message_callback=callback, auto_ack=True)
print('Ожидание сообщений. Для выхода нажмите CTRL+C')

channel.start_consuming()
