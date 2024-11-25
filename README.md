# Civams Access Control

Hệ thống quản lý truy cập dựa trên nhận diện khuôn mặt và MQTT.

## Cấu hình

Cập nhật các thông số trong `config.py` để kết nối với MQTT broker và thiết bị.

## Cài đặt

1. Cài đặt các thư viện yêu cầu:
    ```bash
    pip install -r requirements.txt
    ```
2. Chạy ứng dụng:
    ```bash
    python main.py
    ```

## Các chức năng
- Kiểm tra quyền truy cập từ kết quả nhận diện khuôn mặt.
- Đồng bộ dữ liệu từ server.
- Quản lý token xác thực.
- Điều khiển mở/đóng cửa.
