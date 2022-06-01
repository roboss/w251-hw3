import paho.mqtt.client as mqtt
  

LOCAL_MQTT_HOST="10.43.52.146"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="test_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

#publish the message
local_mqttclient.publish(LOCAL_MQTT_TOPIC,"Hello MQTT...")

test_image = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x04\x08\x00\x00\x00\x00j\xb3\n\xe6\x00\x00\x00\x10IDAT\x08\x1dcx\xc3P\xc7p\x98\xe10\x00\x0b\xfe\x02\xf1)^ %\x00\x00\x00\x00IEND\xaeB`\x82'
local_mqttclient.publish(LOCAL_MQTT_TOPIC,"rohit")