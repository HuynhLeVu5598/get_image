import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
from io import BytesIO
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Selenium WebDriver
name = 39794

list_dc = [
    "https://discord.com/channels/662267976984297473/989268383751106560",
    "https://discord.com/channels/662267976984297473/997262352632250549",
    "https://discord.com/channels/662267976984297473/997271766302982234",
]

driver = webdriver.Chrome()
driver.get("https://discord.com/channels/662267976984297473/989268383751106560")

sleep(60)
try:
    email_input = driver.find_element(By.NAME, "email")
    # input_elem = driver.find_element(By.ID, "uid_13")
    email_input.send_keys("huynhlevumm@gmail.com")

    pw_input = driver.find_element(By.NAME, "password")
    pw_input.send_keys("100pagesCode3712")
    pw_input.send_keys(Keys.RETURN)
except:
    pass
sleep(60)

while True:

    print("Start")
    for li in list_dc:
        driver.get(li)
        sleep(15)

        for i in range(1000):
            # Scroll to the top of the page
            driver.execute_script("window.scrollTo(0, 0);")
            # print("a")
            # sleep(2)

        print("Start2")

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Find all the div elements with id starting with "message-content-"
        div_elements = soup.find_all(
            "div", {"id": lambda x: x and x.startswith("message-content-")}
        )
        # Iterate over the div elements and find the ones that contain "Upscaled by"
        for div_element in div_elements:

            if "Upscaled" in div_element.text:

                # Find the parent div element
                parent_div = div_element.parent
                parent_div = parent_div.parent

                # .find("div", class_="message-2CShn3")

                # Do something with the parent div element
                image_elements = parent_div.find_all("img")
                if image_elements:

                    for image in image_elements:

                        image_url = image.get("src")
                        if image_url.startswith("http"):
                            image_response = requests.get(image_url)
                            image = Image.open(BytesIO(image_response.content))
                            width, height = image.size

                            # Check if image is smaller than 200x200 pixels
                            if width < 200 or height < 200:
                                continue

                            image_extension = os.path.splitext(image_url)[1]
                            image_name = f"4/image_{name}.png"
                            name += 1
                            with open(image_name, "wb") as f:
                                f.write(image_response.content)

        # Close the driver
        # driver.quit()
        sleep(15)
