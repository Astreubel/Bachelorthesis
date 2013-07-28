#!/usr/bin/python

import RPi.GPIO as io
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
from ola.ClientWrapper import ClientWrapper
from ola.OlaClient import Universe
from subprocess import *
import os

io.setmode(io.BCM)
io.setup(14,io.IN)

lcd = Adafruit_CharLCD()
lcd.begin(16,2)

display_time = 3

#command to get ip address in the right format
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

def Universes(state, universes):
	if universes:
		for uni in universes:
			lcd.message("Universum %s\nName: %s" %(uni.id, uni.name))
			sleep(display_time)
			lcd.clear()
	else: 
		lcd.message(" kein In/Output\n   definiert")
		sleep(display_time)
	wrapper.Stop()
    
lcd.message("   OLA wird \n   gestartet")
sleep(5)
lcd.clear()

ipaddr = run_cmd(cmd)
lcd.message('  IP-Adresse: \n%s' % ( ipaddr ) )
sleep(10)
lcd.clear()
  
while 1:	
	lcd.clear()
	wrapper = ClientWrapper()
	client = wrapper.Client()
	client.FetchUniverses(Universes)
	wrapper.Run()
	if(io.input(14)):
		os.system("sudo shutdown -h now")
		lcd.clear()
		lcd.message("System wird \nheruntergefahren")
		sleep(display_time)
		lcd.clear()
		break
	sleep(0.1)
