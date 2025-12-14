import network 
import time
from umqtt.simple import MQTTClient 

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')
print("Connecting.")
while not wifi.isconnected():
    print('.',end=' ')
    time.sleep(.4)
print("Connected successfully")

MQTT_CLIENT_ID = 'yourname-clientid-randomnumber'
MQTT_SERVER = 'broker.mqttdashboard.com'
MQTT_TOPIC = 'ishan-heloo123-led'

def msg_received(topic, msg):   #callback function
    print("MSG Received", msg)

mqtt_subscriber = MQTTClient(MQTT_CLIENT_ID, MQTT_SERVER)
mqtt_subscriber.set_callback(msg_received)
mqtt_subscriber.connect()

mqtt_subscriber.subscribe(MQTT_TOPIC)

print("Mqtt connected successfully")

while True:
    mqtt_subscriber.check_msg()
    time.sleep(.5)
    print('.')