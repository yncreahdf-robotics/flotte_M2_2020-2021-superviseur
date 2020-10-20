#!/usr/bin/env python3

import time

import mqttperso

ip = "192.168.1.5"

mqttperso.publish(ip, 1883, "topiCoco", "testmessage", 2)


while (1):
	time.sleep(5)
	print("ok")
