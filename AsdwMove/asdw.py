def hold_key(key, hold_time):
    import time, pyautogui

    start_time = time.time()

    while time.time() - start_time < hold_time:
        pyautogui.press(key)

while True:
    hold_key('s', 3)
    hold_key('d', 3)
    hold_key('w', 3)
    hold_key('a', 3)
