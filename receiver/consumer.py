import pika
import time

connected = False
# Устанавливаем соединение с RabbitMQ
while not connected:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('172.20.0.4'))
        channel = connection.channel()
        connected = True
    except pika.exceptions.AMQPConnectionError:
        print("Ошибка подключения. Повторная попытка через 6 секунд...")
        time.sleep(6)

counter = 0

# Функция для обработки полученных сообщений
def callback(ch, method, properties, body):
    global counter
    counter += 1
    print(f"Получено сообщение #{counter}", body.decode())

# Слушаем очередь и обрабатываем полученные сообщения
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('Ожидание сообщений. Для выхода нажмите CTRL+C')

# Запускаем бесконечный цикл обработки сообщений
channel.start_consuming()