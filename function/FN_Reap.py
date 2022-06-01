import pytesseract
import cv2
import numpy
import pyautogui
import mss
import time
import pyscreeze
from win32gui import FindWindow, GetWindowRect

custom_config = r'--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789+-*'
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

Noxplayer = FindWindow(None, "NoxPlayer1")
left, top, width, height  = GetWindowRect(Noxplayer)
print(left, top, width, height)

def ClickMenuQuest(x1, y1):
    time.sleep(1)
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

def py_locateOnscreeNotime(name):
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('Image/' + name, region=(left, top, width - left, height - top), grayscale = True, confidence=.8)
    else:
        pyautogui.click(x = r.left + (r.width / 2), y = r.top + (r.height / 2), interval=0.5)
        return True

def ConfirmButton():
    sct = mss.mss()
    monitor = {"top": top, "left": left, "width": width, "height": height}
    while True:
        img = numpy.array(sct.grab(monitor))
        scr_remove = img[:,:,:3]
        ConfirmButtonImage = cv2.imread('Image/Reap/ConfirmButton.png')
        result = cv2.matchTemplate(scr_remove, ConfirmButtonImage, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if(max_val >= 0.85):
            return 'Success Reap'
        else:
            py_locateOnscreeNotime('Reap/QuestCrop.png')
            return True

def findconfirmbutton():
    while True:
        if(ConfirmButton() == 'Success Reap'):
            return 1

def FindresultText(n1, mark, n2):
    if(mark == '+'):
        return n1 + n2
    elif(mark == '-'):
        return n1 - n2
    elif(mark == '*'):
        return n1 * n2
    else:
        return 'Failed Error'

def ResultTextpytesseract():
    img = cv2.imread("Image/Reap/Screenshot.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    scaled = cv2.resize(gray, (0,0), fx = 4, fy = 4, interpolation = cv2.INTER_CUBIC)
    thresh = 240
    img_binary_inv = cv2.threshold(scaled, thresh, 255, cv2.THRESH_BINARY_INV)[1]
    text = pytesseract.image_to_string(img_binary_inv, lang='eng', config = custom_config)
    SvalueString = text[:-2]
    print(SvalueString)
    if(len(SvalueString) == 3):
        if(SvalueString[1] == '4' or SvalueString[1] == '7'):
            if(SvalueString[1] == '4'):
                result = FindresultText(int(SvalueString[0]), '+', int(SvalueString[2]))
            else:
                result = FindresultText(int(SvalueString[0]), '*', int(SvalueString[2]))
        else:
            result = FindresultText(int(SvalueString[0]), SvalueString[1], int(SvalueString[2]))
            
        if(result != 'Failed Error'):
            return result
        else:
            scaledx3 = cv2.resize(gray, (0,0), fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
            thresh = 240
            img_binary_invx3 = cv2.threshold(scaledx3, thresh, 255, cv2.THRESH_BINARY_INV)[1]
            text = pytesseract.image_to_string(img_binary_invx3, lang='eng', config = custom_config)
            SvalueString = text[:-2]
            if(len(SvalueString) == 3):
                result = FindresultText(int(SvalueString[0]), SvalueString[1], int(SvalueString[2]))
                if(result != 'Failed Error'):
                    return result
                else:
                    return 'Error1'
            else:
                return 'Error2'
    elif(len(SvalueString) == 2):
        if(SvalueString[0] == '+' or SvalueString[0] == '-' or SvalueString[0] == '*'):
            result = FindresultText(1, SvalueString[0], int(SvalueString[1]))
            if(result != 'Failed Error'):
                return result
            else:
                return 'Error3'
        elif(SvalueString[1] == '+' or SvalueString[1] == '-' or SvalueString[1] == '*'):
            result = FindresultText(int(SvalueString[0]), SvalueString[1], 1)
            if(result != 'Failed Error'):
                return result
            else:
                return 'Error5'
        else:
            result = FindresultText(int(SvalueString[1]), SvalueString[1], 1)
            if(result != 'Failed Error'):
                return result
            else:
                return 'Error4'
    elif(len(SvalueString) == 1):
        result = FindresultText(int(SvalueString[0]), '*', 1)
        return result
    else:
        if(SvalueString.find("+") != -1):
            if(SvalueString[1] == '4'):
                result = FindresultText(int(SvalueString[0]), SvalueString[2], int(SvalueString[3]))
                return result
            else:
                number_font = SvalueString[0] + SvalueString[1]
                result = FindresultText(int(number_font), SvalueString[2], int(SvalueString[3]))
                return result
        elif(SvalueString.find("-") != -1):
            number_font = SvalueString[0] + SvalueString[1]
            result = FindresultText(int(number_font), SvalueString[2], int(SvalueString[3]))
            return result
        elif(SvalueString.find("*") != -1):
            number_font = SvalueString[0] + SvalueString[1]
            result = FindresultText(int(number_font), SvalueString[2], int(SvalueString[3]))
            return result

def Number_Click(num):
    if(num == '0'):
        ClickMenuQuest(1060, 510)
        return True
    elif(num == '1'):
        ClickMenuQuest(840, 430)
        return True
    elif(num == '2'):
        ClickMenuQuest(910, 430)
        return True
    elif(num == '3'):
        ClickMenuQuest(990, 430)
        return True
    elif(num == '4'):
        ClickMenuQuest(840, 510)
        return True    
    elif(num == '5'):
        ClickMenuQuest(910, 510)
        return True
    elif(num == '6'):
        ClickMenuQuest(990, 510)
        return True
    elif(num == '7'):
        ClickMenuQuest(840, 580)
        return True
    elif(num == '8'):
        ClickMenuQuest(910, 580)
        return True
    elif(num == '9'):
        ClickMenuQuest(990, 580)
        return True

