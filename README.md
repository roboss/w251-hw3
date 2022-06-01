# w251-hw3
### 60 points for a containerized end to end appliation DONE

### 10 points for using a user defined network in the cloud (automatic if using k8s on the cloud side) DONE

### 10 points for using Kubernetes on your Jetson DONE

### 10 points for explaining the MQTT topics and the QoS that you used. DONE

I used two topics - one for the Jetson and then one for the AWS side from the Jetson. The "test-topic" from the Jetson got a published message of the face binary message and sent it to the listener via the broker. It also logged the message as standard output also. This message was then republished through a new topic "mytopic" which the AWS MQTT broker was subscribing to and capturing messages from. I used Quality of Service 0, which is the most minimal QoS service which is a best-effort guarantee that it will publish a message at most once. There is no ack and the message is not stored and retransmitted by the sender. The sender does not even know if the receiver on the cloud has received the message. This is opposed to QoS level 1 where this a guarantee of a message received at least once and QoS 2 - where the message is receieved exactly once. LINE OF CODE: remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  
### 10 points for storing your faces in publicly reachable object storage DONE

  NEED TO LOGIN WITH YOUR AWS ACCOUNT - could not find a way without login
  
  LINK: https://s3.console.aws.amazon.com/s3/buckets/firstbuckettestrohit
  
### 10 bonus points for using Kubernetes instead of Docker on the cloud side. DONE
