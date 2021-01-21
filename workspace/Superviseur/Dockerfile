FROM python:3.7-alpine

RUN apk update
RUN apk upgrade
RUN apk add mosquitto
RUN apk add mosquitto-clients
RUN pip install paho-mqtt
RUN pip install mysql-connector-python


WORKDIR Superviseur

