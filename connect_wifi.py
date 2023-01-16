import network #Import library
sta_if = network.WLAN(network.STA_IF) 


def connectWifi():
    if sta_if.isconnected() == False: #If network is not connected
        sta_if.active(True) #Reactive Network
        sta_if.connect('AIoT-Garage', 'asdfghjk') #Enter SSID and Wifi Password 
        print('connection is established for the first time: ' + str(sta_if.isconnected())) #Print if wifi is connected
    else:
        print('Wifi already connected')








'''def connectWifi():
    sta_if = network.WLAN(network.STA_IF)
    print('WLAN interface is active: ' + str(sta_if.active()))
    print('Network settings: ' + str(sta_if.ifconfig()))

    # activate the station interface:
    sta_if.active(True)

    # Connect to Wifi
    sta_if.connect('AIoT-Garage', 'asdfghjk')
    print('connection is established: ' + str(sta_if.isconnected()))
    return'''
#connectWifi()
