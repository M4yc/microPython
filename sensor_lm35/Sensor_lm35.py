from machine import ADC
from time import sleep

# Configura莽茫o do sensor de temperatura LM35
lm35_pin = 0  # ADC0 (pino anal贸gico 0) no ESP8266
adc = ADC(0)  # Cria um objeto ADC para o ADC0

try:
    while True:
        lm35_value = adc.read()  # L锚 o valor anal贸gico do LM35

        # Converte o valor lido em temperatura (considerando 10 mV por grau Celsius)
        temperature_celsius = (lm35_value / 1024.0) * 330.0

        # Exibe a temperatura na sa铆da serial
        print("Temperatura: {:.2f}掳C".format(temperature_celsius))

        sleep(1)  # Espera um segundo antes de ler novamente

except KeyboardInterrupt:
    pass
