import network
import time 
from umqtt.simple import MQTTClient 

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

mqtt_client_id = ''
mqtt_broker = 'broker.mqttdashboard.com'
mqtt_topic = ''

def msg_receiver(topic, message):
    print("Incomming Msg", message)

mqtt_subscriber = MQTTClient(mqtt_client_id, mqtt_broker)
mqtt_subscriber.set_callback(msg_receiver)

mqtt_subscriber.connect()

mqtt_subscriber.subscribe(mqtt_topic)

while True:
    mqtt_subscriber.check_msg()
    print("Receiving..")
    time.sleep(.5)