from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
from io import BytesIO

# Set up Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://discord.com/channels/662267976984297473/989268383751106560")
sleep(50)
name = 0
for i in range(1000):
    # Scroll to the top of the page
    driver.execute_script("window.scrollTo(0, 0);")
    sleep(2)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all the image elements
    image_elements = soup.find_all("img")

    # Download each image
    for i, image_element in enumerate(image_elements):
        image_url = image_element.get("src")
        if image_url.startswith("http"):
            image_response = requests.get(image_url)

            image = Image.open(BytesIO(image_response.content))
            width, height = image.size

            # Check if image is smaller than 200x200 pixels
            if width < 200 or height < 200:
                continue

            image_extension = os.path.splitext(image_url)[1]
            image_name = f"2/image_{name}.png"
            name += 1
            with open(image_name, "wb") as f:
                f.write(image_response.content)

# Close the driver
driver.quit()
