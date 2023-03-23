from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from undetected_chromedriver import Chrome


# driver = webdriver.Chrome("W:/Document/chromedriver_win32/chromedriver.exe")
with Chrome(use_subprocess=True) as driver:

    driver.get("https://googpt.ai/?hl=vi")

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
            "give me 5 prompt to product beauty of nature stock photo detail"
        )

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
            for i in range(1, 11):
                content = content.replace(f"{i}. ", "")
                content = content.replace(f"{i}) ", "")

            content = content.replace('"', "")
            content = content.replace("\n\n", "\n")

            with open(f"allimagenature.txt", "a", encoding="utf-8") as write_file:
                write_file.write(content)
                if content != "\n":
                    write_file.write("\n")
