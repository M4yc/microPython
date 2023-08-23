from machine import Pin
from time import sleep

rele = Pin(16,Pin.OUT)
rele.value(0)

for i in range(10):
    rele.value(not rele.value())
    sleep(2)
