import dose #doseUmfahren und testenUndFahren-modul
import speicher #speicher-modul
from allSensors import *
from motor import *

V = 42

speicher.LadeWerte([sensor_W,sensor_A,sensor_R,sensor_G])
print(dose.TestenUndFahrenColor(V,V,2000))
Off()