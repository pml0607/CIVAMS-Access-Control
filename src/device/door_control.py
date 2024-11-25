import time
from gpio_setup import setup_gpio

class DoorControl:
    def __init__(self):
        self.door_pin = setup_gpio()

    def open_door(self, duration=5):
        """Mở cửa trong một khoảng thời gian (giây)"""
        print("Opening door...")
        # Điều khiển GPIO để mở cửa
        time.sleep(duration)
        self.close_door()

    def close_door(self):
        """Đóng cửa"""
        print("Closing door...")
        # Điều khiển GPIO để đóng cửa
