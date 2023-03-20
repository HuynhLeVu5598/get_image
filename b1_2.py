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

choose_file = int(input("choose name folder save: "))
download_dir = f"C:/Users/BTTB/Downloads/{choose_file}"

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

driver = webdriver.Chrome()
driver.get("https://skybox.blockadelabs.com/")
sleep(20)
name = 0
init_length = len(os.listdir(download_dir))

list_selected = [
    "Fantasy Landscape",
    "Anime Art Style",
    "Surreal Style",
    "Digital Painting",
    "Scenic",
    "Nebula",
    "Realistic",
    "SciFi",
    "Dreamlike",
    "Interior Views",
    "Sky",
    "Dutch Masters",
    "Infrared (Experimental Nature Scenes)",
    "Low Poly (Experimental)",
    "Advanced (No Style Words)",
]

with open(f"image{choose_file}.txt", "r", encoding="utf-8") as read_file:
    content = read_file.readlines()

mycontent = []
for c in content:
    mycontent.append(c)
already_use = []
for mc in mycontent:
    # for i in range(1, 16):
    input_element = WebDriverWait(driver, 1000).until(
        EC.visibility_of_element_located((By.NAME, "prompt"))
    )
    try:
        input_element.clear()
    except:
        pass
    input_element.send_keys(mc)
    print("mc: ", mc)
    already_use.append(mc)
    with open(f"image{choose_file}.txt", "w", encoding="utf-8") as write_file:
        for mc1 in mycontent:
            if mc1 not in already_use:
                write_file.write(mc1)

    # dropdown = WebDriverWait(driver, 100).until(
    #     EC.visibility_of_element_located((By.NAME, "styleId"))
    # )

    for ls in list_selected:
        try:
            sleep(3)
            select_element = driver.find_element(By.NAME, "styleId")
            # Select the second option (index starts from 0)
            select_element.click()
            sleep(2)

            select = Select(select_element)
            select.select_by_visible_text(ls)
            # Wait for the button to be clickable
            generate_button = WebDriverWait(driver, 1000).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Generate"]'))
            )
            generate_button.click()
            while True:
                try:
                    # Wait for the download button to be clickable for up to 10 seconds
                    wait = WebDriverWait(driver, 1000)
                    download_button = wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, '//button[contains(span, "Download image")]')
                        )
                    )

                    # Click the download button
                    download_button.click()

                    # Check the current length of the download directory
                    sleep(5)
                    current_length = len(os.listdir(download_dir))
                    print("Pass: ", current_length)

                    # If the length has increased, assume the download is complete
                    if current_length > init_length:
                        init_length += 1
                        break
                except:
                    pass
        except:

            sleep(2)
            pass
