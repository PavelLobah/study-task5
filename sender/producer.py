import pika
import time

connected = False
# Устанавливаем соединение с RabbitMQ
while not connected:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('172.20.0.4'))
        channel = connection.channel()
        channel.exchange_declare(
            exchange='my_exchange', exchange_type='direct')
        channel.queue_declare(queue='hello')
        channel.queue_bind(
            queue='hello', exchange='my_exchange', routing_key='hello')
        connected = True
    except pika.exceptions.AMQPConnectionError:
        print("Ошибка подключения. Повторная попытка через 5 секунд...")
        time.sleep(5)

counter = 0
# Функция для отправки сообщений

def send_message():
    global counter
    counter += 1
    channel.basic_publish(exchange='', routing_key='hello',
                          body='Hello, RabbitMQ!')
    print(f"Сообщение успешно отправлено №{counter}")


# Отправляем сообщения с интервалом в 2 секунды
while True:
    send_message()
    time.sleep(2)


# Закрываем соединение
connection.close()
