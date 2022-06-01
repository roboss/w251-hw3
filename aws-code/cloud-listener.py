import paho.mqtt.client as mqtt
import numpy as np
import cv2
from PIL import Image
import boto3

LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="mytopic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    print("message received: ",str(msg))
    payload = msg.payload
    print(payload)
    try:
        np_arr = np.fromstring(payload, np.uint8)
        print(type(np_arr))
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        print(type(img))
        im = Image.fromarray(img)
        print(type(im))
        width, height = im.size
        print(width, height)
        aws_access_key_id = "TEST_KEY"
        aws_secret_access_key = "SECRET_KEY"
        session = boto3.Session(aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
        s3 = session.resource("s3")
        txt =  b'etgertherThis is the content of the file uploaded from python boto3 asdfasdf'
        #BUCKET = 'firstbuckettestrohit'
        randint = np.random.randint(100000)
        file_name = str(randint) + "file_name.png"
        res_object = s3.Object('firstbuckettestrohit', file_name)
        result = res_object.put(Body=payload)
        res = result.get("ResponseMetadata")
        print(res.get("HTTPStatusCode"))

        #img_file_name = randint + "img.png"
        #s3.put_object(Filename=img_file_name,Body=payload, Bucket=BUCKET,Key=img_file_name)
    except Exception:
        pass
       
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()
