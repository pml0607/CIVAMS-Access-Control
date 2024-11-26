from pyA20.gpio import gpio
from pyA20.gpio import port

def setup_gpio():
    """Cấu hình GPIO cho việc điều khiển relay (mở/đóng cửa)"""
    gpio.init()
    gpio.setcfg(port.PA7, gpio.OUTPUT)
    return 7
