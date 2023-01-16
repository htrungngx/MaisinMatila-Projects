import pyb
from machine import Pin
from time import sleep

IN1 = Pin('PA9', Pin.OUT) #High voltage #Initial high voltage pin
IN2 = Pin('PA10', Pin.OUT)  #Low voltage #Initial low voltage pin
ENA = Pin('PK1', Pin.OUT) #Initial speed pin

print(IN1)
print(IN2)
print(ENA)

def open(): #Motor rotate Left => Right
        print("Door is opening")
        IN1.high() #Rotate motor => Opening
        IN2.low()

def close(): #Motor rotates Right => Left
        print("Door is closing")
        IN1.low()
        IN2.high() #Closing

def stop(): #Turn off Motor
        IN1.low()
        IN2.low()


def openUp():
    while True:
        open()
        sleep(3)
        stop()
        break


def closeDown():
    while True:
        close()
        sleep(5)
        stop()

while True:
    openUp()
    closeDown()
