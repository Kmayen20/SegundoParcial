import keyboard
import pyfirmata2
import time
PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)
x=2
while True:
    if keyboard.is_pressed('a'):
        x=x-1
    if keyboard.is_pressed('d'):
        x=x+1    
    board.digital[x].write(1)
    time.sleep(.5)
    board.digital[x].write(0) 
    time.sleep(.1)
