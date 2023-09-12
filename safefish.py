""""
Safe Fisher -
Copyright (C) 2023 JSmo - All Rights Reserved.
You may use, distribute and modify this code.  You may not resell or profit from it.
"""

import pyautogui
import time
import random
import win32api
import win32con
from mousekey import MouseKey  # https://pypi.org/project/mousekey/

# SET THESE THINGS BEFORE YOU RUN THE SCRIPT
CATCH_COUNT = 96  # Sell after you catch how many fish?  Backpack size minus slots used with equipment
FISHING_DELAY = .25  # .25 for main, .41 for perfect balance and total noob - Lower is faster
FISHING_RANDOM = .2  # Random delay to add to casts to make less bannable, .2 or .1 for mains .05 for total noob.
FISHING_POLE_SLOT = '1'  # What slot is fishing pole in?  Make sure it has quotes around it.  EX: "1" or "2"
TIME_FOR_BUBBLES = 4  # Max time to wait after casting to detect bubbles.  Noobs might need 5 or 6
SELL_ANYWHERE = True  # If you purchased sell anywhere.  Otherwise the script will exit.

OPEN_CHESTS = False  # If you want to use this script to open chests only.  You'll need to set the coords below
OPEN_CHEST_X = 922  # Use Mpos to get coords of the bottom of the white E box you need to press.  MUST BE WHITE
OPEN_CHEST_Y = 511  # Same ^

# Script setup Mousekey
mkey = MouseKey()
# Kills the whole process, does always work (even with pure except)
mkey.enable_failsafekill('ctrl+c')


# Function for human like mouse clicking
def mclick(x, y):
	try:
		mkey.left_click_xy_natural(
			x, y,
			delay=.2,  # duration of the mouse click (down - up)
			# min_variation=-3,  # a random value will be added to each pixel  - define the minimum here
			max_variation=3,  # a random value will be added to each pixel  - define the maximum here
			use_every=4,  # use every nth pixel
			sleeptime=(0.005, 0.009),  # delay between each coordinate
			print_coords=False,  # console output
			percent=190,  # the lower, the straighter the mouse movement
			)
	except:
		win32api.SetCursorPos((x, y))
		time.sleep(random.uniform(0.001, 0.1))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
		time.sleep(random.uniform(0.001, 0.1))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Function for human like mouse movement
def mmove(x, y):
	try:
		mkey.move_to_natural(
			x, y,
			# min_variation=-3,  # a random value will be added to each pixel  - define the minimum here
			max_variation=3,  # a random value will be added to each pixel  - define the maximum here
			use_every=4,  # use every nth pixel
			sleeptime=(0.005, 0.009),  # delay between each coordinate
			print_coords=True,  # console output
			percent=90,  # the lower, the straighter the mouse movement
			)
	except:
		win32api.SetCursorPos((x, y))


# Function to check for air bubbles on the screen
def check_air_bubbles():
	s = pyautogui.screenshot()
	for x in range(770, 1160):
		for y in range(350, 730):
			colorcode = (68, 252, 234)  # Blue bubbles
			tempvar = False
			for x2 in range(5):
				if s.getpixel((x + x2, y)) == colorcode:
					tempvar = True
				else:
					tempvar = False
					break
			if tempvar is True:
				return True


# Function to wait for air bubbles on the screen
def wait_for_air_bubbles(timeout):
	"""Waits for air bubbles"""
	now = time.time()
	while time.time() - now < timeout:
		if check_air_bubbles():
			return True
	return False


# Function to wait for a color at a coordinate
def wait_for_color(x, y, color, timeout):
	now = time.time()
	while time.time() - now < timeout:
		if pyautogui.pixelMatchesColor(x, y, color):
			time.sleep(.25)
			return True
	return False


# Waits for fish to get on the line
def wait_for_fish_on(timeout):
	"""Waits for fishing bar up"""
	now = time.time()
	while time.time() - now < timeout:
		if fish_on():
			return


# Checks if fish on the line
def fish_on():
	"""Detects if the fishing bar is up"""
	# 821*806 location and color (53fa53  or RGB 83, 250, 83)
	if pyautogui.pixelMatchesColor(810, 810, (251, 98, 76)):
		return True
	else:
		return False


