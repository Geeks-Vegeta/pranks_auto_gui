'''
make computer shutdown 
while asking in prompt 

'''

import os
import pyautogui
import time


def main():
    time.sleep(2)
    asking=pyautogui.confirm('Do you want to continue ?')
    if asking=="OK":
        os.system("shutdown /s /t 1")
    else:
        os.system("shutdown /s /t 1")



if __name__=="__main__":
    main()

