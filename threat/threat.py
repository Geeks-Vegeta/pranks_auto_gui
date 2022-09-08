'''
This will open paint and write an threatning message 

'''


threat='''

“You think I'm playing at some game? You think iron will keep you safe? Hear my words, manling. Do not mistake me for my mask. You see light dappling on the water and forget the deep, cold dark beneath. Listen. You cannot hurt me. You cannot run or hide. In this I will not be defied.

I swear by all the salt in me: if you run counter to my desire, the remainder of your brief mortal span will be an orchestra of misery.

I swear by stone and oak and elm: I'll make a game of you. I'll follow you unseen and smother any spark of joy you find. You'll never know a woman's touch, a breath of rest, a moment's peace of mind.
'''

import pyautogui
import subprocess
import time

def main():
    subprocess.Popen(["notepad"],shell = True)
    pyautogui.press('enter')
    pyautogui.write(threat, interval=0.25)


if __name__=="__main__":
    main()


