import paho.mqtt.client as mqtt
import numpy as np
import cv2

test_image = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x04\x08\x00\x00\x00\x00j\xb3\n\xe6\x00\x00\x00\x10IDAT\x08\x1dcx\xc3P\xc7p\x98\xe10\x00\x0b\xfe\x02\xf1)^ %\x00\x00\x00\x00IEND\xaeB`\x82"
print(type(test_image))
nparr = np.fromstring(test_image, np.uint8)
print(type(nparr))
print(nparr)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
print(type(img))
print(img)
cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()