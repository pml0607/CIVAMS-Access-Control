import requests
import json
import logging
from dotenv import load_dotenv
import os
from database.db import Database

class DatabaseSync:
    def __init__(self):
        load_dotenv()  # Đảm bảo môi trường được tải
        self.api_url = os.getenv("API_URL")
        self.auth_token = os.getenv("AUTH_TOKEN")
        
        # Kiểm tra sự tồn tại của API URL và AUTH TOKEN
        if not self.api_url or not self.auth_token:
            logging.error("API URL hoặc AUTH_TOKEN không được cấu hình trong môi trường.")
            raise ValueError("API URL hoặc AUTH_TOKEN không hợp lệ.")
        
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": self.auth_token,
        }

    def sync(self, payload):
        """
        Đồng bộ dữ liệu từ thông điệp MQTT.
        """
        try:
            data = json.loads(payload)
            device_id = data.get("deviceId")
            db_update = data.get("dbUpdate", [])

            if not device_id or not db_update:
                logging.error("Payload không hợp lệ hoặc thiếu thông tin cần thiết")
                return
            local_device_id = "000000004115741d"
            if device_id != local_device_id:
                print("deviceId không khớp")
                return
            for table_name in db_update:
                last_update_time = self.get_last_update_time(table_name)

                if not last_update_time:
                    logging.warning(f"Không thể lấy thời gian cập nhật cuối cho bảng {table_name}")
                    continue

                response = self.call_update_api(table_name, last_update_time)

                if response:
                    self.update_local_db(table_name, response)
                else:
                    logging.error(f"Không có dữ liệu để cập nhật cho bảng {table_name}")

        except json.JSONDecodeError as e:
            logging.error(f"Lỗi khi phân tích JSON payload: {e}")
        except Exception as e:
            logging.error(f"Lỗi trong quá trình đồng bộ: {e}")

    def get_last_update_time(self, table_name):
        """
        Lấy thời gian cập nhật cuối cùng của bảng từ cơ sở dữ liệu cục bộ.
        Args:
            table_name (str): Tên bảng.
        Returns:
            str: Thời gian cập nhật cuối cùng dạng ISO8601.
        """
        db = Database("access_control.db")
        try:
            db.execute(f"SELECT MAX(updated_at) FROM")
        # Thay thế với truy vấn thực tế tới cơ sở dữ liệu
        return "2022-03-31T08:04:35.825Z"

    def call_update_api(self, table_name, last_update_time):
        """
        Gửi yêu cầu tới API để lấy dữ liệu cập nhật.
        Args:
            table_name (str): Tên bảng.
            last_update_time (str): Thời gian cập nhật cuối cùng.
        Returns:
            dict: Dữ liệu nhận được từ API.
        """
        payload = [
            {
                "lastPulledAt": last_update_time,
                "tableName": table_name,
            }
        ]

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            if response.status_code == 200:
                logging.info(f"Đồng bộ thành công cho bảng {table_name}")
                return response.json()
            else:
                logging.error(f"API trả về lỗi cho bảng {table_name}, mã lỗi: {response.status_code}, chi tiết: {response.text}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Lỗi khi gọi API cho bảng {table_name}: {e}")
        return None

    def update_local_db(self, table_name, data):
        """
        Cập nhật cơ sở dữ liệu cục bộ với dữ liệu mới.
        Args:
            table_name (str): Tên bảng.
            data (dict): Dữ liệu mới để cập nhật.
        """
        # Thay thế bằng logic thực tế để cập nhật cơ sở dữ liệu cục bộ
        logging.info(f"Cập nhật bảng {table_name} với dữ liệu: {data}")
