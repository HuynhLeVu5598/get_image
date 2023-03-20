from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
import os
from time import sleep
import glob

get_dir = "C:/Users/BTTB/Downloads/t/"
download_dir = "2/"
# Set up Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://replicate.com/nightmareai/real-esrgan")
name = len(os.listdir(download_dir))

for img in glob.glob(get_dir + "*.png"):
    print(img)
    # Wait for the file input element to be visible
    file_input = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".dropzone input[type=file]"))
    )

    # Send the file path to the file input element
    file_input.send_keys(img)

    # Wait for the upload to complete
    WebDriverWait(driver, 100).until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, ".dropzone input[type=file]")
        )
    )

    scale_input = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.NAME, "scale"))
    )

    scale_input.clear()  # clear the input field in case there's any existing value
    scale_input.send_keys("10")  # enter the desired value
    sleep(2)

    button = driver.find_element(By.XPATH, "//button[contains(., 'Submit')]")
    button.click()

    download_button = WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.form-button-secondary[href$='output.png']")
        )
    )
    download_button.click()

    image = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.TAG_NAME, "img"))
    )
    image_url = image.get_attribute("src")
    image_response = requests.get(image_url)
    image_name = download_dir + f"image_{name}.png"
    name += 1
    with open(image_name, "wb") as f:
        f.write(image_response.content)

    sleep(2)
    driver.back()


sleep(500)
