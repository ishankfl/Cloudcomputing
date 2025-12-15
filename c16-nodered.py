import network
from umqtt.simple import MQTTClient
import time
from machine import Pin

led_pin = Pin(5, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')

while not wifi.isconnected():
    print('Connecting..')

print("Successfully connected to wifi")

MQTT_CLIENT_ID = 'ishan-client'
MQTT_SERVER = 'broker.mqttdashboard.com'
MQTT_TOPIC = 'ishan-topic-123'

def msg_received(topic, msg):
    print("Message comming from nodered: ", msg)
    msg_in_string = msg.decode()
    if msg_in_string == 'ON':
        led_pin.value(1)
    
    if msg_in_string == 'OFF':
        led_pin.value(0)

mqtt_subscriber = MQTTClient(MQTT_CLIENT_ID,MQTT_SERVER)
mqtt_subscriber.set_callback(msg_received)

mqtt_subscriber.connect()

mqtt_subscriber.subscribe(MQTT_TOPIC)

while True:
    mqtt_subscriber.check_msg()
    print("Receiving.. data...")
    time.sleep(.5)

