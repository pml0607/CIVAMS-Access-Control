import RPi.GPIO as GPIO

def setup_gpio():
    """Cấu hình GPIO cho việc điều khiển relay (mở/đóng cửa)"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)  # GPIO 18 cho relay
    return 18
