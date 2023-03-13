from motor import *
import utime
from sensor_Licht import *
from meinePins import *
#from Bewegungsablauf import *
from allSensors import *
from turn import *
from colorSensor import *

def TestenUndFahren(Va,Vb,t,seite=RECHTS):
    t1 = utime.ticks_ms()
    diff = 0
    OnFwd(MOT_A,Va)
    OnFwd(MOT_B,Vb)
    if seite == RECHTS:
        while diff < t:
            sensor_W.messen()
            if sensor_W.wertR < 20:
                Off(MOT_AB)
                return True
            diff = utime.ticks_ms() - t1
    else:
        while diff < t:
            sensor_W.messen()
            if sensor_W.wertL < 20:
                Off(MOT_AB)
                return True
            diff = utime.ticks_ms() - t1
    Off(MOT_AB)
    return False

def TestenUndFahrenColor(Va,Vb,t,seite=LINKS):
    t1 = utime.ticks_ms() + t
    OnFwd(MOT_A,Va)
    OnFwd(MOT_B,Vb)
    while utime.ticks_ms() < t1:
        sensor_A.messen()
        sensor_G.messen()
        color.update()
        #print(utime.ticks_ms())
        if color.on_black(seite):
            return True
    Off(MOT_AB)
    return False


def run():
    VDose = 550
    OnFwd(MOT_AB,-40)
    utime.sleep(0.5)
    OnFwd(MOT_B,40)
    utime.sleep(1.1)
    OnFwd(MOT_AB,40)
    utime.sleep(0.4)
    Off(MOT_AB)
    utime.sleep(0.5)
    Linie = False
    Linie = TestenUndFahren(50,50,500)
    while not Linie:
        Linie = TestenUndFahren(50,-50,400)
        if Linie:
            break
        Linie = TestenUndFahren(50,50,VDose)
        VDose -= 40
    OnFwd(MOT_AB,40)
    utime.sleep(0.5)
    OnGyro(-70,40)