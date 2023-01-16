
#This main file will compile everything together and make Arduino run independance without IDE
#from connect_wifi import connectWifi #Import Wifi function
from send_file import send_my_photo #Import Sendfile function
#from capture import captureImage #import Capturing image function
from motion_check import motion_detected #Import motion detect function
import gate #Import gate function
from time import sleep


"""while True:
    connectWifi() #Initial Wifi
    sleep(1) #wait 1 second after starting Wifi function
    if motion_detected(): #Turn on Motion sensor function, if it detected
        sleep(5) #Wait 5 seconds to make sure motion detect right
        captureImage() #Taking picture
        sleep(3) #Wait 3 seconds to process picture
        #response = send_my_photo("latest.bmp") #Send picture to storage
        sleep(4)
        print(str(response.text)) #Send notification if picture saved successfully or re-take
        #if response.text == 'true': #If plate same as database, return "True"
        #    print('open') #Print opening notificaiton
        #    gate.openUp() #Open gate by rotating motor
        #    sleep(5)
        #    gate.closeDown() #Closing after opening
        #else:
        #   print('Do not open')"""


while True:
    print("Starting")
    if motion_detected():
        sleep(5)
        gate.openUp()
        sleep(5)
        gate.closeDown()
    else:
        print('Do not open')
