import time
import datetime
import cv2
import mss
import numpy
import pyautogui
import keyboard
import pyscreeze
from win32gui import FindWindow, GetWindowRect, GetForegroundWindow

Noxplayer = FindWindow(None, "NoxPlayer")
left, top, width, height  = GetWindowRect(Noxplayer)
print(left, top, width, height)

def keyboardS():
    for i in range(2):
        pyautogui.keyDown('s')
        pyautogui.keyUp('s')

def ClickMenuQuest(x1, y1):
    time.sleep(1)
    pyautogui.click(x = left + x1, y = top + y1, interval=0.5)
    return True

def nodelayClickMenuQuest(x1, y1):
    pyautogui.click(x = left + x1, y = top + y1, interval=0.5)
    return True

def py_locateOnscreen(name):
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('Image/' + name, region=(left, top, width - left, height - top), grayscale = True, confidence=.8)
    else:
        time.sleep(1)
        print(r.left, r.top, r.width, r.height)
        # pyautogui.moveTo(x = r.left + (r.width / 2), y = r.top + (r.height / 2))
        pyautogui.click(x = r.left + (r.width / 2), y = r.top + (r.height / 2), interval=0.5)
        return True

def py_locateOnscreennoclick(name):
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('Image/' + name, region=(left, top, width - left, height - top), grayscale = True, confidence=.8)

def COC_Mission():
    Poring_Open()
    Canival()
    py_locateOnscreen("COC/COCMission.png")
    py_locateOnscreen("COC/GO_immediately.png")
    COC_MissionClick()
    ClickMenuQuest(965, 630)
    py_locateOnscreen("COC/CloseCOC.png")
    return True

def Poring_Open():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        COC_Mission = cv2.imread('Image/COC/Poring_Open.png')
        result = cv2.matchTemplate(scr_remove, COC_Mission, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = COC_Mission.shape[1]
        h = COC_Mission.shape[0]
        print(max_val)
        if(max_val >= 0.75):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return True

def Canival():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        COC_Mission = cv2.imread('Image/COC/Canival.png')
        result = cv2.matchTemplate(scr_remove, COC_Mission, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = COC_Mission.shape[1]
        h = COC_Mission.shape[0]
        if(max_val >= 0.75):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return True

def COC_MissionClick():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        COC_Mission = cv2.imread('Image/COC/COC_Mission.png')
        result = cv2.matchTemplate(scr_remove, COC_Mission, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = COC_Mission.shape[1]
        h = COC_Mission.shape[0]
        if(max_val >= 0.75):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return True

def COC_MissionnoClick():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        COC_Mission = cv2.imread('Image/COC/COC_Mission.png')
        result = cv2.matchTemplate(scr_remove, COC_Mission, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = COC_Mission.shape[1]
        h = COC_Mission.shape[0]
        if(max_val >= 0.75):
            return True

def Getquest_Greencolor():
    while True:
        pix = pyscreeze.pixel(width - 89, height - 356)
        print(pix)
        if(pix[1] >= 230):
            time.sleep(1)
            pyautogui.click(x = width - 89, y = height - 356, interval=0.5)
            return True

def COCsource():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        COCsource_Image = cv2.imread('Image/COC/COCsource.png')
        result = cv2.matchTemplate(scr_remove, COCsource_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = COCsource_Image.shape[1]
        h = COCsource_Image.shape[0]
        if(max_val >= 0.80):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return True
        else:
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return False

def SendComplete():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        SendComplete_Image = cv2.imread('Image/COC/SendComplete.png')
        result = cv2.matchTemplate(scr_remove, SendComplete_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = SendComplete_Image.shape[1]
        h = SendComplete_Image.shape[0]
        if(max_val >= 0.80):
            return True
        else:
            return False

def CloseCOC():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        SendComplete_Image = cv2.imread('Image/COC/CloseCOC.png')
        result = cv2.matchTemplate(scr_remove, SendComplete_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = SendComplete_Image.shape[1]
        h = SendComplete_Image.shape[0]
        if(max_val >= 0.80):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return True

def Sendquest_COC():
    ClickMenuQuest(165, 290)
    COC_MissionnoClick()
    Getquest_Greencolor()
    if(COCsource() == True):
        ClickMenuQuest(555, 300)
        py_locateOnscreennoclick("COC/BuyCancelCOC.png")
        ClickMenuQuest(558, 494)
        ClickMenuQuest(818, 320)
        ClickMenuQuest(890, 394)
        py_locateOnscreen("COC/Correct_COC.png")
        py_locateOnscreen("COC/BuySuccess.png")
        nodelayClickMenuQuest(1223, 93)
        ClickMenuQuest(165, 290)
        COC_MissionnoClick()
        Getquest_Greencolor()
        py_locateOnscreen("COC/SendComplete.png")
        return 1
    else:
        time.sleep(2)
        if(SendComplete() == True):
            ClickMenuQuest(875, 310)
            ClickMenuQuest(780, 195)
            ClickMenuQuest(765, 290)
            py_locateOnscreennoclick("COC/BuyCancelCOC.png")
            ClickMenuQuest(558, 494)
            nodelayClickMenuQuest(818, 320)
            nodelayClickMenuQuest(890, 394)
            py_locateOnscreen("COC/Correct_COC.png")
            py_locateOnscreen("COC/BuySuccess.png")
            nodelayClickMenuQuest(1223, 93)
            ClickMenuQuest(165, 290)
            COC_MissionnoClick()
            Getquest_Greencolor()
            py_locateOnscreen("COC/SendComplete.png")
            return 1
        else:
            time.sleep(2)
            return 1

