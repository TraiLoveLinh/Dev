import time
import pyautogui as pa

time.sleep(5)

n = 5
for i in range(n):
    pa.write("hii, anh yeu em", interval=0.1)
    pa.press("enter")