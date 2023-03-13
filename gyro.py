from meinePins import *
import mpu6050
import math
import utime
class RotSensor:
    def __init__(self):     
        self.mpu = mpu6050.MPU6050()
        self.mpu.setSampleRate(200)
        self.mpu.setGResolution(2) 
        self.gxoffset = 0#.07
        self.gyoffset = 0
        self.gzoffset=0
        self.filterLaenge = 5
        self.summex=0
        self.summey=0
        self.summez=0
        self.acc_x=0
        self.acc_y=0
        self.acc_z=0
        self.lastMess = 0
        self.start = 0
        
    def init(self):
        self.summex = 0
        self.start = 0
    
    def messeOffset(self):
        gx=0
        gy=0
        gz=0
        for i in range(100):
            g =  self.mpu.readData()
            utime.sleep_ms(5)
            gx += g.Gyroz
        #    gy += g.Gy
        #    gz += g.Gz
            
        self.gxoffset=gx/100
        #self.gyoffset=gy/1000
        #self.gzoffset=gz/1000
            
    def messeRot(self):
        t = utime.ticks_us()
        if self.start == 1:
           g  = self.mpu.readData()
           gx = g.Gyroz - self.gxoffset
           diff = t - self.lastMess
           self.summex = self.summex + (diff*gx)/1000000
        self.lastMess = t
        self.start = 1
            
    def messeNeigung(self):
        g =  self.mpu.readXYZData()
        gx = g.Gx - self.gxoffset
        gy = g.Gy - self.gyoffset       
        gz = g.Gz - self.gzoffset
        
        if gx <-0.99: gx =- 0.99
        if gx > 0.99: gx = 0.99
        if gy <-0.99: gy = -0.99
        if gy > 0.99: gy = 0.99
        if gz <-0.99: gz = -0.99
        if gz > 0.99: gz = 0.99
        gx =  int(180 / math.pi * math.asin(gx))
        gy =  int(180 / math.pi * math.asin(gy))
        gz =  int(180 / math.pi * math.asin(gz))
        self.summex-=self.acc_x
        self.summey-=self.acc_y
        self.summez-=self.acc_z
        self.summex+=gx
        self.summey+=gy
        self.summez+=gz
        self.acc_x=self.summex//self.filterLaenge
        self.acc_y=self.summey//self.filterLaenge
        self.acc_z=self.summez//self.filterLaenge
        
