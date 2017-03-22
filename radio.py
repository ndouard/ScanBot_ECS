import configparser
import os
import os.path
import sys
import pathlib
import time
import threading
from ftplib import FTP
from nanpy import ArduinoApi
#retrieves knob PWM level using nanpy
def init():
	a = ArduinoApi()
	a.pinMode(6, a.INPUT)
	
def get_knob_level():
	#analogRead
	return 0

#retrieves 3 pos switch PWM level using nanpy
def get_3_pos_level():
	return 200

def get_2_pos_level():
	return 50

