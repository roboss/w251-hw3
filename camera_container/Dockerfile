FROM ubuntu
  
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt install -y python3-dev python3-pip  python3-opencv vim-tiny  libopencv-dev
RUN apt install -y mosquitto-clients
RUN apt install -y mosquitto
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install paho-mqtt

COPY cam.py cam.py
# COPY /home/rohit/v3/week03/hw/camera_container/haarcascade_frontalface_default.xml /usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml

CMD ["python3","cam.py"]