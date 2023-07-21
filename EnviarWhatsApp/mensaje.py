import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+51941234307')
sleep(15)

for i in range(5):
    pyautogui.typewrite('prueba')
    pyautogui.press('enter')