#see diagrams
#from nanpy import Servo
import time

#servo_rotation = Servo(10)
#servo_tilt = Servo(11)

def left90():
	#servo_tile.write()
	#servo_left.write()
	return

	
def right90():
	#servo_tile.write()
	#servo_left.write()
	return

def left180():
	#servo_tile.write()
	#servo_left.write()
	return

def right180():
	#servo_tile.write()
	#servo_left.write()
	return

def left():
	return

def right():
	return

def servo_demo():
	for move in [0, 90, 180, 90, 0]:
		servo_tilt.write(move)
		time.sleep(1)
	
	for move in [0, 90, 180, 90, 0]:
		servo_rotation.write(move)
		time.sleep(1)

def write_pwm_rot(pwm_input):
	#coef + write servo_demo
	return

def write_pwm_tilt(pwm_input):
	if pwm_input == 100:
		left()
	elif pwm_input == 200:
		right()
	else:
		print("Bad 3-pos PWM input - is the radio controller correctly configured?")

def home():
	#go to default pos
	return
