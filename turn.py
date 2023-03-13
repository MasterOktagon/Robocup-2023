from motor import *
import utime
from gyro import *
from allSensors import *
from meinePins import *

#Off()
ns = RotSensor()
ns.messeOffset()

def Debug(lvl,*text):
    """
    Funktion, die je nach Debug-Level verschieden viel ausgibt
    """
    if lvl <= DEBUG:
        print(text)

def OnGyro(deg, V, testen=None):         # positiver Winkel = links; negativer Winkel = rechts
    ns.init()
    ns.messeRot()
    if deg > 0:
        OnFwd(MOT_A,V) 
        OnFwd(MOT_B,-V)
        while ns.summex < deg:
            #utime.sleep_ms(3)
            ns.messeRot()
            if testen != None:
                sensor_W.messen()
                
                if testen == LINKS and sensor_W.wertL <=GRAU:
                    return
                elif sensor_W.wertR <=GRAU:
                    return
            #print(ns.summex)
                
    elif deg < 0:
        OnFwd(MOT_A,-V)
        OnFwd(MOT_B,V)
        while ns.summex > deg:
            #utime.sleep_ms(3)
            ns.messeRot()
            if testen != None:
                sensor_W.messen()
                if testen == LINKS and sensor_W.wertL <=GRAU:
                    return
                elif sensor_W.wertR <=GRAU:
                    return
            #print(ns.summex)
    

    
if __name__ == "__main__":
    OnGyro(90, 60)
    utime.sleep(1)
    OnGyro(-90, 80)
    Off()