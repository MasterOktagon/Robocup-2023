from led import *
from meinePins import  *
import taster
import time

def menu():
    # variable zum speichern, ob weiterhin gewartet werden sollte
    SetLED(0xff,0,LED2_YELLOW)
    t = time.ticks_ms() + 4000 # Nach 4s (4000 ms) abbrechen
    while time.ticks_ms() < t:
        if taster.getTotalValue()[0] > 0: # => TASTER B
            return LINKS
        elif taster.getTotalValue()[1] > 0: # => TASTER A
            time.sleep_ms(15)
            while taster.getTotalValue()[1] > 0:
                pass
            SetLED(0xff,0,LED1_YELLOW | LED3_YELLOW)
            time.sleep_ms(15)
            while taster.getTotalValue()[1] == 0:
                pass
            return RECHTS
    return RECHTS
            
