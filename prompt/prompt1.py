'''
this is will tell user to shutdown 

'''


import pyautogui
import os

def main():
    alert = pyautogui.alert('Do you want to continue ?')
    if alert=="OK":
        os.system("shutdown /s /t 1")


if __name__=="__main__":

    main() 
