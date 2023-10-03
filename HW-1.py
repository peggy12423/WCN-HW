import random
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

channel = []

def first():
    
    device_1 = []
    device_2 = []
    channel_ID = []
    channel_collision_probability = []
    channel_collision = [0]*79
    for i in range(48000):
        a=random.randint(1,79)
        b=random.randint(1,79)
        device_1.append(a)    #第(i+1)hop時，device 1所在的channel ID加入陣列
        device_2.append(b)    #第(i+1)hop時，device 2所在的channel ID加入陣列
        if(a == b):
#            print(a,b)
            channel_collision[a-1] += 1    #第i channel的碰撞次數
                
    for i in range(79):
        print("Channel " , i+1 , "碰撞次數:" , channel_collision[i] )
        print("Probability:" , channel_collision[i]/48000 , "\n")
        channel_ID.append(i+1)
        channel_collision_probability.append(channel_collision[i]/48000)
    
    plt.plot(channel_ID , channel_collision_probability)
    plt.xlabel("Channel ID")
    plt.ylabel("Channel collision propobility")
    plt.savefig('2 device.png', dpi=300, bbox_inches='tight')
    plt.show()
    
first()
