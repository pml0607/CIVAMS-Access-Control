import paho.mqtt.client as mqtt
import json
from mqtt.topics import TOPICS
from config import MQTT_BROKER, MQTT_PASSWORD, MQTT_PORT, MQTT_USERNAME

class MQTTClient:
    def __init__(self, message_handler):
        self.client = mqtt.Client()
        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.on_message = self.on_message
        self.message_handler = message_handler

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.paylod.decode())
        self.message_handler(msg.topic, payload)

    def start(self):
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        for topic in TOPICS:
            self.client.subscribe(topic)
        print("MQTT Client started.")
        self.client.loop_forever()