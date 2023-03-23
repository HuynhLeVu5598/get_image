from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.support.ui import Select
import os
from time import sleep
import glob
import pyautogui
import pyperclip
import time

driver = webdriver.Chrome()

driver.get("https://googpt.ai/?hl=vi")

allpath = "test1/*.jpg"

for file_path in glob.glob(allpath):
    file_name = os.path.basename(file_path)
    file_name = file_name[:-4]
    file_name = " ".join(file_name.split("_"))
    with open(f"description.txt", "a", encoding="utf-8") as write_file:
        write_file.write(file_name)
        write_file.write("\n")

    while True:
        input_field = driver.find_element(By.ID, "search-input")

        # Wait for the input field to be visible
        wait = WebDriverWait(driver, 100)
        input_field = wait.until(
            EC.visibility_of_element_located((By.ID, "search-input"))
        )
        input_field.clear()
        # Enter text into the input field
        input_field.send_keys(f"Description for image {file_name} for SEO")

        # Wait for the button to be clickable
        wait = WebDriverWait(driver, 100)
        button = wait.until(EC.element_to_be_clickable((By.ID, "search-button")))

        # Click the button
        button.click()
        dem = 0
        sleep(8)
        while True:
            sleep(2)
            # Wait for the div element to be present
            wait = WebDriverWait(driver, 100)
            div_element = wait.until(
                EC.presence_of_element_located((By.ID, "ai-result"))
            )

            # Get the text content inside the div element
            content = div_element.text
            dem += 1
            if dem == 4:
                # Wait for the button to be clickable
                wait = WebDriverWait(driver, 100)
                button = wait.until(
                    EC.element_to_be_clickable((By.ID, "search-button"))
                )

                # Click the button
                button.click()
                dem = 0
                sleep(6)

            if content != "":
                break

        if (not content.startswith("Sorry")) and (
            not content.startswith("As an AI language model")
        ):
            break

    with open(f"description.txt", "a", encoding="utf-8") as write_file:
        write_file.write(content)
        write_file.write("\n")

    while True:
        input_field = driver.find_element(By.ID, "search-input")

        # Wait for the input field to be visible
        wait = WebDriverWait(driver, 100)
        input_field = wait.until(
            EC.visibility_of_element_located((By.ID, "search-input"))
        )
        input_field.clear()
        # Enter text into the input field
        input_field.send_keys(
            f"Tags for image {file_name} for SEO must have # before tag"
        )

        button = driver.find_element(By.ID, "search-button")

        # Wait for the button to be clickable
        wait = WebDriverWait(driver, 100)
        button = wait.until(EC.element_to_be_clickable((By.ID, "search-button")))

        # Click the button
        button.click()

        while True:
            # Wait for the div element to be present
            wait = WebDriverWait(driver, 100)
            div_element = wait.until(
                EC.presence_of_element_located((By.ID, "ai-result"))
            )

            # Get the text content inside the div element
            content = div_element.text

            if content != "":
                break

        if (not content.startswith("Sorry")) and (
            not content.startswith("As an AI language model")
        ):
            break

    with open(f"description.txt", "a", encoding="utf-8") as write_file:
        write_file.write(content)
        write_file.write("\n")
        write_file.write("\n")
