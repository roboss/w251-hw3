import numpy as np
import cv2
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="10.43.52.146"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="test_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))

face_cascade = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")
print(face_cascade)

# the index depends on your camera setup and which one is your USB camera.
# you may need to change to 1 depending on your local config
cap = cv2.VideoCapture(0)

face_imgs = []

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(type(frame))
    print(frame.size)
    print(frame.shape)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = frame

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(f"[INFO] Found {len(faces)} face(s).")

    if len(faces) > len(face_imgs):
        print("[INFO] New number of maximum faces detected!")
        #face_imgs = faces

    temp_faces = []

    for face in faces:
        (x,y,w,h) = face
        print((x,y,w,h))
        # your logic goes here; for instance
        # cut out face from the frame.. 
        crop_face = frame[y:y+h,x:x+w]
        print(crop_face.shape)
        temp_faces.append(crop_face)
        cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]

    face_imgs = temp_faces
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture

msgs = []

print("LOOP OVER")

print(len(face_imgs))

rgb_weights = [0.2989,0.5870,0.1140]

if len(face_imgs) > 5:
    face_imgs = face_imgs[:4]

res = []

for face in face_imgs:
    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    face = face[::2,::2]
    print(face)
    print(face.shape)
    res.append(face)

face_imgs = res

if len(face_imgs) > 0:

    local_mqttclient = mqtt.Client()
    local_mqttclient.on_connect = on_connect_local
    local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

    print(face_imgs)
    for idx, face in enumerate(face_imgs):
        rc,png = cv2.imencode('.png', face)
        msg = png.tobytes()
        msgs.append(msg)
        #print(msg)
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, f"Publishing face number {1 + idx}")
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, f"test")
        local_mqttclient.publish(LOCAL_MQTT_TOPIC,msg)

#print(msgs)

for face in face_imgs:
    print(type(face))
    print(face.shape)
    print(face.size)

print(f"Found {len(face_imgs)} faces")

print(len(msgs))

for msg in msgs:
    print(len(msg))

cap.release()
cv2.destroyAllWindows()