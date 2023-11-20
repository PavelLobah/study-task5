run:
	python3 sender/producer.py
	python3 receiver/consumer.py
	
docker:
	docker-compose up -d
