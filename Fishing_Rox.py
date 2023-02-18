from function.FN_Fising import *
from win32gui import FindWindow, GetWindowRect

Total_Fishing, Location_Fishing, i = Total_Location()
Noxplayer = FindWindow(None, "NoxPlayer")
left, top, width, height  = GetWindowRect(Noxplayer)
print(left, top, width, height)
# while i < int(Total_Fishing):
#     Center_iconX, Center_iconY = Fising_Icon(top, left, width - left, height - top)
#     if(Fishing_Click(int(Location_Fishing), int(Center_iconX), int(Center_iconY - 54)) == True):
#         i += 1