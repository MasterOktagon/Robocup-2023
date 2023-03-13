from machine import *

i2c = I2C(0, sda=Pin(4), scl=Pin(5))

#  7 6 5 4 3 2 1 0
#  B G B G R B G R
#  3 3 3 2 2 1 1 1

LED1        = const(0x07)
LED2        = const(0x18)
LED3        = const(0xE0)

LED1_GREEN  = const(0x02)
LED1_RED    = const(0x04)
LED1_YELLOW = const(0x06)
LED1_BLUE   = const(0x01)
LED1_LIGHTBLUE = const(0x03)
LED1_LILA  =  const(0x05)
LED1_WHITE =  const(0x07)
LED2_GREEN =  const(0x10)
LED2_RED   =  const(0x08)
LED2_YELLOW = const(0x18)
LED3_GREEN  = const(0x40)
LED3_RED    = const(0x80)
LED3_YELLOW = const(0xC0)
LED3_BLUE   = const(0x20)
LED3_LIGHTBLUE = const(0x60)
LED3_LILA  =  const(0xA0)
LED3_WHITE =  const(0xE0)



class PortExtension:
    def __init__(self,i2c, adr):
        self.adr = adr
        self.i2c = i2c
        self.val = 0
        self.arr = bytearray(1)
        
    def WriteToHardware(self):
        self.arr[0] = ~self.val
        i2c.writeto(self.adr, self.arr)
        
    def SetBit(self,num):
        self.val= self.val | (1 << num)
        self.WriteToHardware()
    
    def ResetBit(self, num):
        self.val = self.val & ~(1<<num)
        self.WriteToHardware()

    def SetBits(self, bits):
        self.val = self.val | bits

    def ResetBits(self, bits):
        self.val = self.val & ~bits
        
    def ToggleBits(self, bits):
        self.val = self.val ^ bits
        self.WriteToHardware()
        
    def WriteAll(self, val):
        self.val = val
        self.WriteToHardware()
        
l = PortExtension(i2c, 32)
blink = 0
timerActive = 0


def TimerCallback(timer):
    global l
    global blink
    l.ToggleBits(blink)
    
    
tim = Timer(freq=3, mode=Timer.PERIODIC, callback=TimerCallback)
tim.deinit()
    
    
def SetLedOn(val):
    global l
    l.SetBits(val)
    l.WriteToHardware()
    
def SetLedOff(val):
    global l
    l.ResetBits(val)
    l.WriteToHardware()
    
    
    
    
    
def SetLedBlinkOn(val, freq_=3):
    global blink
    global tim
    global timerActive
    blink = blink | val
    if (timerActive == 0) and (blink != 0):
        tim.init(freq=freq_, mode=Timer.PERIODIC, callback=TimerCallback)
        timerActive = 1
    
def SetLedBlinkOff(val):
    global blink
    global tim
    global timerActive
    blink = blink & ~val
    if (timerActive == 1) and (blink == 0):
        tim.deinit()
        timerActive = 0

def SetLED(off, on, blink=0, freq=3):
    global l
    if (off != 0):
       l.ResetBits(off)
       SetLedBlinkOff(off)
    l.SetBits(on)
    if (blink != 0):
       SetLedBlinkOn(blink, freq)
    l.WriteToHardware()

    
#SetLed(0, LED1_GREEN|LED3_RED, LED2_YELLOW, freq=5)

#while True:
#    pass



