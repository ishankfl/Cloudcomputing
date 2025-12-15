import network
from umqtt.simple import MQTTClient
import time 
from machine import Pin

#define LED
led_pin = Pin(5, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')

# wifi.isconnected() = False, not False = True, while True:
while not wifi.isconnected():
    print("Connecting..")
print("Connected to wifi")

MQTT_CLIENT_ID = 'mqtt-client-sulav-123'
MQTT_BROKER = 'broker.mqttdashboard.com'
MQTT_TOPIC = 'mqtt-topic-randomnamevalue'

def received_msg(topic, msg):
    print("Msg", msg)
    decoded_msg = msg.decode()
    if decoded_msg == 'ON':
        led_pin.value(1)
    if decoded_msg == 'OFF':
        led_pin.value(0)

mqtt_subscriber = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)# client_id, server-url
mqtt_subscriber.set_callback(received_msg)

mqtt_subscriber.connect()
mqtt_subscriber.subscribe(MQTT_TOPIC)

while True:
    mqtt_subscriber.check_msg()
    time.sleep(.5)
    print('Running..')