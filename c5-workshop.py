import network
import time

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')

print("Obtaining IP Address")
while not wifi.isconnected():
    print('.')
    time.sleep(.3)

if wifi.isconnected():
    print("wifi connected successfully")
