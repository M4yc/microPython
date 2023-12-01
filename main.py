import time
from machine import Pin, SoftI2C, ADC
from lib_lcd1602_2004_with_i2c import LCD

scl_pin = 5
sda_pin = 4
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))

lm35_pin = 0  # Pino analógico 0 no ESP8266
adc = ADC(0)  # Cria um objeto ADC para o ADC0

try:
    while True:
        lm35_value = adc.read_u16()  # Lê o valor analógico do LM35

        # Converte o valor lido em temperatura (considerando 3.3V de referência e 12 bits de resolução)
        temp_celsius = 100

        # Exibe a temperatura na saída serial
        print("Temperatura: {:.2f} °C".format(temp_celsius))

        # Exibe a temperatura no LCD
        lcd.puts("Temperatura: {:.2f} °C".format(temp_celsius))

        time.sleep(2)  # Espera 2 segundos para ler um novo valor no sensor
        lcd.clear()

except KeyboardInterrupt:
    pass
