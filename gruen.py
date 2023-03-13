from meinePins import *
from allSensors import *

  # nicht die Länge verändern!
blackLoop = [0,0]

    
    
def aufSchwarz(richtung):
    if richtung == LINKS:
        diff = sensor_A.wertL    
    else: 
        diff = sensor_A.wertR
        
    if diff <= SCHWARZSCHWELLE:
        if blackLoop[richtung] > 4:
            return True
        else:
            blackLoop[richtung] += 1
            return False
    else:
        blackLoop[richtung] = 0
        return False
