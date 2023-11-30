import neopixel
import machine
import time

# Configuração dos LEDs
pin = machine.Pin(23)  # Escolha o número do pino apropriado
num_leds = 1           # Número de LEDs no seu conjunto

pixels = neopixel.NeoPixel(pin, num_leds)

# Função para definir a cor de todos os LEDs
def set_color(color):
    for i in range(num_leds):
        pixels[i] = color
    pixels.write()

# Teste de cores
set_color((255, 0, 0))  # Vermelho
time.sleep(1)
set_color((0, 255, 0))  # Verde
time.sleep(1)
set_color((0, 0, 255))  # Azul
time.sleep(1)

# Desligar todos os LEDs
set_color((0, 0, 0))