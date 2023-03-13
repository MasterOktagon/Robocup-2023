from machine import *
from motor import *
import utime

V = 50

lichtW = Pin(20,Pin.OUT)
lichtG = Pin(19,Pin.OUT)
lichtR = Pin(9,Pin.OUT)
lichtA = Pin(18,Pin.OUT)
LEDs = [lichtW,lichtR,lichtG,lichtA] 

for i in range (1):
    for s in LEDs:
        s.value(1)
        utime.sleep(1)
        s.value(0)
        utime.sleep(1)

SilberLED = machine.Pin(LED_S,machine.Pin.OUT)
SilberLED.on()
utime.sleep(1)
SilberLED.off()
SilberSensor = machine.ADC(SENSOR_S)

while True:
    
    print("An",SilberSensor.read_u16())
    utime.sleep(3)
    OnFwd(MOT_AB, V)
    utime.sleep(3)
    Off(MOT_AB)
    print("Aus")
    utime.sleep(3)
