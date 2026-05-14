import pyautogui
import subprocess


def join(id):
    subprocess.call("C:\\Users\\dell\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    while True:
        join1 = pyautogui.locateOnScreen('join1.png')
        if join1 != None:
            pyautogui.click(join1)
            print("Clicked Join 1")
            pyautogui.click(pyautogui.locateOnScreen('back.png'))
            break
        else:
            print("Could not find join 1")
      
    while True:
        feild = pyautogui.locateOnScreen('feild.png')
        if feild != None:
            pyautogui.click(feild)
            print("Made the Input Feild active")
            pyautogui.typewrite(id)
            pyautogui.click(pyautogui.locateOnScreen('join2.png'))
            break
        else:
            print("Could not find the input feild")

join ("513 560 6873")






