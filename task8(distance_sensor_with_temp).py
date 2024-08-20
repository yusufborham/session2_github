from matplotlib import pyplot as plt
from matplotlib import animation
from gpiozero import DistanceSensor
import numpy as np
import Adafruit_DHT
import time 
from datetime import datetime

def init():
    return temp,dis  
######################################################################
def animate(i):
    h,t = Adafruit_DHT.read_retry(sensor,pin)           #read temp 
    distance = sensor.distance()                        #read distance 

    y1=t                                
    old_y1 =temp.get_ydata()             
    new_y1 =np.r_[old_y1[1:],y1]
    temp.set_ydata(new_y1)                              #add new data to temp line

    y2=distance
    old_y2 =dis.get_ydata()             
    new_y2 =np.r_[old_y2[1:],y2]
    dis.set_ydata(new_y2)                               #add new data to distance line

    return temp,dis
########################################################################
sensor = Adafruit_DHT.DHT11
pin = 20
########################################################################
sensor = DistanceSensor(echo=18, trigger=17)

distance = sensor.distance()
########################################################################

h,t = Adafruit_DHT.read_retry(sensor,pin)
########################################################################

file = open("logFile.log",'a')                          #open file 
## prepare line to save on the file 
data = str(datetime.now()) + " -> " + str(distance) + "meters " + "temp is " + str(t) + "c \n"
file.writelines(data)
#########################################################################

fig = plt.figure()

ax = plt.axes(xlim=(0,30),ylim=(15,45))

temp, = ax.plot(np.arange(30),np.ones(30,dtype=float),lw=1,c='blue',marker='d',ms=2)
dis, = ax.plot(np.arange(30),np.ones(30,dtype=float),lw=1,c='red',marker='d',ms=2)

anim = animation.FuncAnimation(fig,animate,init_func=init, frames=30 , interval=100, blit =False)
 
