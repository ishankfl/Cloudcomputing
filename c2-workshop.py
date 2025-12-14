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
MQTT_TOPIC = 'yourname-topic-something-1'

def received_msg(topic, msg):
    print("Topic", topic)
    print("Msg", msg)

#connection to mqtt
mqtt_subscriber = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
mqtt_subscriber.set_callback(received_msg)
mqtt_subscriber.connect()
mqtt_subscriber.subscribe(MQTT_TOPIC)

while True:
    mqtt_subscriber.check_msg()
    time.sleep(.3)
    print("Running...")


# i = 0
# while True:
#     data = {'number':i}
#     payload = ujson.dumps(data) # dictionary converted to json
#     mqtt_publisher.publish(MQTT_TOPIC, payload)
#     i+=1
#     print("sent data", payload)