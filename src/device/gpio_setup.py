from pyA20.gpio import gpio
from pyA20.gpio import port


class GPIO_Setup:
    def __init__(self, pin, mode):
	self.pin = pin
	self.mode = mode
	self.state = None
	self.initialized = False


    def setup_gpio(self):
        """Cấu hình GPIO cho việc điều khiển relay (mở/đóng cửa)"""
        gpio.init()
        gpio.setcfg(self.pin, self.mode)
        self.initialized = True
	if self.mode == gpio.OUTPUT:
	    self.state = gpio.LOW
	    gpio.output(self.pin, self.state)

    def set_state(self.state):
	if not self.initialized:
	    raise RuntimeError("GPIO chưa được khởi tạo!")
	if self.mode != gpio.OUTPUT:
	    raise RuntimeError("GPIO không ở ché độ OUTPUT!")
	self.state = gpio.HIGH if state else gpio.LOW
	gpio.output(self.pin, self.state)

    def get_state(self):
        """Lấy trạng thái hiện tại của GPIO"""
        if not self.initialized:
            raise RuntimeError("GPIO chưa được khởi tạo!")
        if self.mode == gpio.INPUT:
            self.state = gpio.input(self.pin)
        return self.state
