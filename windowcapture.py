
import win32gui, win32ui, win32con
import pyautogui, sys
import numpy as np
import cv2
from PIL import ImageGrab, Image
import time


class WindowCapture:

    # properties
    w = 0
    h = 0
    hwnd = None


    # constructor
    def __init__(self, window_name):
        # find the handle for the window we want to capture
        self.hwnd = win32gui.FindWindow(None, window_name)

        self.left, self.top, self.right, self.bot = win32gui.GetWindowRect(self.hwnd)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        else:
            self.left, self.top, self.right, self.bot = win32gui.GetWindowRect(self.hwnd)



        # self.left = 0
        # self.top= 0
        # self.right= 0
        # self.bot = 0
        #
        # self.w = 0
        # self.h = 0

        # window_rect = win32gui.GetWindowRect(self.hwnd)
        #
        # self.w = window_rect[2] - window_rect[0]
        # self.h = window_rect[3] - window_rect[1]

        # account for the window border and titlebar and cut them off
        # border_pixels = 0
        # titlebar_pixels = 0
        # self.w = self.w - (border_pixels * 2)
        # self.h = self.h - titlebar_pixels - border_pixels
        # self.cropped_x = border_pixels
        # self.cropped_y = titlebar_pixels

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        # self.offset_x = window_rect[0] + self.cropped_x
        # self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):


        win32gui.SetForegroundWindow(self.hwnd)
        time.sleep(0.5)
        # self.left, self.top, self.right, self.bot = win32gui.GetWindowRect(self.hwnd)

        img = ImageGrab.grab(bbox=(self.left, self.top, self.right, self.bot))  # x, y, w, h
        # img_np = np.array(img)
        # img= img_np
        # img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        img.save('temp.png')

        return img


    def list_window_names(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.

    def send_click(self,point):

        pyautogui.moveTo(self.left+point[0], self.top+point[1])

        win32gui.SetForegroundWindow(self.hwnd)
        pyautogui.click()
        print("Clicked")
