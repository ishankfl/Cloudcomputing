import network
import time 
from umqtt.simple import MQTTClient 
from machine import Pin
#setup pin
led_light = Pin(17, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST','')
print('Obtaining Ip Address ')
while True:
    if wifi.isconnected():
        break
    print('.', end=' ')
    time.sleep(.3)
print("Wifi connected successfully")

mqtt_client_id = 'ishan-client-12'
mqtt_broker = 'broker.mqttdashboard.com'
mqtt_topic = 'ishan-topic-12'

def msg_receiver(topic, message):
    print("Incomming Msg", message)
    message = message.decode()

    if message == 'ON':
        led_light.value(1)
    
    elif message == 'OFF':
        led_light.value(0)


mqtt_subscriber = MQTTClient(mqtt_client_id, mqtt_broker)
mqtt_subscriber.set_callback(msg_receiver)

mqtt_subscriber.connect()

mqtt_subscriber.subscribe(mqtt_topic)

while True:
    mqtt_subscriber.check_msg()
    print("Receiving..")
    time.sleep(.5)