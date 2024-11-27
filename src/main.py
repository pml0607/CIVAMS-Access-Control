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

def handle_results(client, userdata,msg):
    """Xử lý kết quả nhận từ MQTT message (face recognition)"""
    # Kiểm tra quyền truy cập
    if access_control.check_access(msg, db):
        door_control.open_door()
    else:
        door_control.close_door()

def handle_sync_request(client, userdata, msg):
    """Xử lý yêu cầu đồng bộ dữ liệu"""
    db_sync.sync(msg)

def handle_auth_token(client, userdata,msg):
    """Lưu token xác thực và đồng bộ với server"""
    auth_manager.update_auth_token(msg)
    db_sync.sync(msg)

if __name__ == "__main__":
    main()
