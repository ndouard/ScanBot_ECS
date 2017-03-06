from __future__ import print_function
'''
Handles instances
	Capture start/stop
	Turret high level commands
	Vehicle nav override

Handles processes
	Manual radio control capture using knob as turret orientation control and 3 pos 'mode' switch as +45, 0, -45 sensor horizontal angle command
	Autonomous scan: swipes room, handles start/stop automatically - possible to end capture manually

Core acts as a console program - leaves room for GUI implementation
'''

import sys
#handles low level turret actions
import turret
#start/stop capture - handles Minnowboard dialog
import capture


def get_user_command():
	print('Possible capture modes:')
	print('#1 - Manual')
	print('#2 - Autonomous')
	print('What will you choose? (1/2)')
	user_input = raw_input()
	#need to parse properly!
	selected_mode = int(user_input)
	return selected_mode

def manual():
	return
	
def autonomous():
	return




if __name__ == '__main__':
	selected_mode = get_user_command()
	selected_mode_name = str()
	if selected_mode == 1:
		selected_mode_name = 'Manual'
	else:
		selected_mode_name = 'Autonomous'
	print('Mode #' + str(selected_mode) + ' - ' + selected_mode_name + ' will be used.')

	if selected_mode == 1:
		manual()
	else:
		autonomous()


