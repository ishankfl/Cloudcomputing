import network
import time 

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')
print('Obtaining Ip Address ')
while True:
    if wifi.isconnected():
        break
    print('.', end=' ')
    time.sleep(.3)
print("Wifi connected successfully")