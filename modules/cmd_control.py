import ctypes
import pyautogui
import time

def ventana():
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    time.sleep(0.5)
    pyautogui.hotkey("win", "up")

    contador = 1
    a = 0
    b = 0
    while contador == 1:
        if a >= screen_width - 13:
            b -= 4
            contador = 0
        a += 13
        b += 1
    return b