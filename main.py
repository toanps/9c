# Requirements
# pip install opencv-python
# pip install pillow
# pip install pywin32
# pip install win32gui
# pip install pyautogui

# pyinstaller --onefile hello.py

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import win32gui
import time


import os
# from time import time
from windowcapture import WindowCapture

from findClicks import findClickPositions

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pyautogui
pyautogui.FAILSAFE= True

import sys
windowName = '9c'

def clickImage(windowName, imagePath):

    wincap = WindowCapture(windowName)
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # cv.imshow('Computer Vision', screenshot)

    points = findClickPositions(imagePath, "temp.png",
                                threshold=0.70, debug_mode='points')
    print(points)
    if len(points):
        wincap.send_click(points[0])

def send_click(point):
    hwnd = win32gui.FindWindow(None, "9c")
    win32gui.SetForegroundWindow(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    pyautogui.moveTo(left + point[0], top + point[1])

    time.sleep(0.5)

    pyautogui.click()
    print("Clicked")

clear=[143,196]
pinkBarFull = [904, 61]

def FindImage(windowName, imagePath):
    wincap = WindowCapture(windowName)
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    points = findClickPositions(imagePath, "temp.png",
                                threshold=0.70, debug_mode='points')
    print(points)
    return points

try:
    while True:

        if FindImage(windowName, "starBarEmpty.png"):
            clickImage(windowName, "pinkBarFull.png")
        # get an updated image of the game
        clickImage(windowName, "clear.png")
        send_click(clear)
        # cv.imshow('Computer Vision', screenshot)

        time.sleep(300)

except KeyboardInterrupt:
    sys.exit()

# initialize the WindowCapture class



print('Done.')
