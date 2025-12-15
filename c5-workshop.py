import network
import time
from umqtt.simple import MQTTClient
from machine import Pin

#setup pin
led_pin = Pin(5, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')

print("Obtaining IP Address")
while not wifi.isconnected():
    print('.')
    time.sleep(.3)

if wifi.isconnected():
    print("wifi connected successfully")

mqtt_cleint_id = 'ishan-something'
mqtt_broker = 'broker.mqttdashboard.com'
mqtt_topic = 'ishan-topic'

def msg_receiver(topic, incomming_msg):
    print('Msg received', incomming_msg)

    decoded_msg = incomming_msg.decode()

    if decoded_msg == 'ON':
        led_pin.value(1)
    
    if decoded_msg == 'OFF':
        led_pin.value(0)


mqtt_subscriber = MQTTClient(mqtt_cleint_id, mqtt_broker)
mqtt_subscriber.set_callback(msg_receiver)

mqtt_subscriber.connect()

#setup topic
mqtt_subscriber.subscribe(mqtt_topic)

while True:
    mqtt_subscriber.check_msg()
    time.sleep(.3)
    print("Receiving..")