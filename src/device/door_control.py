import time
from gpio_setup import GPIO_Setup
from pyA20.gpio import port, gpio

class DoorControl:
	def __init__(self, pin = port.PA7):
		self.gpio_controller = GPIO_Setup(pin = pin, mode = gpio.OUTPUT)
		self.gpio_controller.setup_gpio()
	def open_door(self, duration = 5):
		print("Opening door...")
		self.gpio_controller.set_state(True)
		time.sleep(duration)
		self.close_door()
	def close_door(self):
		print("Closing door...")
		self.gpio_controller.set_state(False)
