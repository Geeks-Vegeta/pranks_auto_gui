'''
this is will tell user to shutdown 

'''


import pyautogui
import os
import time
import subprocess

def main():
    alert = pyautogui.alert('Do you want to continue ?')
    if alert=="OK":
        subprocess.Popen(["start", "cmd", "/k", "tree"], shell = True)
        time.sleep(3)
        pyautogui.write('cd ..', interval=0.25)
        pyautogui.press('enter')
        pyautogui.write('tree', interval=0.25)
        pyautogui.press('enter')


if __name__=="__main__":

    main() 
