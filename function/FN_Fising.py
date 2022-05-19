import cv2
import mss
import numpy
import pyautogui
import time
import keyboard
import pyscreeze

def Noxplayname(nox):
    switcher = {
        "1": "NoxPlayer",
        "2": "NoxPlayer(1)"
    }
    return switcher.get(nox, "กรุณากรอกเลขที่อยู่ในลิสต์")

def Total_Location():
    print("-----------------------")
    Total = input("จะตกปลากี่รอบกรอกจำนวน : ")
    i = 0
    return (Total, 204, i)

def CheckvalueImage(name, top, left, width, height):
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width, "height": height}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        Checkvalue_Img = cv2.imread('Image/' + name)
        result = cv2.matchTemplate(scr_remove, Checkvalue_Img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = Checkvalue_Img.shape[1]
        h = Checkvalue_Img.shape[0]
        print(min_val, max_val, min_loc, max_loc)
        if(max_val >= 0.80):
            pyautogui.moveTo(max_loc[0] + left + (w/2), max_loc[1] + top + (h/2))
            return False
        src = img.copy()
        cv2.imshow('ImageCheck', scr_remove)
        cv2.waitKey(1)
        time.sleep(.10)
        if keyboard.is_pressed('q'):
            break

def Fising_Icon(top, left, width, height):
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width, "height": height}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        FishingIcon_Img = cv2.imread('Image/Fishing/Fishingicon.png')
        result = cv2.matchTemplate(scr_remove, FishingIcon_Img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = FishingIcon_Img.shape[1]
        h = FishingIcon_Img.shape[0]
        #print(min_val, max_val, min_loc, max_loc)
        if(max_val >= 0.85):
            pyautogui.moveTo(max_loc[0] + left + (w/2), max_loc[1] + top + (h/2))
            pyautogui.click(interval = 0.1)
            return (max_loc[0] + left + (w/2), max_loc[1] + top + (h/2))

def Fishing_Click(greenlocation, centerx, centery):
    while True:
        pix = pyscreeze.pixel(centerx, centery)
        print(pix[1], greenlocation)
        if(pix[1] >= greenlocation):
            pyautogui.click()
            return True

def Night_Check(top, left, width, height):
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width, "height": height}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        Nighticon_Img = cv2.imread('Image/Home/Nighticon.png')
        result = cv2.matchTemplate(scr_remove, Nighticon_Img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = Nighticon_Img.shape[1]
        h = Nighticon_Img.shape[0]
        # print(min_val, max_val, min_loc, max_loc)
        if(max_val >= 0.80):
            return True
        else:
            return False