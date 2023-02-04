import pyautogui

while True:
    pyautogui.moveRel(100, 0, 1)
    pyautogui.moveRel(0, -100, 1)
    pyautogui.moveRel(-100, 0, 1)
    pyautogui.moveRel(0, 100, 1)
