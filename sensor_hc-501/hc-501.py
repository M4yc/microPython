from machine import Pin
from time import sleep

# Configura莽茫o do sensor PIR
pir_sensor = Pin(3, Pin.IN)  # Substitua pelo pino correto

try:
    while True:
        pir_value = pir_sensor.value()  # L锚 o valor do sensor PIR

        # Exibe o valor do sensor na sa铆da serial
        if pir_value:
            print("Movimento Detectado")
        else:
            print("Sem Movimento")

        sleep(1)  # Espera um segundo antes de ler novamente

except KeyboardInterrupt:
    pass
