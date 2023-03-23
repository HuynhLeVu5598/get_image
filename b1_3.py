from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
from selenium.webdriver.support.ui import Select
import os
from time import sleep
import glob
import pyautogui
import pyperclip
import time


driver = webdriver.Chrome()
driver.get(
    "http://43xevft7udzo4udvnelzwf65225jjwfdoldkrrrekaiapj3lm54q.remote.moe/?__theme=dark"
)
text = "This stunning landscape image captures the beauty and tranquility of a dense forest. With rich, warm tones and intricate details, it transports you to a peaceful natural setting. This image is perfect for nature lovers and those who enjoy rustic and earthy themes"
# Copy the text to the clipboard
pyperclip.copy(text)
sleep(20)
for each_down in range(20):

    for i in range(18):
        pyautogui.press("tab")

    # Simulate keyboard shortcut for paste
    if each_down == 0:
        pyautogui.hotkey("ctrl", "v")

    for i in range(10):
        pyautogui.press("tab")

    pyautogui.press("down")

    pyautogui.hotkey("ctrl", "enter")

    sleep(20)
    for i in range(32):
        pyautogui.press("tab")

    sleep(20)
    pyautogui.press("enter")

    for i in range(5):
        pyautogui.press("tab")

    pyautogui.press("enter")
    sleep(2)

    for i in range(10):
        pyautogui.press("tab")

    pyautogui.press("enter")

    for i in range(6):
        pyautogui.press("tab")
    sleep(200)


##############################################

# # Copy the text to the clipboard
# pyperclip.copy(text)

# for each_down in range(20):

#     for i in range(11):
#         pyautogui.press("tab")

#     # Simulate keyboard shortcut for paste
#     if each_down == 0:
#         pyautogui.hotkey("ctrl", "v")
#     for i in range(10):
#         pyautogui.press("tab")

#     pyautogui.press("down")

#     pyautogui.hotkey("ctrl", "enter")

#     sleep(13)
#     for i in range(24):
#         pyautogui.press("tab")

#     pyautogui.press("enter")

#     for i in range(5):
#         pyautogui.press("tab")

#     pyautogui.press("enter")
#     sleep(2)

#     for i in range(10):
#         pyautogui.press("tab")

#     pyautogui.press("enter")

#     for i in range(6):
#         pyautogui.press("tab")


sleep(2000)
