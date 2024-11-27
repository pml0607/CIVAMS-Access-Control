from mqtt.client import MqttClient
from logic.access import AccessControl
from logic.db_sync import DatabaseSync
from logic.auth import AuthManager
from device.door_control import DoorControl
from database.db import Database

# Khởi tạo các module
mqtt_client = MqttClient()
access_control = AccessControl()
db_sync = DatabaseSync()
auth_manager = AuthManager()
door_control = DoorControl()
db = Database("access_control.db")

def main():
    mqtt_client.connect()
    # Đăng ký các topic
    mqtt_client.subscribe("topic/results/#", handle_results)
    mqtt_client.subscribe("topic/face_terminal/sync_request/", handle_sync_request)
    mqtt_client.subscribe("topic/Device/AuthenToken/", handle_auth_token)

    # Khởi động chương trình
    mqtt_client.loop_forever()

def handle_results(client, userdata, msg):
    """Xử lý kết quả nhận từ MQTT message (face recognition)"""
    # Kiểm tra quyền truy cập
    payload = msg.payload.decode()
    try:
        # Kiểm tra quyền truy cập
        if access_control.check_access(payload, db):
            door_control.open_door()
        else:
            door_control.close_door()
    except Exception as e:
        print(f"Lỗi trong handle_results: {e}")


def handle_sync_request(client, userdata, msg):
    """Xử lý yêu cầu đồng bộ dữ liệu"""
    payload = msg.payload.decode()
    db_sync.sync(payload)

def handle_auth_token(client, userdata, msg):
    """Lưu token xác thực và đồng bộ với server"""
    payload = msg.payload.decode()
    auth_manager.update_auth_token(payload)
    db_sync.sync(payload)

if __name__ == "__main__":
    main()
