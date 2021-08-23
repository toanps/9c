import win32gui
import pyautogui
pyautogui.FAILSAFE= True
import time
import sys



def send_click(point):
    hwnd = win32gui.FindWindow(None, "9c")
    win32gui.SetForegroundWindow(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    pyautogui.moveTo(left + point[0], top + point[1])

    time.sleep(0.5)

    pyautogui.click()
    print("Clicked")

clear=[163,196]

try:
    while True:
        send_click(clear)
        time.sleep(10)
        send_click(clear)
        time.sleep(280)
except KeyboardInterrupt:
    sys.exit()