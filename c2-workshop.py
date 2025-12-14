import network
import time
from umqtt.simple import MQTTClient
import ujson

# connection to wifi
wifi_connection = network.WLAN(network.STA_IF)
wifi_connection.active(True)
# wifi_connection.connect('ssid','pw')
wifi_connection.connect('Wokwi-GUEST','')

print("Connecting..")
while not wifi_connection.isconnected():
    print('.')
    time.sleep(.5)
print("Connected successfully")

MQTT_CLIENT_ID = 'yourname-clientid-123'
MQTT_BROKER = 'broker.mqttdashboard.com'
MQTT_TOPIC = 'yourname-topic-something'
#connection to mqtt
mqtt_publisher = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
mqtt_publisher.connect()

i = 0
while True:
    data = {'number':i}
    payload = ujson.dumps(data) # dictionary converted to json
    mqtt_publisher.publish(MQTT_TOPIC, payload)
    i+=1
    print("sent data", payload)