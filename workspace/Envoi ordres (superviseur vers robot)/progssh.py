#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
from subprocess import Popen, call, PIPE
import paramiko

def func_do_ssh_Stuff(address, usr, pwd, command):
        try:
            print("ssh " + usr + "@" + address + ", running : " +
                         command)
            client = paramiko.SSHClient()
            client.load_system_host_keys() # this loads any local ssh keys
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(address, username=usr, password=pwd)
            _, ss_stdout, ss_stderr = client.exec_command(command)

                    
	    r_out, r_err = ss_stdout.readlines(), ss_stderr.read()
   
	
        except IOError:
            print(".. host " + address + " is not up")
            return "host not up", "host not up"


if __name__ == '__main__':
	func_do_ssh_Stuff("192.168.1.103", "robotino", "robotino", "python heronReception.py")
