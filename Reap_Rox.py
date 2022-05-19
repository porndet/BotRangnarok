from function.FN_Reap import *
from datetime import datetime

for i in range(20):
    if(findconfirmbutton() == 1):
        Screenshot_Image = pyautogui.screenshot(region = (width - 729, height - 392, 89, 37))
        Screenshot_Image.save(r"Image/Reap/Screenshot.png")
        Result_Reap = ResultTextpytesseract()
        print(Result_Reap)
        if(Result_Reap == 'Error1' or Result_Reap == 'Error2' or Result_Reap == 'Error3' or Result_Reap == 'Error4'):
            current_time = "Screenshot " + datetime.now().strftime("%d-%m-%Y_%H%M%S") + '.png'
            Screenshot_Image.save("Image/Reap/" + current_time)
        else:
            StringResult = str(Result_Reap)
            if(len(StringResult) == 1):
                ClickMenuQuest(640, 425)
                Number_Click(StringResult[0])
                ClickMenuQuest(1060, 580)
                py_locateOnscreen('Reap/ConfirmButton.png')
            else:
                ClickMenuQuest(640, 425)
                Number_Click(StringResult[0])
                Number_Click(StringResult[1])
                ClickMenuQuest(1060, 580)
                py_locateOnscreen('Reap/ConfirmButton.png')