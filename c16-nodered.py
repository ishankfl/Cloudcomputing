import network
from umqtt.simple import MQTTClient

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

mqtt_subscriber = MQTTClient(MQTT_CLIENT_ID,MQTT_SERVER)
mqtt_subscriber.set_callback(msg_received)

mqtt_subscriber.connect()

mqtt_subscriber.subscribe(MQTT_TOPIC)

while True:
    mqtt_subscriber.check_msg()
    print("Receiving.. data...")
