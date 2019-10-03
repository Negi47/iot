import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input
while 1:
    if(IO.input(14)==True): 
        IO.output(2,True) 
        IO.output(3,False) 
    
    if(IO.input(14)==False): 
        IO.output(3,True) 
        IO.output(2,False)
