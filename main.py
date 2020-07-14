import pyautogui as gui
import time
import keyboard
import pydirectinput as di
import random

RUN = False
STOP = False

def toggleRun():
	global RUN
	RUN = not RUN

def stop():
	global STOP
	STOP = True

keyboard.add_hotkey('v', toggleRun)
keyboard.add_hotkey('x', stop)

while not STOP:
	if RUN:
		print("run " + str(random.random()), end="\r")
		im = gui.screenshot()

		im = im.crop([200, 508, 1720, 509])

		placesToClick = []

		for i in range(0, 1520, 10):
			colour = im.getpixel((i, 0))
			if 25 < colour[0] and colour[0] < 55 and 20 < colour[1] and colour[1] < 45 and 75 < colour[2] and colour[2] < 115: 
				placesToClick.append(i-760)


		if len(placesToClick) > 1:
			lastPos = placesToClick[-1]
			for i in range(len(placesToClick)-1, 0, -1):
				placesToClick[i] -= placesToClick[i-1]

			for pos in placesToClick:
				di.move(pos, None)
				di.click()
				# print(gui.position())

			di.move(-lastPos, None)
	time.sleep(0.1)