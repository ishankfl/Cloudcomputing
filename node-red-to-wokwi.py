import network 

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')
print("Connecting.")
while not wifi.isconnected():
    print('.',end=' ')
print("Connected successfully")