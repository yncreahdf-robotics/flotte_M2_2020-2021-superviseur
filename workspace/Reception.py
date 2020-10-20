
#!/usr/bin/env python

import time

import mqttperso

ip = "192.168.1.5"

mqttperso.subscribe(ip, 1883, "topiCoco", 2)


while (1):
	time.sleep(5)
	print("ok")
