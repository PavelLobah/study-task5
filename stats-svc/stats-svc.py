import pika
import time
import datetime

connected = False
# Устанавливаем соединение с RabbitMQ
while not connected:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('172.20.0.4'))
        channel = connection.channel()
        connected = True
    except pika.exceptions.AMQPConnectionError:
        print("Ошибка подключения. Повторная попытка через 5 секунд...")
        time.sleep(5)

channel.queue_declare(queue='finish_queue')

counter = 0

# Функция для обработки полученных сообщений
def callback(ch, method, properties, body):
    global counter
    counter += 1
    message = eval(body.decode())
    message['published_at'] = str(datetime.datetime.now())
    print(f"Получено сообщение в stats-svc: #{counter}", message)
    channel.basic_publish(exchange='', routing_key='finish_queue', body=str(message))


# Слушаем очередь и обрабатываем полученные сообщения
channel.basic_consume(queue='stats_queue', on_message_callback=callback, auto_ack=True)

print('Ожидание сообщений. Для выхода нажмите CTRL+C')

channel.start_consuming()