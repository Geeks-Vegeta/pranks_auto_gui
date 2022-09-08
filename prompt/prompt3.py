'''
Asking password from prompt and opening multiple cmds
'''

import os
import time
import pyautogui
import subprocess


def main():
    password=pyautogui.password('Enter your chrome password')
    if password =="college":
        subprocess.Popen(["start", "cmd", "/k", "tree"], shell = True)
        time.sleep(3)
        pyautogui.write('cd ..', interval=0.25)
        pyautogui.press('enter')
        pyautogui.write('tree', interval=0.25)
        pyautogui.press('enter')
    else:
        for x in range(10):
            subprocess.Popen(["start", "cmd", "/k", "tree"], shell = True)
            time.sleep(1)


if __name__=="__main__":
    main()



