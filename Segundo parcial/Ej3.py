import pyfirmata2

from pyfirmata2 import Arduino, util 
import time 
 
port= pyfirmata2.Arduino.AUTODETECT
board=pyfirmata2.Arduino(port)
                                         
it=util.Iterator(board) 
it.start() 

analog0=board.get_pin('a:0:i') 

while True:
##Ascendente 
    dato=analog0.read() 
    print(dato)
    if dato is not None and dato > 0.50:
        x=.2
    else:
        x=1
    board.digital[2].write(1)
    time.sleep(x)
    board.digital[2].write(0) 
    time.sleep(.1)
    board.digital[3].write(1)
    time.sleep(x)
    board.digital[3].write(0) 
    time.sleep(.1)
    board.digital[4].write(1)
    time.sleep(x)
    board.digital[4].write(0) 
    time.sleep(.1)
    board.digital[5].write(1)
    time.sleep(x)
    board.digital[5].write(0) 
    time.sleep(.1)
    board.digital[6].write(1)
    time.sleep(x)
    board.digital[6].write(0) 
    time.sleep(.1)
    board.digital[7].write(1)
    time.sleep(x)
    board.digital[7].write(0) 
    time.sleep(.1)
    board.digital[8].write(1)
    time.sleep(x)
    board.digital[8].write(0) 
    time.sleep(.1)
    board.digital[9].write(1)
    time.sleep(x)
    board.digital[9].write(0) 
    time.sleep(.1)
##Descendente
    board.digital[9].write(1)
    time.sleep(x)
    board.digital[9].write(0) 
    time.sleep(.1)
    board.digital[8].write(1)
    time.sleep(x)
    board.digital[8].write(0) 
    time.sleep(.1)
    board.digital[7].write(1)
    time.sleep(x)
    board.digital[7].write(0) 
    time.sleep(.1)
    board.digital[6].write(1)
    time.sleep(x)
    board.digital[6].write(0) 
    time.sleep(.1)
    board.digital[5].write(1)
    time.sleep(x)
    board.digital[5].write(0) 
    time.sleep(.1)
    board.digital[4].write(1)
    time.sleep(x)
    board.digital[4].write(0) 
    time.sleep(.1)
    board.digital[3].write(1)
    time.sleep(x)
    board.digital[3].write(0) 
    time.sleep(.1)
    board.digital[2].write(1)
    time.sleep(x)
    board.digital[2].write(0) 
    time.sleep(.1)
    