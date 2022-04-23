import pyfirmata2

from pyfirmata2 import Arduino, util 
import time 
 
port= pyfirmata2.Arduino.AUTODETECT
board=pyfirmata2.Arduino(port)

while True:
## 1 segundo
    board.digital[2].write(1)
    time.sleep(1)
    board.digital[2].write(0) 
    time.sleep(.1)
    board.digital[3].write(1)
    time.sleep(1)
    board.digital[3].write(0) 
    time.sleep(.1)
    board.digital[4].write(1)
    time.sleep(1)
    board.digital[4].write(0) 
    time.sleep(.1)
    board.digital[5].write(1)
    time.sleep(1)
    board.digital[5].write(0) 
    time.sleep(.1)
## 2 segundos
    board.digital[6].write(1)
    time.sleep(2)
    board.digital[6].write(0) 
    time.sleep(.1)
    board.digital[7].write(1)
    time.sleep(2)
    board.digital[7].write(0) 
    time.sleep(.1)
    board.digital[8].write(1)
    time.sleep(2)
    board.digital[8].write(0) 
    time.sleep(.1)
    board.digital[9].write(1)
    time.sleep(2)
    board.digital[9].write(0) 
    time.sleep(.1)