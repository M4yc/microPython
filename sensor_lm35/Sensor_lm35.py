from machine import ADC,Pin
from time import sleep

# Configura鑾借尗o do sensor de temperatura LM35
lm35_pin = 0  # ADC0 (pino analogico 0) no ESP8266
adc = ADC(0)  # Cria um objeto ADC para o ADC0

try:
    while True:
        lm35_value = adc.read()  # Le o valor analogico do LM35

        # Converte o valor lido em temperatura (considerando 10 mV por grau Celsius)
        temperature_celsius = (lm35_value / 1024.0) * 330.0

        # Exibe a temperatura na saida serial
        print("Temperatura: {:.2f} 鎺矯".format(temperature_celsius))

        sleep(1)  # Espera um segundo antes de ler novamente

except KeyboardInterrupt:
    pass

