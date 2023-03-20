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

# Text to be copied
text = "This stunning landscape image captures the beauty and tranquility of a dense forest. With rich, warm tones and intricate details, it transports you to a peaceful natural setting. This image is perfect for nature lovers and those who enjoy rustic and earthy themes"

textarea = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//textarea[@data-testid='textbox']"))
)


# Type text into the textarea
textarea.send_keys(text)

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


# select = WebDriverWait(driver, 100).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "gr-input"))
# )

# # Create a Select object for the element
# select_object = Select(select)

# # Select the 'LMS' option
# select_object.select_by_value("LMS")


# # Find the element to click on
# button = WebDriverWait(driver, 1000).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='prompt-button']"))
# )

# # Click on the element
# button.click()

sleep(2000)