# Function to simulate a random cast single click
def click_random_cast():
	x, y = random.randint(960, 970), random.randint(520, 530)
	mclick(x, y)


# Function to simulate a double random cast click
def double_click_random_cast():
	click_random_cast()
	time.sleep(random.uniform(0.02, 0.025))
	click_random_cast()


# Function to reel in the fish
def reel(fish_count):
	x, y = random.randint(960, 970), random.randint(520, 530)
	mmove(x, y)
	wait_for_fish_on(5)
	while fish_on():
		mclick(x, y)
		time.sleep(random.uniform(FISHING_DELAY, FISHING_DELAY + FISHING_RANDOM))
	fish_count += 1
	print('Fish caught: ' + str(fish_counter))
	return fish_count


# Function to check if fishing pole is selected and select if not
def is_pole_selected():
	# If fishing pole is not selected, select it
	if not pyautogui.pixelMatchesColor(688, 935, (0, 213, 255)):
		mkey.force_activate_window(10290540)
		mkey.press_key(FISHING_POLE_SLOT, delay=.05)  # delay in seconds


# Function to check the fish count
def check_fish_count(fish_count):
	sold = False
	if fish_count == CATCH_COUNT or pyautogui.pixel(826, 694) == (253, 0, 97):
		if SELL_ANYWHERE:
			print('Inventory full, selling...')
			sell_fish()
		else:
			print('Inventory full, exiting program')
			exit()
		fish_count = 0
		sold = True

	return fish_count, sold


# Function to sell fish or exit program
def sell_fish():
	# Stop fishing by clicking fishing pole
	time.sleep(1)
	mkey.force_activate_window(10290540)
	mkey.press_key(FISHING_POLE_SLOT, delay=.05)  # delay in seconds
	time.sleep(random.uniform(.25, .5))

	# Click backpack
	mclick(random.randint(1180, 1230), random.randint(936, 997))
	# Wait for green sell box
	wait_for_color(1100, 350, (84, 234, 52), 2)

	# Make sure backpack is selected
	if not pyautogui.pixelMatchesColor(698, 346, (0, 213, 255)):
		mclick(698, 346)

	#  If there are fish in backpack, sell
	if pyautogui.pixel(579, 495) != (249, 248, 248):
		# click sell button
		x, y = random.randint(1037, 1097), random.randint(335, 375)
		mclick(x, y)
		wait_for_color(1193, 444, (84, 234, 52), 2)

		# click sell all
		x, y = random.randint(1174, 1320), random.randint(416, 452)
		mclick(x, y)
		wait_for_color(1122, 444, (84, 234, 52), 2)

		# click final sell button
		x, y = random.randint(1140, 1155), random.randint(430, 440)
		mclick(x, y)
		wait_for_color(1122, 444, (255, 255, 255), 2)

	# Close backpack
	x, y = random.randint(1397, 1400), random.randint(363, 366)
	mclick(x, y)

	# If fishing pole is not selected, select it
	is_pole_selected()

	time.sleep(random.uniform(.25, .5))
	# Cast
	mclick(960, 520)


# Main loop for opening chests, must get pixel of the E button bottom border in white and store in global variable
# OPEN_CHEST_X and OPEN_CHEST_Y
if OPEN_CHESTS:
	# Quick and dirty open chests.
	while True:
		if pyautogui.pixelMatchesColor(OPEN_CHEST_X, OPEN_CHEST_Y, (255, 255, 255)):
			# Hold E
			mkey.force_activate_window(10290540)
			mkey.press_key('e', delay=2)  # delay in seconds
			# Click buy
			mclick(697, 831)
		time.sleep(.25)


# Main loop to fish after checking that fishing pole is selected
is_pole_selected()
fish_counter = 0
while True:
	# Cast
	double_click_random_cast()

	# Check for full inventory or fish sell needed
	fish_counter, reset = check_fish_count(fish_counter)
	if reset:
		continue

	# Wait for bubbles
	if wait_for_air_bubbles(TIME_FOR_BUBBLES):
		# Hook then reel in the fish
		click_random_cast()
		fish_counter = reel(fish_counter)
