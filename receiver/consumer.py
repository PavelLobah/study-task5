import pika

# Устанавливаем соединение с RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('172.20.0.3'))
channel = connection.channel()

# Создаем очередь
channel.queue_declare(queue='hello')

# Функция для обработки полученных сообщений
def callback(ch, method, properties, body):
    print("Получено сообщение:", body)

# Слушаем очередь и обрабатываем полученные сообщения
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('Ожидание сообщений. Для выхода нажмите CTRL+C')

# Запускаем бесконечный цикл обработки сообщений
channel.start_consuming()