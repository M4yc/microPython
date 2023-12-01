import time
from machine import Pin, ADC, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Configuração do LCD I2C
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Configuração do LM35
lm35_pin = 17  # Pino analógico no Raspberry Pi Pico
#adc = ADC(Pin(lm35_pin))

try:
    while True:
        #lm35_value = adc.read_u16()  # Lê o valor analógico do LM35

        # Converte o valor lido em temperatura (considerando 3.3V de referência e 12 bits de resolução)
        #temp_celsius = (lm35_value / 65535.0) * 330.0

        # Exibe a temperatura no terminal
        print("Temperatura: {:.2f} °C".format(100))

        # Exibe a temperatura no LCD
        lcd.putstr("Temp: {:.2f} C".format(100))

        time.sleep(2)  # Espera 2 segundos para ler um novo valor no sensor
        lcd.clear()

except KeyboardInterrupt:
    pass
