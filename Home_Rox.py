from function.FN_Home import *

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
        if(max_val >= 0.75):
            pyautogui.click(x = max_loc[0] + left + (w / 2), y = max_loc[1] + top  + (h / 2), interval = 0.5)
            return True

# ------------------------------------------------ Daily Quest -----------------------------------------#
# Quest_Fishing()
# while True :
#     SendQuestMssion()

# import COCMission_Rox
import MissionBoard_Rox

# import MissionBoardLike_Rox

# if(datetimeObj_Function() == True):
#     if(datetime_fullBlessing() == True):
#         py_locateOnscreen('Home/QuestClick.png')
#         ClickMenuQuest(275, 640)
#         py_locateOnscreen('Home/Closeicon.png')
#         time.sleep(4)
#         !ssasadsddda()
#         import COCMission_Rox
#         import MissionBoard_Rox

# py_locateOnscreen('Home/QuestClick.png')
# ClickMenuQuest(275, 640)
# ClickMenuQuest(350, 300)
# ClickMenuQuest(275, 640)
# py_locateOnscreen('Home/Closeicon.png')
# time.sleep(2)
# import COCMission_Rox
# import MissionBoard_Rox