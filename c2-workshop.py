import network
import time
# connection to wifi
wifi_connection = network.WLAN(network.STA_IF)
wifi_connection.active(True)
# wifi_connection.connect('ssid','pw')
wifi_connection.connect('Wokwi-GUEST','')

print("Connecting..")
while not wifi_connection.isconnected():
    print('.')
    time.sleep(.5)
print("Connected successfully")