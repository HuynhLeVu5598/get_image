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
from undetected_chromedriver import Chrome


# driver = webdriver.Chrome("W:/Document/chromedriver_win32/chromedriver.exe")
with Chrome(use_subprocess=True) as driver:

    driver.get("https://stablediffusion.fr/webui")
    sleep(1000)
    # Prompt
    textarea = driver.find_element_by_css_selector('textarea[data-testid="textbox"]')

    # Enter text into the textarea
    textarea.send_keys("This is the text that will be entered")

    # Submit the form containing the textarea (if necessary)
    textarea.submit()

    sleep(1000)
