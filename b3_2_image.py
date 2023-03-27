from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep
import glob
import csv
from undetected_chromedriver import Chrome

multi_data = []

# driver = webdriver.Chrome()

allpath = "test1/*.jpg"

# driver = webdriver.Chrome("W:/Document/chromedriver_win32/chromedriver.exe")
with Chrome(use_subprocess=True) as driver:
    driver.get("https://googpt.ai/?hl=vi")
    for file_path in glob.glob(allpath):
        data = []

        file_name = os.path.basename(file_path)
        # filename
        data.append(str(file_name))
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
            input_field.send_keys(
                f"Description for image {file_name} must less than 200 words, encapsulated in one sentence"
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
                break

        # descripton
        # content = content.replace("\n", " ")
        # content = content.replace('"""', "")
        # content = content.replace('"', "")
        data.append(content)

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
                f"Tags for image {file_name}, tags are separated by commas, at least 7 tags"
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
        # tags
        content = content.replace(". ", ",")
        data.append(str(content))
        with open(f"description.txt", "a", encoding="utf-8") as write_file:
            write_file.write(content)
            write_file.write("\n")
            write_file.write("\n")

        data.append("Backgrounds/Textures,Nature")
        data.append("no")
        data.append("no")
        data.append("yes")
        multi_data.append(data)


filename = "images.csv"

# Open a new CSV file in write mode
with open(filename, "w", newline="") as csvfile:
    # Create a CSV writer object
    writer = csv.writer(
        csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )

    # Write the header row
    writer.writerow(
        [
            "Filename",
            "Description",
            "Keywords",
            "Categories",
            "Editorial",
            "Mature content",
            "illustration",
        ]
    )

    # Write the data rows
    for row in multi_data:
        writer.writerow(row)


# Open the file for reading
with open(filename, "r") as file:

    # Read the contents of the file
    contents = file.read()

    # Replace the characters
    contents = contents.replace('"""', "")

# Open the same file for writing
with open(filename, "w") as file:

    # Write the modified contents back to the file
    file.write(contents)
