# -*- coding: utf-8 -*-
__author__ = 'LiYuanhe'
import time
from machine import Pin, SoftI2C
from lib_lcd1602_2004_with_i2c import LCD
scl_pin = 5
sda_pin = 4
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))

custom_char_0 = [
  0B00000,
  0B00000,
  0B01010,
  0B11111,
  0B11111,
  0B01110,
  0B00100,
  0B00000
]
lcd.create_charactor(0,custom_char_0)
#0000000000000000

while True:
  lcd.puts("I2C LCD Sucesso ")
  time.sleep(2)
  lcd.clear()
  lcd.puts("Inicializando a Contagem de 0-14")
  time.sleep(2)
  lcd.clear()
  for i in range(15):
    lcd.puts(str(i))
    lcd.puts(chr(0),1,0)
    time.sleep(1)
    lcd.clear()
    

