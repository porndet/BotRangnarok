import time
import cv2
import mss
import numpy as np
import pyautogui
import numpy
from array import *
import pyscreeze
from win32gui import FindWindow, GetWindowRect

Noxplayer = FindWindow(None, "NoxPlayer")
left, top, width, height  = GetWindowRect(Noxplayer)
print(left, top, width, height)

def ClickPoring():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while "Screen capturing":
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        ClickPoring_Image = cv2.imread('Image/Board/ClickPoring.png')
        result = cv2.matchTemplate(scr_remove, ClickPoring_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = ClickPoring_Image.shape[1]
        h = ClickPoring_Image.shape[0]
        #print(min_val, max_val, min_loc, max_loc, w, h)
        src = img.copy()
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            time.sleep(0.5)
            return True

def ClickCarnival():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        ClickCanival_Image = cv2.imread('Image/Board/COCCanival.png')
        result = cv2.matchTemplate(scr_remove, ClickCanival_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = ClickCanival_Image.shape[1]
        h = ClickCanival_Image.shape[0]
        src = img.copy()
        if(max_val >= 0.80):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            time.sleep(0.5)
            return True

def COCMission():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        MissionBoardIcon_Image = cv2.imread('Image/Board/MissionBoardIcon.png')
        result = cv2.matchTemplate(scr_remove, MissionBoardIcon_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = MissionBoardIcon_Image.shape[1]
        h = MissionBoardIcon_Image.shape[0]
        # print(min_val, max_val, min_loc, max_loc, w, h)
        src = img.copy()
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return True

def GoCOC_function():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        GoCoc_Image = cv2.imread('Image/Board/GoCOC.png')
        result = cv2.matchTemplate(scr_remove, GoCoc_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = GoCoc_Image.shape[1]
        h = GoCoc_Image.shape[0]
        # print(min_val, max_val, min_loc, max_loc, w, h)
        src = img.copy()
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval=0.5)
            return True

def GoMissonBoard():
    # ClickPoring()
    ClickCarnival()
    COCMission()
    GoCOC_function()

def ClickMenuConfirm():
    time.sleep(0.1)
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        ConfirmQuest_Image = cv2.imread('Image/Board/ConfirmQuest.png')
        result = cv2.matchTemplate(scr_remove, ConfirmQuest_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = ConfirmQuest_Image.shape[1]
        h = ConfirmQuest_Image.shape[0]
        # print(min_val, max_val, min_loc, max_loc, w, h)
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True

def GetQuestMissionBoard():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        QuestBounty_Image = cv2.imread('Image/Board/QuestBounty.png')
        result = cv2.matchTemplate(scr_remove, QuestBounty_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = QuestBounty_Image.shape[1]
        h = QuestBounty_Image.shape[0]
        #print(min_val, max_val, min_loc, max_loc, w, h)
        src = img.copy()
        if(max_val >= 0.85):
            return True

def GetQuestMissionBoard1():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        Questicon_Image = cv2.imread('Image/Board/Questicon.png')
        result = cv2.matchTemplate(scr_remove, Questicon_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = Questicon_Image.shape[1]
        h = Questicon_Image.shape[0]
        #print(min_val, max_val, min_loc, max_loc, w, h, "Board")
        src = img.copy()
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True


def GoQuestMissionBoard():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        GoQuestMissionBoard_Image = cv2.imread('Image/Board/GoQuestMissionBoard.png')
        result = cv2.matchTemplate(scr_remove, GoQuestMissionBoard_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = GoQuestMissionBoard_Image.shape[1]
        h = GoQuestMissionBoard_Image.shape[0]
        #print(min_val, max_val, min_loc, max_loc, w, h)
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True

def GoQuestMissionBoardNew():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    timeout = 0
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        GoQuestMissionBoard_Image = cv2.imread('Image/Board/GoQuestMissionBoard.png')
        result = cv2.matchTemplate(scr_remove, GoQuestMissionBoard_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = GoQuestMissionBoard_Image.shape[1]
        h = GoQuestMissionBoard_Image.shape[0]
        print(min_val, max_val, min_loc, max_loc, w, h)
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True
        else:
            timeout += 1
            if timeout >= 200:
                return False

def NextCommunicationNPC():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        NextQuesticon_Image = cv2.imread('Image/Board/NextQuesticon.png')
        result = cv2.matchTemplate(scr_remove, NextQuesticon_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = NextQuesticon_Image.shape[1]
        h = NextQuesticon_Image.shape[0]
        # print(min_val, max_val, min_loc, max_loc, w, h)
        if(max_val >= 0.85):
            time.sleep(0.5)
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True

def CancelMssionBoard():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        CancelMissionBoard_Image = cv2.imread('Image/Board/CancelMissionBoard.png')
        result = cv2.matchTemplate(scr_remove, CancelMissionBoard_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = CancelMissionBoard_Image.shape[1]
        h = CancelMissionBoard_Image.shape[0]
        # print(min_val, max_val, min_loc, max_loc, w, h)
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True

def CropRox():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        CheckQuest_Image = cv2.imread('Image/Board/CheckQuest.png')
        result = cv2.matchTemplate(scr_remove, CheckQuest_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = CheckQuest_Image.shape[1]
        h = CheckQuest_Image.shape[0]
        if(max_val >= 0.85):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True

def keyboardESC():
    for i in range(2):
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')

def keyboardS():
    for i in range(2):
        pyautogui.keyDown('s')
        pyautogui.keyUp('s')

def GetGoNextMissionBoard(Clickx, Clicky):
    time.sleep(0.5)
    GetQuestMissionBoard1()
    time.sleep(0.3)
    pyautogui.click(x = Clickx, y = Clicky, interval = 0.5)
    GoQuestMissionBoard()
    NextCommunicationNPC()

def GetGoMissionBoard(Clickx, Clicky):
    GetQuestMissionBoard1()
    time.sleep(0.2)
    pyautogui.click(x = Clickx, y = Clicky, interval = 0.5)
    GoQuestMissionBoard()

def CommunicationCondition(Com):
    if(Com < 2):
        pyautogui.click(x = 921, y = 285, interval = 0.5)
        ClickMenuConfirm()
        return True
    else:
        return False

def CropCondition(Crop):
    if(Crop < 2):
        pyautogui.click(x = 921, y = 285, interval = 0.5)
        ClickMenuConfirm()
        return True
    else:
        return False

def AttackCondition(Attack):
    if(Attack < 6):
        pyautogui.click(x = 921, y = 285, interval = 0.5)
        ClickMenuConfirm()
        return True
    else:
        return False

def SendQuestMssion():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width - left, "height": height - top}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        CheckQuest_Image = cv2.imread('Image/Board/SendQuest.png')
        result = cv2.matchTemplate(scr_remove, CheckQuest_Image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = CheckQuest_Image.shape[1]
        h = CheckQuest_Image.shape[0]
        if(max_val >= 0.85):
            time.sleep(1)
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True
        

# ClickQuestNew = [157, 277]
# pyautogui.click(ClickQuestNew, interval = 1)
# time.sleep(300)

ClickQuestNew = [157, 277]
pyautogui.click(ClickQuestNew, interval = 1)
time.sleep(300)

def AttackQuestMission(x):
    pyautogui.click(828, 576, interval = 1)
    GetQuestMissionBoard1()
    time.sleep(1)
    pyautogui.click(x, interval = 1)
    if GoQuestMissionBoardNew() == True:
        time.sleep(300)
        return True
    else:
        AttackQuestMission1(x)
        return True

def AttackQuestMission1(x):
    GetQuestMissionBoard1()
    time.sleep(1)
    pyautogui.click(x, interval = 1)
    GoQuestMissionBoard()    
    return True       

AttackQuestXY = [340, 233]
for i in range(6):
    AttackQuestMission(AttackQuestXY)
    AttackQuestXY[1] += 48
else:
    pyautogui.click(828, 576, interval = 1)
    GoMissonBoard()