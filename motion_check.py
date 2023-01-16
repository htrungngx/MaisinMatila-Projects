from machine import Pin
import time

PIR1 = Pin('PC3', Pin.IN)  #Initial Motion Sensor


def motion_detected(): #Motion Function
    if PIR1.value():
        print("Motion Detected")
        return True
    else:
        print("No motion")
        return False
    time.sleep(1)


while True:
    motion_detected()
    time.sleep(2) #Detect in 2 seconds
