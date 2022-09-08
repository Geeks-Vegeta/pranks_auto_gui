'''
This will take screenshots and create one folder on desktop 

'''


import os
import sys
import pyautogui

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
_dir = f"{desktop}\ss"
if os.path.exists(_dir):
    pass
else:
    os.mkdir(_dir)
    

for x in range(10):
    im1 = pyautogui.screenshot()
    im1.save(f'{_dir}/my_screenshot{x}.png')

