#Programa para sensor LM35 com Display LCD I2C

import time
from machine import Pin, SoftI2C, ADC
from lib_lcd1602_2004_with_i2c import LCD

scl_pin = 5
sda_pin = 4
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))

lm35 = 0 #ADC (pino analogico 0) no ESP8266
adc = ADC(0) #Cria um objeto ADC para o ADC0

# 0000000000000000
try:
    while True:
        lm35_value = adc.read()  # Le o valor analogico do LM35

        # Converte o valor lido em temperatura (considerando 10 mV por grau Celsius)
        #temperature_celsius = (lm35_value / 1024.0) * 330.0
        temp_celsius = (lm35 / 1024) * 330
        # Exibe a temperatura na saida serial
        print("Temperatura: {:.2f} °C".format(temperature_celsius))
        lcd.puts("Temperatura: {:.2f} °C".format(temp_celsius))
        time.sleep(2)  # espera 2 segundos para ler um novo valor no sensor
        lcd.clear()


except KeyboardInterrupt:
    pass




