import pyautogui, sys, time, random

#print('Press Ctrl-C to quit.')
i = 0
print("you have 10 seconds to position your mouse where you want to initiate a click")

time.sleep(10)
pyautogui.click()

try:
    #while True:
    while i < 88:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='\n', flush=True)
        pyautogui.click()
        delay = random.randrange(120,140)
        time.sleep(delay)
        pyautogui.click()
        i += 1
except KeyboardInterrupt:
    print('\n')
