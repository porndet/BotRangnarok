import mss
from PIL import Image
import cv2
import numpy as np

while True:
    sct = mss.mss()
    monitor = sct.monitors[1]
    img = np.array(sct.grab(monitor))
    scr_remove = img[:,:,:3]
    COC_Mission = cv2.imread('Image/COC/PoringOpen_NotFull.png')
    result = cv2.matchTemplate(scr_remove, COC_Mission, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    w = COC_Mission.shape[1]
    h = COC_Mission.shape[0]
    print(min_val, max_val, min_loc, max_loc)
    scr = img.copy()
    cv2.rectangle(scr, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,0,255), 2)
    cv2.imshow("Result", scr)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break


# while True:
#     img = sct.grab(monitor)
