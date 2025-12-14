import network 
import time
from umqtt.simple import MQTTClient 
from machine import Pin

led_pin = Pin(4, Pin.OUT) #setup led pin

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
    decode_msg = msg.decode()
    if decode_msg == 'ON':
        led_pin.value(1)
        
    if decode_msg == 'OFF':
        led_pin.value(0)

mqtt_subscriber = MQTTClient(MQTT_CLIENT_ID, MQTT_SERVER)
mqtt_subscriber.set_callback(msg_received)
mqtt_subscriber.connect()

mqtt_subscriber.subscribe(MQTT_TOPIC)

print("Mqtt connected successfully")

while True:
    mqtt_subscriber.check_msg()
    time.sleep(.5)
    print('.')