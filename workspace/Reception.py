
#!/usr/bin/env python

import time

import FonctionsMQTT

ip = "192.168.1.5"

FonctionsMQTT.subscribe(ip, 1883, "topiCoco", 2)


while (1):
	time.sleep(5)
	print("ok")
