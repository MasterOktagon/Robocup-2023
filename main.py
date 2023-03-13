import utime # Zeit-modul (built-in)
import taster # Taster-modul
from motor import * # Fahern-modul
from meinePins import * #konstanten-modul
from turn import * #gyro-modul
import dose #doseUmfahren und testenUndFahren-modul
from sensor_Licht import * #sensor-modul
import speicher #speicher-modul
import machine #hardware-modul (built-in)
from allSensors import * #all sensoren in einem Modul
from gruen import * #deprecated
import menu #Hauptmenue-modul

from led import * #status-led-modul
from colorSensor import * #farberkennungs-modul
#------------------------------------------------------
# v0.9.1 - Stand 10.03.2023
__version__ = "0.9.6"

led = machine.Pin(25,machine.Pin.OUT) #Energie-LED
led.on()
SilberSensor = machine.ADC(SENSOR_S)
SilberLED = machine.Pin(LED_S,machine.Pin.OUT)


diff = 0                         # differenz zum fahren

def Debug(lvl,*text):
    """
    Funktion, die je nach Debug-Level verschieden viel ausgibt
    """
    if lvl <= DEBUG:
        print(text)

#---------------------------HAUPTSCHLEIFE---------------------------#
Off(MOT_AB)                     # Init im Stillstand

#menue:
#A => Kalibrieren
#B => Warten
#sonst Laden/Starten (4s Zeit)

print("Menu: Choose option: A => Kal; B => Wait")
if menu.menu() == RECHTS:
    speicher.LadeWerte([sensor_W,sensor_A,sensor_R,sensor_G])
else:
    print("Kalibrieren...")
    kalibrieren()
    print("...Beendet")
      
SetLED(0xff,0,0)
utime.sleep(1)


z=1 # Linienfolger-Variablen
n=2

#-----------------------

for s in sensoren: # Min/Max Debug der Sensoren
     Debug(1,s.name, s.miniL, s.maxiL, s.miniR, s.maxiR) # Bildschirmausgabe der Werte

print("Main")
while True:
    for s in sensoren: # Lichtwerte messen
        s.messen()
        #Debug(3,s.name, s.wertL, s.wertR)
    #SetLED(0xff,0,0) #Status-LEDs aus
    color.update()
    
    #print(color.on_black(LINKS), "L        \tR", color.on_black(RECHTS))
    #utime.sleep_ms(100)

    diff = sensor_W.wertL - sensor_W.wertR # Differenzen bilden vb vb vb vb vb vb vb vb vb vb vb vb vb vb vb vb vb vb vb
    Adiff = sensor_A.wertL - sensor_A.wertR
    if abs(Adiff) < 25:
        Adiff=0
    
    
    
    vupdate = z*(diff + Adiff*3)//n # Geschwindigkeitsaenderung: Gewichtung: Innen: 1; Aussen: 3; Mult.: 1
    #Debug(2,vupdate)
    #if vupdate > 30: SetLED(0,LED2_RED,0) #Starke differenz
    
    OnFwd(MOT_B,V + vupdate ) # Geschwindigkeit wird Addiert/Subtrahiert um eine Drehung zu erzeugen
    OnFwd(MOT_A,V - vupdate )
    if color.on_green(LINKS):
        SetLED(0,LED1_GREEN,0)
        OnFwd(MOT_AB,V/2)
        for i in range(200):
            for s in sensoren:
                s.messen()
            color.update()
            #utime.sleep_ms(10)
        if color.on_green(RECHTS): # L+R => Beide Seiten; 180-Grad-Drehung
            Off()
            SetLED(0,LED3_GREEN,0)
            print("Grüner Punkt - LR")
            
            if dose.TestenUndFahrenColor(V/2,V/2,500): # -> schwarze Linie
                OnFwd(MOT_AB,V/2)
                utime.sleep_ms(1200)
                OnGyro(180, V)
                OnFwd(MOT_AB,V/2)
                utime.sleep_ms(1000)
                
        else:
            Off()
            print("Grüner Punkt - L")
#             OnFwd(MOT_A,-V)
#             OnFwd(MOT_B,V)
#             utime.sleep_ms(2000)
            if dose.TestenUndFahrenColor(V/2,V/2,500,LINKS): # -> schwarze Linie
                OnFwd(MOT_AB,V/2)
                utime.sleep_ms(1200)
                OnGyro(90, V)
                OnFwd(MOT_AB,V/2)      
                utime.sleep_ms(1000)
        SetLED(0xff, 0 , 0)
    elif color.on_green(RECHTS):
        #Off()
        SetLED(0,LED3_GREEN,0)
#        OnFwd(MOT_A,V)
#        OnFwd(MOT_B,-V)
#        utime.sleep_ms(2000)
        OnFwd(MOT_AB,V/2)
        for i in range(200):
            for s in sensoren:
                s.messen()
            color.update()
            #utime.sleep_ms(10)
        if color.on_green(LINKS): # L+R => Beide Seiten; 180-Grad-Drehung
            Off()
            SetLED(0,LED1_GREEN,0)
            print("Grüner Punkt - LR")
            
            if dose.TestenUndFahrenColor(V/2,V/2,500): # -> schwarze Linie
                OnFwd(MOT_AB,V/2)
                utime.sleep_ms(1200)
                OnGyro(180, V)
                OnFwd(MOT_AB,V/2)
                utime.sleep_ms(1000)

        else:
            print("Grüner Punkt - R")
            if dose.TestenUndFahrenColor(V/2,V/2,500,RECHTS): # -> schwarze Linie
                OnFwd(MOT_AB,V/2)
                utime.sleep_ms(1400)
                OnGyro(-90, V)
                OnFwd(MOT_AB,V/2)
                utime.sleep_ms(1000)
        SetLED(0xff, 0 , 0)
    
    if taster.getTotalValue()[2] > 0: # Einer der beiden taster gedrueckt                   
        print("Dose")
        dose.run()
        print("Main")
    
    #GruenR = color.on_green(RECHTS)
    #GruenL = color.on_green(LINKS)
        
    
#     SilberLED.on()
#     utime.sleep_us(40)
#     #print(SilberSensor.read-_u16())
#     if SilberSensor.read_u16() < 3000:
#         Off()
#         print("Silberlinie")
#         SetLED(0xff,0,LED2_GREEN)
#         break
#     SilberLED.off()

