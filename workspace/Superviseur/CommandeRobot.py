import sys
import paho.mqtt.client as mqtt

sys.path.append('/home/isen-lab-rob-1-pc/Desktop/flotte_M2_2020-2021-superviseur/workspace/Superviseur')
#print(sys.path)
import Positions

#	gets supervisor's IP using the host file
hosts = open('/etc/hosts','r')
for line in hosts:
	splitted_line=line.split()
	try:
		if splitted_line[1]=="supIP":
			ipsuperviseur = splitted_line[0]
	except IndexError:
		pass			

#	TCP port used for MQTT	
port = 1883

############
### Defs ###
############

def on_connect(client, userdata, flags, rc):

	print("Connected with result code "+str(rc))
	if rc==0:
		print("connection ok")
		#pass
	else:
		print("connection no")
		#pass

	
def on_disconnect(client, userdata, rc):

	print("Client Got Disconnected")


def on_message(client, userdata, msg):

	print("Yes! i receive the message :" , str(msg.payload))
	print("message received ", msg.payload.decode("utf-8"))
	print("message topic=",msg.topic)
	print("message qos=",msg.qos)
	print("message retain flag=",msg.retain)


	if msg.topic == "Initialisation/Type":

		print("ip du robot" + msg.payload.decode("utf-8").split("/")[0])
		print("type de robot" + msg.payload.decode("utf-8").split("/")[1])



#Appel d'une fonction qui permet de recevoir un message

def subscribe(ip, port, topic, qos):

	client = mqtt.Client()

	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.connect(ip,port,65535)
	client.subscribe(topic, qos)
	client.loop_start()
	print("subscribed to "+topic)


#Appel d'une fonction qui permet d'envoyer un message

def publish(ip, port, topic, message, qos):

	client = mqtt.Client()

	client.connect(ip,port,65535)
	client.loop_start()
	client.publish(topic, message, qos)
	print("message sent to "+topic)



# Verifier que les robots en marche sont toujours en marche
#def main():
print(ipsuperviseur)
publish(ipsuperviseur, port, "Commande/Envoi", "rien", 2)
print(ipsuperviseur)
#if __name__=="__main__":
#	main()