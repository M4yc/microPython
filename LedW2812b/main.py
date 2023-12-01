import time
from neopixel import Neopixel
pixels = Neopixel(17, 0, 23, "GRB")

colors = [
  (0xb6, 0xe4, 0x30),
  (0x42, 0xd1, 0xe0),
]

pixel_index = 0
color_index = 0
while True:
  pixels.set_pixel(pixel_index, colors[color_index])
  pixels.show()
  #print(pixel_index, colors[color_index])
  pixel_index += 1
  if pixel_index == 16:
    pixel_index = 0
    color_index = (color_index + 1) % 2
  time.sleep(0.1)
