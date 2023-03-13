
from allSensors import *

class ColorSensor:
    def __init__(self):
        #self.on_white = 0
        self._on_green = [0,0]
        self._on_black = [0,0]
        
    def update(self):
        if sensor_G.wertL - sensor_R.wertL >= GRUENSCHWELLE and self._on_green[LINKS] < 7:
            self._on_green[LINKS] += 1
        elif self._on_green[LINKS] > 1 and sensor_G.wertL - sensor_R.wertL<GRUENSCHWELLE:
            self._on_green[LINKS] -= 1
        
        if sensor_G.wertR - sensor_R.wertR >= GRUENSCHWELLE and self._on_green[RECHTS] < 7:
            self._on_green[RECHTS] += 1
        elif self._on_green[RECHTS] > 1 and sensor_G.wertR - sensor_R.wertR < GRUENSCHWELLE:
            self._on_green[RECHTS] -= 1
            
        if sensor_A.wertR <= SCHWARZSCHWELLE and self._on_black[RECHTS] < 7:
            self._on_black[RECHTS] += 1
        elif self._on_black[RECHTS] > 1 and sensor_A.wertR > SCHWARZSCHWELLE:
            self._on_black[RECHTS] -= 1
            
        if sensor_A.wertL <= SCHWARZSCHWELLE and self._on_black[LINKS] < 7:
            self._on_black[LINKS] += 1
        elif self._on_black[LINKS] > 1 and sensor_A.wertL > SCHWARZSCHWELLE:
            self._on_black[LINKS] -= 2
            
    def on_green(self,dir):
        return self._on_green[dir] > 6
    
    def on_black(self,dir):
        return self._on_black[dir] > 6 and not self._on_green[dir] > 6
    
    def on_white(self,dir):
        return not self._on_black[dir] > 6 and not self._on_green[dir] > 6
    
color = ColorSensor()