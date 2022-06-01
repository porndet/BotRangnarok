import time
import datetime
import cv2
import mss
import numpy
import pyautogui
import keyboard
from win32gui import FindWindow, GetWindowRect
import pyscreeze

Noxplayer = FindWindow(None, "NoxPlayer1")
left, top, width, height  = GetWindowRect(Noxplayer)
print(left, top, width, height)

def keyboardY():
    pyautogui.keyDown('y')
    pyautogui.keyUp('y')

def datetimeObj_Function():
    while True:
        Timehour = datetime.datetime.now().hour
        TimeMinute = datetime.datetime.now().minute
        if(Timehour == 5 and TimeMinute == 10):
            ClickMenuQuest(350, 300)
            keyboardY()
            print("Complete Gohome")
            return True

def datetime_fullBlessing():
    while True:
        Timehour = datetime.datetime.now().hour
        TimeMinute = datetime.datetime.now().minute
        if(Timehour == 5 and TimeMinute == 20):
            print("Complete Blessing")
            return True

def ClickMenuQuest(x1, y1):
    time.sleep(2)
    pyautogui.click(x = left + x1, y = top + y1, interval=0.5)
    return True

def py_locateOnscreen(name):
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('Image/' + name, region=(left, top, width - left, height - top), grayscale = True, confidence=.8)
    else:
        time.sleep(1)
        pyautogui.click(x = r.left + (r.width / 2), y = r.top + (r.height / 2), interval=0.5)
        return True
        # print(r.left, r.top, r.width, r.height)
        # pyautogui.moveTo(x = r.left + (r.width / 2), y = r.top + (r.height / 2))

def py_locateOnscreennoclick(name):
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('Image/' + name, region=(left, top, width - left, height - top), grayscale = True, confidence=.8)

def Fishingicon_first():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        Fishingicon_Image = cv2.imread('Image/Fishing/Fishingicon_first.png')
        result = cv2.matchTemplate(scr_remove, Fishingicon_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = Fishingicon_Image.shape[1]
        h = Fishingicon_Image.shape[0]
        print(max_val)
        if(max_val >= 0.75):
            time.sleep(1)
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return True

def Quest_Fishing():
    ClickMenuQuest(165, 290)
    py_locateOnscreen("Quest/Skipquest.png")
    ClickMenuQuest(165, 290)
    py_locateOnscreen("Fishing/Sendfish.png")
    py_locateOnscreen("Quest/Sendquest_item.png")
    ClickMenuQuest(165, 290)
    py_locateOnscreen("Fishing/Sendfish_complete.png")
    py_locateOnscreen("Quest/Skipquest.png")
    ClickMenuQuest(165, 290)
    Fishingicon_first()
    ClickMenuQuest(890, 705)
    py_locateOnscreen("Fishing/Itemfish.png")
    py_locateOnscreen("Fishing/Fishingicon.png")
    py_locateOnscreen("Fishing/Fishingicon.png")
    py_locateOnscreen("Fishing/Craftfish.png")
    py_locateOnscreen("Quest/Confirmquest.png")
    ClickMenuQuest(165, 290)
    py_locateOnscreen("Fishing/Usemagicbait.png")
    py_locateOnscreen("Quest/Skipquest.png")
    return True

def FirstLogin_Rox():
    py_locateOnscreen("Home/Roxicon.png")
    py_locateOnscreennoclick("Home/Roxfirst.png")
    time.sleep(2)
    ClickMenuQuest(660, 670)
    py_locateOnscreennoclick("Home/Roxbin.png")
    time.sleep(2)
    ClickMenuQuest(660, 670)
