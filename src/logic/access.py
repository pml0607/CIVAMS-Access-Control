import socket
import json
from datetime import datetime

class AccessControl:

    # Lấy thông tin địachỉ ip trong local
    hostname = socket.gethostname()
    local_machine_ip = socket.gethostbyname(hostname)

    # Xử lý
    def check_access(self, msg, db):
        global local_machine_ip
        data = json.loads(msg)

        """Kiểm tra quyền truy cập dựa trên thông tin nhận được từ MQTT"""
        
        #Lấy thông tin từ bản tin MQTT
        src_ip = data.get("src_ip")
        user_id = data.get("recognize_id")
        department_id = data.get("department_Id")
        updateAt = data.get("updateAt")

        #Xử lý thời gian

        if not isinstance(update_at, str):
                print(f"Lỗi: `updateAt` không phải chuỗi, giá trị nhận được: {update_at}")
                return False

        try:
            # Chuyển đổi thời gian từ định dạng ISO 8601 với hậu tố Z
            if update_at.endswith("Z"):
                update_at = update_at.replace("Z", "+00:00")
            current_time = datetime.fromisoformat(update_at)
        except ValueError as e:
            print(f"Thời gian không hợp lệ trong `updateAt`: {update_at}. Lỗi: {e}")
            return False
        current_day = current_time.strftime("%a")
        current_hour = current_time.strftime("%H:%M")
        #Xử lí bản tin
        if (src_ip == local_machine_ip and user_id != "" and updateAt != "") :
            db.connect()

            access_info = db.access(user_id, department_id)
            if access_info:
                access_allowed, access_days, start_time, end_time = access_info
                if (access_allowed and current_day in access_days.split(",") 
                    and start_time <= current_hour <= end_time):
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
            
