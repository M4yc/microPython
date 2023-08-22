from lcd_i2c import LCD_I2C
from machine import I2C, Pin

#PCF8574 on 0x50
I2C_ADDR = 0x27 #DEC 39, HEX 0x27
NUM_ROWS = 2
NUM_COLS = 16

i2c = I2C(0, scl=Pin(20),sda=Pin(19), freq=800000)
lcd = LCD_I2C(addr=I2C_ADDR,cols=NUM_COLS,rows=NUM_ROWS, i2c=i2c)

lcd.begin()
lcd.print("hello word")