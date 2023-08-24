
import time
from machine import Pin, SoftI2C, ADC
from lib_lcd1602_2004_with_i2c import LCD

scl_pin = 5
sda_pin = 4
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))

lm35 = 0 #ADC (pino analogico 0) no ESP8266
adc = ADC(0) #Cria um objeto ADC para o ADC0

# 0000000000000000

while True:
    lm35_value = adc.read()

    temp_celsius = (lm35/1024)*330

    lcd.puts("Temperatura: {:.2f} °C".format(temp_celsius))
    time.sleep(2)#espera 2 segundos para ler um novo valor no sensor
    lcd.clear()
