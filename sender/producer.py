import pika
import time

# Устанавливаем соединение с RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создаем очередь
channel.queue_declare(queue='hello')

# Функция для отправки сообщений
def send_message():
    channel.basic_publish(exchange='', routing_key='hello', body='Hello, RabbitMQ!')
    print("Сообщение успешно отправлено")

# Отправляем сообщения с интервалом в 2 секунды
while True:
    send_message()
    time.sleep(2)

# Закрываем соединение
connection.close()