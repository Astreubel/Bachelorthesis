#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
from ola.ClientWrapper import ClientWrapper
from ola.OlaClient import Universe

lcd = Adafruit_CharLCD()
lcd.begin(16,2)

#command to get ip address in the right format
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

def Universes(state, universes):
  for uni in universes:
    lcd.message("Universe %s\nName:%s" %(uni.id, uni.name))
    wrapper.Stop()
    
lcd.message("OLA wird \ngestartet...")
sleep(10)

ipaddr = run_cmd(cmd)
lcd.message('IP: \n%s' % ( ipaddr ) )
sleep(10)
  
while 1:
	lcd.clear()
	wrapper = ClientWrapper()
	client = wrapper.Client()
	client.FetchUniverses(Universes)
	wrapper.Run()
	sleep(10)
