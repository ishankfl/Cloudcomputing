import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')

while not wifi.isconnected():
    print('Connecting..')

print("Successfully connected to wifi")