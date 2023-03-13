from sensor_Licht import *
import speicher

sensor_A = Sensor(LED_A, "Außen")
sensor_W = Sensor(LED_W, "Weiss")
sensor_R = Sensor(LED_R, "Rot")
sensor_G = Sensor(LED_G, "Gruen")
sensoren = [sensor_W,sensor_R,sensor_A,sensor_G]

def kalibrieren():
    for s in sensoren: #startet Kalibrierung
        s.kalibrierStart()
    for i in range (500): # Kalibrierung (x500)
        for s in sensoren:
            s.kalibrierRunde()
    speicher.SchreibeWerte([sensor_W,sensor_A,sensor_R,sensor_G])
    #Debug(1,sensor_W.miniL,sensor_W.maxiL,sensor_W.miniR,sensor_W.maxiR)





