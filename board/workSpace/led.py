from machine import Pin

led2 = Pin(2, Pin.OUT)

def led2_on():
  led2.value(1)
  
def led2_off():
  led2.value(0)
