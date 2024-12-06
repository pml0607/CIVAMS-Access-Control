import socket
import json
from datetime import datetime

class AccessControl:

    # Xử lý
    def check_access(self, msg, db):
        hostname = socket.gethostname()
        local_machine_ip = socket.gethostbyname(hostname)
        print(local_machine_ip)
        data = json.loads(msg)

        """Kiểm tra quyền truy cập dựa trên thông tin nhận được từ MQTT"""
        
        #Lấy thông tin từ bản tin MQTT
        src_ip = data.get("src_ip")
        user_id = data.get("recognize_id")
        department_id = data.get("department_Id")
        updateAt = data.get("updatedAt")

        #Xử lý thời gian

        if not isinstance(updateAt, str):
                print(f"Lỗi: `updateAt` không phải chuỗi, giá trị nhận được: {updateAt}")
                return False

        try:
            # Chuyển đổi thời gian từ định dạng ISO 8601 với hậu tố Z
            if updateAt.endswith("Z"):
                updateAt = updateAt.replace("Z", "+00:00")
            current_time = datetime.fromisoformat(updateAt)
        except ValueError as e:
            print(f"Thời gian không hợp lệ trong `updateAt`: {updateAt}. Lỗi: {e}")
            return False
        current_day_of_week = datetime.datetime.now().weekday() + 1
        current_hour = current_time.strftime("%H:%M:%S")
        #Xử lí bản tin
        if (src_ip == local_machine_ip and user_id != "" and updateAt != "") :
            db.connect()

            access_info = db.access(user_id, department_id)
            if access_info:
                start_time, end_time = access_info
                if (start_time <= current_hour <= end_time and current_day_of_week in range(1, 6)):
                    return True
            return False
        else:
            conditions = [src_ip == local_machine_ip, user_id != "", updateAt != ""]
            messages = [
                "IP không khớp",
                "Không có người dùng",
                "Ngày giờ không khả dụng",
            ]

            errors = [msg for cond, msg in zip(conditions, messages) if not cond]
            print("Các lỗi sau được phát hiện:")
            for error in errors:
                print(f"- {error}")
            
