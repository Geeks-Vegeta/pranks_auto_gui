

'''
This is for continoulsy clicking the screen shorts of user and saving it to home page

'''

import pyautogui
import time

for x in range(10):
    im1 = pyautogui.screenshot()
    im1.save(f'my_screenshot{x}.png')
