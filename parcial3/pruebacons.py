from kafka import KafkaConsumer

consumer = KafkaConsumer('quickstart-events', bootstrap_servers = ['localhost:9092'])
for mes in consumer:
        print(mes.value.decode("utf-8"))
