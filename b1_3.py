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


### web
# driver = webdriver.Chrome()
# driver.get("https://stablediffusion.fr/webui")
# prompt = "This stunning landscape image captures the beauty and tranquility of a dense forest. With rich, warm tones and intricate details, it transports you to a peaceful natural setting. This image is perfect for nature lovers and those who enjoy rustic and earthy themes"
# # Copy the text to the clipboard
# sleep(20)
# for each_down in range(20):
#     for i in range(19):
#         if driver.window_handles and not driver.execute_script(
#             "return window.outerWidth === 0 && window.outerHeight === 0"
#         ):
#             pyautogui.press("tab")
#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break
#     # prompt
#     pyautogui.hotkey("ctrl", "a")
#     pyautogui.press("delete")
#     pyperclip.copy(prompt)
#     pyautogui.hotkey("ctrl", "v")

#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break

#     # negative prompt
#     negative_prompt = "ulgy"
#     pyautogui.press("tab")
#     pyperclip.copy(negative_prompt)

#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break

#     pyautogui.hotkey("ctrl", "a")
#     pyautogui.press("delete")
#     pyautogui.hotkey("ctrl", "v")

#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break

#     # sampling step
#     for i in range(10):
#         if driver.window_handles and not driver.execute_script(
#             "return window.outerWidth === 0 && window.outerHeight === 0"
#         ):
#             pyautogui.press("tab")
#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break

#     for i in range(30):
#         if driver.window_handles and not driver.execute_script(
#             "return window.outerWidth === 0 && window.outerHeight === 0"
#         ):
#             pyautogui.press("up")
#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break
#     # sampling method
#     pyautogui.press("tab")

#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break
#     pyautogui.press("down")

#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break

#     pyautogui.hotkey("ctrl", "enter")

#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break

#     for i in range(19):
#         if driver.window_handles and not driver.execute_script(
#             "return window.outerWidth === 0 && window.outerHeight === 0"
#         ):
#             pyautogui.press("tab")

#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break

#     sleep(80)

#     pyautogui.press("enter")
#     sleep(40)
#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break
#     # download
#     for i in range(6):
#         if driver.window_handles and not driver.execute_script(
#             "return window.outerWidth === 0 && window.outerHeight === 0"
#         ):
#             pyautogui.press("tab")

#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break
#     pyautogui.press("enter")
#     sleep(2)

#     for i in range(13):
#         if driver.window_handles and not driver.execute_script(
#             "return window.outerWidth === 0 && window.outerHeight === 0"
#         ):
#             pyautogui.press("tab")

#     pyautogui.press("enter")
#     if not driver.window_handles and driver.execute_script(
#         "return window.outerWidth === 0 && window.outerHeight === 0"
#     ):
#         break

#     for i in range(6):
#         if driver.window_handles and not driver.execute_script(
#             "return window.outerWidth === 0 && window.outerHeight === 0"
#         ):
#             pyautogui.press("tab")
#     sleep(20)
#     driver.refresh()
#     driver.get("https://stablediffusion.fr/webui")
#     sleep(10)

### google colab

# driver = webdriver.Chrome()
# driver.get(
#     "http://43xevft7udzo4udvnelzwf65225jjwfdoldkrrrekaiapj3lm54q.remote.moe/?__theme=dark"
# )
# text = "This stunning landscape image captures the beauty and tranquility of a dense forest. With rich, warm tones and intricate details, it transports you to a peaceful natural setting. This image is perfect for nature lovers and those who enjoy rustic and earthy themes"
# # Copy the text to the clipboard
# pyperclip.copy(text)
# sleep(20)
# for each_down in range(20):

#     for i in range(18):
#         pyautogui.press("tab")

#     # Simulate keyboard shortcut for paste
#     if each_down == 0:
#         pyautogui.hotkey("ctrl", "v")

#     for i in range(10):
#         pyautogui.press("tab")

#     pyautogui.press("down")

#     pyautogui.hotkey("ctrl", "enter")

#     sleep(20)
#     for i in range(32):
#         pyautogui.press("tab")

#     sleep(20)
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
#     sleep(200)


##############################################


#### local computer
# Copy the text to the clipboard


# prompt = (
#     "A pet dog happily wagging its tail running towards its owner in a vibrant garden."
# )

driver = webdriver.Chrome()

driver.get("chrome://settings/downloads")

sleep(20)

driver.get("http://127.0.0.1:7860")

sleep(10)


first_prompt = "RAW photo "
last_prompt = " (high detailed skin:1.2), 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3"
# negative_prompt = " (semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"
negative_prompt = "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"
dir_get = "txt"
choose_file = 2
with open(
    dir_get + f"/image_{str(choose_file)}.txt", "r", encoding="utf-8"
) as read_file:
    content = read_file.readlines()

myprompts = []
for c in content:
    myprompts.append(c)

already_use = []
for prompt in myprompts:
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:7860")

    already_use.append(prompt)
    with open(
        dir_get + f"/image_{choose_file}.txt", "w", encoding="utf-8"
    ) as write_file:
        for mc1 in myprompts:
            if mc1 not in already_use:
                write_file.write(mc1)

    for each_down in range(20):
        for i in range(11):
            pyautogui.press("tab")

        # prompt
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("delete")
        pyperclip.copy(first_prompt + prompt + last_prompt)
        pyautogui.hotkey("ctrl", "v")

        pyautogui.press("tab")

        # negative prompt
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("delete")
        pyperclip.copy(negative_prompt)
        pyautogui.hotkey("ctrl", "v")

        # sampling method
        for i in range(9):
            pyautogui.press("tab")

        if each_down != 0 and each_down != 2:
            pyautogui.press("down")

        if each_down == 3:
            for i in range(2):
                pyautogui.press("down")

        # sampling steps
        pyautogui.press("tab")
        if each_down == 0:
            for i in range(5):
                pyautogui.press("up")

        # Restore faces
        pyautogui.press("tab")

        if each_down == 0:
            pyautogui.press("space")

        # Width
        for i in range(5):
            pyautogui.press("tab")

        if each_down == 0:
            for i in range(61):
                pyautogui.press("up")

        # Height
        for i in range(2):
            pyautogui.press("tab")

        if each_down == 0:
            for i in range(20):
                pyautogui.press("up")
        # seed
        for i in range(8):
            pyautogui.press("tab")
        pyautogui.press("up")

        pyautogui.hotkey("ctrl", "enter")

        sleep(30)
        for i in range(7):
            pyautogui.press("tab")

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


sleep(2000)
