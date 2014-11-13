# this is the main backend app running on the LEDjockey server.
# Date: 11/2/2014
# Author: Brian Aggrey

from LEDwiz import (LWZ_SBA,LWZ_PBA)
from flask import (Flask, render_template, request)

command = 'off'
options = {
	'on':[255,255,255,255,4],
	'off':[0,0,0,0,4],
	'red':[48,0,0,48,0,0,48,0,0,48,0,0,48,0,0,0,48,0,0,48,0,0,48,0,0,48,0,0,48,0,0,0],
	'green':[0,48,0,0,48,0,0,48,0,0,48,0,0,48,0,0,0,48,0,0,48,0,0,48,0,0,48,0,0,48,0,0],
	'blue':[0,0,48,0,0,48,0,0,48,0,0,48,0,0,48,0,0,0,48,0,0,48,0,0,48,0,0,48,0,0,48,0],
	'fuschia':[48,0,48,48,0,48,48,0,48,48,0,48,48,0,48,0,48,0,48,48,0,48,48,0,48,48,0,48,48,0,48,0],
	'yellow':[48,48,0,48,48,0,48,48,0,48,48,0,48,48,0,0,48,48,0,48,48,0,48,48,0,48,48,0,48,48,0,0]
}

aqua = [0,48,48,0,48,48,0,48,48,0,48,48,0,48,48,0,0,48,48,0,48,48,0,48,48,0,48,48,0,48,48,0]

def easy(command):
	input_string = options.get(command,aqua)


	if len(input_string) == 5:
		LWZ_SBA(input_string)
	else:
		LWZ_PBA(input_string)

easy(command)



