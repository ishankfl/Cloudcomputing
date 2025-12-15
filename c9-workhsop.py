import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')


# wifi.isconnected() = False, not False = True, while True:
while not wifi.isconnected():
    print("Connecting..")

print("Connected to wifi")