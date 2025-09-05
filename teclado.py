import pyautogui
import time


for i in range(1, 100):
    time.sleep(0.5)
    posicion_mouse = pyautogui.position()
    print(f" Posición Mouse = {posicion_mouse}")

