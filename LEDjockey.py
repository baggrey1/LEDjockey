# this is the main backend app running on the LEDjockey server.
# Date: 11/2/2014
# Author: Brian Aggrey

from LEDwiz import (LWZ_SBA,LWZ_PBA)
from flask import (Flask, render_template, request)

# define globals
options = {
	'command=on':['lights on!',255,255,255,255,4],
	'command=off':['lights off!',0,0,0,0,4],
	'command=red':['danger zone!',48,0,0,48,0,0,48,0,0,48,0,0,48,0,0,0,48,0,0,48,0,0,48,0,0,48,0,0,48,0,0,0],
	'command=green':['green means go!',0,48,0,0,48,0,0,48,0,0,48,0,0,48,0,0,0,48,0,0,48,0,0,48,0,0,48,0,0,48,0,0],
	'command=blue':['true blue!',0,0,48,0,0,48,0,0,48,0,0,48,0,0,48,0,0,0,48,0,0,48,0,0,48,0,0,48,0,0,48,0],
	'command=fuschia':['you girly man!',48,0,48,48,0,48,48,0,48,48,0,48,48,0,48,0,48,0,48,48,0,48,48,0,48,48,0,48,48,0,48,0],
	'command=yellow':['yeller!',48,48,0,48,48,0,48,48,0,48,48,0,48,48,0,0,48,48,0,48,48,0,48,48,0,48,48,0,48,48,0,0]
}
aqua = ['get that crap outta yer mouf!',0,48,48,0,48,48,0,48,48,0,48,48,0,48,48,0,0,48,48,0,48,48,0,48,48,0,48,48,0,48,48,0]

app = Flask(__name__)

@app.route("/easy/")
# This route accepts a string from GET request and changes lights based on options dict 
def easy():
	command = request.query_string
	input_string = options.get(command,aqua)

	if len(input_string) == 6:
		LWZ_SBA(input_string[1:])
	else:
		LWZ_PBA(input_string[1:])

	return input_string[0], 200

if __name__ == "__main__":
	app.run(debug=True)