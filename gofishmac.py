""""
Safe Fisher -
Copyright (C) 2023 JSmo - All Rights Reserved.
You may use, distribute and modify this code.  You may not resell or profit from it.
"""

import pyautogui
import time
import random
#from mousekey import MouseKey  # https://pypi.org/project/mousekey/


class GoFish:
    """Fishing Simulator Bot for Roblox"""

    @classmethod
    def start(cls):
        # SET THESE THINGS BEFORE YOU RUN THE SCRIPT

        # If you just want to open chests set True
        OPEN_CHESTS = False  # To open chests only.  Try to get E over the back of your neck in game while at chest.

        #  For fishing set OPEN_CHESTS to False and set these parameters
        CATCH_COUNT = 90  # Sell after you catch how many fish?  Backpack size minus slots used with equipment
        FISHING_DELAY = .25  # .25 for main, .41 for perfect balance and total noob - Lower is faster
        FISHING_RANDOM = .2  # Random delay to add to casts to make less bannable, .2 or .1 for mains .05 for total noob.
        FISHING_POLE_SLOT = 1  # What slot is fishing pole in?
        TIME_FOR_BUBBLES = 12  # Max time to wait after casting to detect bubbles.  Noobs might need 5 or 6
        SELL_ANYWHERE = True  # If you purchased sell anywhere.  Otherwise the script will exit.

        #  Class Variables
        cls.total_fish = 0
        cls.fish_count = 0
        cls.start_time = time.time()

        # Script setup Mousekey
        # mkey = MouseKey()
        # # Kills the whole process
        # mkey.enable_failsafekill('ctrl+c')

        time.sleep(3)
        print('got past sleep')

        # Function for human like mouse clicking
        def pyclick(x, y):
            """Uses pyautogui to move and click mouse"""
            pyautogui.click(x, y)

        def mclick(x, y):
            try:
                pyautogui.click(x, y)
            except:
                pyautogui.click(x, y)

        # Function for human like mouse movement
        def mmove(x, y):
            duration = random.uniform(.5, 1)
            try:
                pyautogui.moveTo(x, y, duration=2, tween=pyautogui.easeInOutQuad)
            except:
                pyautogui.moveTo(x, y, duration=2, tween=pyautogui.easeInOutQuad)

        # Function to check for air bubbles on the screen
        def check_air_bubbles():
            print('start: {}'.format(time.time()))
            s = pyautogui.screenshot()
            print('stop: {}'.format(time.time()))
            color = (69, 252, 234)
            print('startloop: {}'.format(time.time()))
            for x in range(540, 1160, 5):
                for y in range(125, 540, 5):
                    if s.getpixel((x, y)) == color:
                        print('found air bubbles')
                        return True
            print('stop loop, NO air bubbles {}'.format(time.time()))
            return False

        # Function to wait for air bubbles on the screen
        def wait_for_air_bubbles(timeout):
            """Waits for air bubbles"""
            now = time.time()
            while time.time() - now < timeout:
                print('run air bubbles')
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
            s = pyautogui.screenshot()
            color = (83, 250, 83)  # Green Catch Bar
            # Step every 5 pixels to save time
            for x in range(699, 966, 5):
                for y in range(702, 780, 5):
                    if s.getpixel((x, y)) == color:
                        print('fishon')
                        return True
            # Return False at end of the loop
            return False

        # Function to simulate a random cast single click
        def click_random_cast():
            x, y = random.randint(830, 835), random.randint(490, 497)
            mclick(x, y)

        # Function to simulate a double random cast click
        def double_click_random_cast():
            click_random_cast()
            time.sleep(random.uniform(0.02, 0.025))
            click_random_cast()

        # Function to reel in the fish
        def reel():
            x, y = random.randint(830, 835), random.randint(490, 497)
            mmove(x, y)
            wait_for_fish_on(5)
            while fish_on():
                mclick(x, y)
                print('clicking')
                time.sleep(random.uniform(FISHING_DELAY, FISHING_DELAY + FISHING_RANDOM))
            cls.fish_count += 1
            cls.total_fish += 1
            print('Fish caught: {}/{}.  Total fish caught this session: {}.  Total session time: {}'.format(
                cls.fish_count, CATCH_COUNT, cls.total_fish,
                time.strftime("%Hh:%Mm:%Ss", time.gmtime(time.time()-cls.start_time))))

        # Function to check if fishing pole is selected and select if not
        def is_pole_selected():
            # If fishing pole is not selected, select it
            x1 = 600 + (85 * (FISHING_POLE_SLOT-1))
            if not pyautogui.pixelMatchesColor(x1, 875, (0, 213, 255)):
                x2, y2 = 693 + (85 * (FISHING_POLE_SLOT-1)), random.randint(964, 974)
                mclick(x2, y2)

        # Function to check the fish count
        def check_fish_count():
            if cls.fish_count == CATCH_COUNT or is_bag_full():
                if SELL_ANYWHERE:
                    print('Inventory full, selling...')
                    sell_fish()
                else:
                    print('Inventory full, exiting program')
                    exit()
                cls.fish_count = 0
                return True
            return False

        # Function to sell fish or exit program
        def sell_fish():
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

            time.sleep(random.uniform(.25, .5))
            # Cast
            mclick(960, 520)

        def is_bag_full():
            """Detects if the bag full message is up"""
            s = pyautogui.screenshot()
            color = (253, 0, 97)  # "Cannot Catch Fish Because Backpack is Full" message color
            # Step every 2 pixels to save time
            for x in range(570, 670, 2):
                for y in range(650, 750, 2):
                    if s.getpixel((x, y)) == color:
                        return True
            return False

        def chest_ready():
            color = (255, 255, 255)
            s = pyautogui.screenshot()
            for x in range(875, 1000, 5):
                for y in range(500, 700, 5):
                    if s.getpixel((x, y)) == color:
                        return True
            return False

        # Main loop for opening chests
        if OPEN_CHESTS:
            # Quick and dirty open chests.
            mclick(697, 831)
            while True:
                if chest_ready():
                    # Hold E
                    mkey.force_activate_window(10290540)
                    mkey.press_key('e', delay=2)  # delay in seconds
                    # Click buy
                    mclick(697, 831)
                    time.sleep(6)
                    if pyautogui.pixelMatchesColor(594, 314, (0, 213, 255)):
                        print('Ran out of money')
                        mclick(1442, 326)
                        exit()
                time.sleep(.25)

        # Main loop to fish after checking that fishing pole is selected
        mclick(720, 569)  # Click Window
        time.sleep(.5)
        is_pole_selected()
        while True:
            print('got to main loop, getting ready to cast')
            # Cast
            double_click_random_cast()
            print('casted')

            # Check for full inventory or sell fish if needed
            if check_fish_count():
                continue

            # Wait for bubbles
            if wait_for_air_bubbles(TIME_FOR_BUBBLES):
                # Hook then reel in the fish
                click_random_cast()
                fish_counter = reel()


if __name__ == '__main__':
    GoFish.start()
