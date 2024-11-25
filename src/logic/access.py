import socket
import json
from datetime import datetime
import sqlite3
class AccessControl:

    # Lấy thông tin địachỉ ip trong local
    hostname = socket.gethostname()
    local_machine_ip = socket.gethostbyname(hostname)

    # Xử lý
    def check_access(self, msg, db):
        global local_machine_ip
        timestamp = data.get("updateAt")
        current_time = datetime.fromisoformat(timestamp)
        current_day = current_time.strftime("%a")
        current_hour = current_time.strftime("%H:%M")

        """Kiểm tra quyền truy cập dựa trên thông tin nhận được từ MQTT"""
        data = json.loads(msg)
        
        #Lấy thông tin từ bản tin MQTT
        src_ip = data.get("src_ip")
        user_id = data.get("recognize_id")
        department_id = data.get("department_Id")
        updateAt = data.get("updateAT")

        #Xử lí bản tin
        if (src_ip == local_machine_ip and user_id != "" and updateAt != "") :
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            cursor.execute('''SELECT access_allowed, access_days, start_time, end_time
                           FROM access_rules
                           WHERE recognize_id =? OR department_id = ?
                           ''', (user_id, department_id))
            rule = cursor.fetchone()
            
            if rule:
                access_allowed, access_days, start_time, end_time = rule
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
            
