print("Hello, World")
print("Tentando fazer o micro python funcionar")
from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
led.value(False)

while True:
    led.value(not led.value())
    sleep(1)