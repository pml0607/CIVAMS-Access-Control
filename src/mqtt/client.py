import paho.mqtt.client as mqtt
from config import MQTT_CONFIG

class MqttClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(MQTT_CONFIG['username'], MQTT_CONFIG['password'])
        self.client.tls_set(ca_certs = MQTT_CONFIG['ca_cert'], 
                            certfile = MQTT_CONFIG['client_cert'], 
                            keyfile = MQTT_CONFIG['client_key'])

    def connect(self):
        """Kết nối với MQTT broker"""
        self.client.connect(MQTT_CONFIG['broker'], MQTT_CONFIG['port'], 60)

    def subscribe(self, topic, callback):
        """Đăng ký topic để nhận tin nhắn"""
        self.client.subscribe(topic)
        self.client.message_callback_add(topic, callback)

    def on_connect(self, client, userdata, flags, rc):
        """Callback khi kết nối thành công"""
        print(f"Connected with result code {rc}")
    
    def on_message(self, msg):
        """Callback khi nhận tin nhắn"""
        print(f"Message received: {msg.payload.decode()}")
    
    def loop_forever(self):
        """Bắt đầu nhận và xử lý tin nhắn MQTT"""
        self.client.loop_forever()
