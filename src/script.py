from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

counter = 0
grandma = False
time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def keyInput(char):
    pyautogui.keyDown(char)
    time.sleep(0.1)
    pyautogui.keyUp(char)

def mainCookie():
    for i in range(36):
        i += 1
        click(289, 418)
        if keyboard.is_pressed('q'):
            i = 36
        if i == 35:
            i = 0
            clickGrandma()
            if grandma == False:
                i = 36

# LEARNING
def clickGrandma():
    if pyautogui.pixel(1820, 448)[2] == 121:
        grandma == True
        click(1821, 448)
        time.sleep(0.1)
        mainCookie()
    elif pyautogui.pixel(1820, 448)[2] != 121:
        grandma == False
        
mainCookie()