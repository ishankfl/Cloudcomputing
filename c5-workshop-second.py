import network
import time
from umqtt.simple import MQTTClient
from machine import Pin
import dht 
import ujson
#setup pin
led_pin = Pin(5, Pin.OUT)
sensor = dht.DHT22(Pin(4))

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

mqtt_publisher = MQTTClient(mqtt_cleint_id, mqtt_broker)
mqtt_publisher.connect()

while True:
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    print("Temp and Humidity: ", temp, humidity)
    data = {'temp':temp, 'humidity':humidity}
    payload = ujson.dumps(data)
    mqtt_publisher.publish(mqtt_topic, payload)
    print("Sent data", payload)
    time.sleep(.5)