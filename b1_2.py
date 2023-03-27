### RUN 1 cmd
# FOR /L %i IN (1,1,10) DO start "python" /B python b1_2.py %i
### RUN multi cmd
# FOR /L %i IN (1,1,10) DO start cmd /k python b1_2.py %i

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
import sys


def convert_name(s):
    s = " ".join(s.split("("))
    s = " ".join(s.split(")"))
    s = s.lower()
    s = s.replace("  ", "_")
    s = s.replace(" ", "_")
    if s[-1] == "\n":
        s = s[:-1]
    if s[-1] == ".":
        s = s[:-1]
    return s


def find_common_element(file_name, all_name):
    common_element = ""
    for x, y in zip(file_name, all_name):
        if x == y:
            common_element += x
        else:
            break
    return common_element


def find_most_common_element(file_names, all_name):
    most_common = ""
    max_length = 0
    for file_name in file_names:
        common_element = find_common_element(file_name, all_name[: len(file_name)])
        if len(common_element) > max_length:
            most_common = file_name
            max_length = len(common_element)
    return most_common


dir_get = "txt_n"
# choose_file = int(input("choose name folder save: "))
choose_file = int(sys.argv[1])

download_dir = f"C:/Users/BTTB/Downloads/{str(choose_file)}"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

sleep(10 * choose_file)

driver = webdriver.Chrome("W:/Document/chromedriver_win32/chromedriver.exe")

driver.get("chrome://settings/downloads")

sleep(10)

driver.get("https://skybox.blockadelabs.com/")
sleep(8)
name = 0
init_length = len(os.listdir(download_dir))

list_selected = [
    "Fantasy Landscape",
    "Anime Art Style",
    "Surreal Style",
    "Digital Painting",
    "Scenic",
    "Realistic",
    "SciFi",
    "Dreamlike",
    "Interior Views",
    "Sky",
    "Dutch Masters",
    "Infrared (Experimental Nature Scenes)",
]

# list_selected = [
#     "Digital Painting",
#     "Dutch Masters",
# ]


with open(dir_get + f"/image_{choose_file}.txt", "r", encoding="utf-8") as read_file:
    content = read_file.readlines()

mycontent = []

for c in content:
    mycontent.append(c)
already_use = []
for mc in mycontent:
    print("mc: ", mc)

    # for i in range(1, 16):
    input_element = WebDriverWait(driver, 1000).until(
        EC.visibility_of_element_located((By.NAME, "prompt"))
    )
    already_input = 0
    while True:
        try:
            input_element.clear()
            input_element.send_keys(mc)
            already_input = 1
            break
        except:
            print("error input")
    if already_input == 1:
        already_use.append(mc)
        with open(
            dir_get + f"/image_{choose_file}.txt", "w", encoding="utf-8"
        ) as write_file:
            for mc1 in mycontent:
                if mc1 not in already_use:
                    write_file.write(mc1)

        # with open(f"allimage.txt", "a", encoding="utf-8") as write_file:
        #     write_file.write(mc)
        #     write_file.write("\n")

        # dropdown = WebDriverWait(driver, 100).until(
        #     EC.visibility_of_element_located((By.NAME, "styleId"))
        # )

        for ls in list_selected:
            # try:

            select_element = driver.find_element(By.NAME, "styleId")
            # Select the second option (index starts from 0)
            already_select = 0
            while True:
                try:
                    select_element.click()
                    already_select = 1
                    break
                except:
                    pass
            if already_select == 1:
                select = Select(select_element)
                already_select2 = 0

                while True:
                    try:
                        select.select_by_visible_text(ls)
                        already_select2 = 1
                        break
                    except:
                        pass
                if already_select2 == 1:
                    # Wait for the button to be clickable
                    generate_button = WebDriverWait(driver, 1000).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, '//button[text()="Generate"]')
                        )
                    )
                    already_generate = 0
                    while True:
                        try:
                            generate_button.click()
                            already_generate = 1
                            break
                        except:
                            pass
                    if already_generate == 1:
                        already_download = 0
                        while True:
                            try:
                                # Wait for the download button to be clickable for up to 10 seconds
                                wait = WebDriverWait(driver, 1000)
                                download_button = wait.until(
                                    EC.element_to_be_clickable(
                                        (
                                            By.XPATH,
                                            '//button[contains(span, "Download image")]',
                                        )
                                    )
                                )

                                # Click the download button
                                download_button.click()
                                already_download = 1

                            except:
                                print("Error download")
                                continue
                            if already_download == 1:
                                # Check the current length of the download directory
                                sleep(5)
                                current_length = len(os.listdir(download_dir))
                                print("Pass: ", current_length, init_length)

                                if current_length > init_length:
                                    init_length += 1
                                    first_name = convert_name(ls)
                                    if first_name[-1] != "_":
                                        first_name += "_"
                                    last_name = convert_name(mc)
                                    all_name = first_name + last_name
                                    print("all_name: ", all_name)
                                    file_names = []
                                    for dr in glob.glob(download_dir + "/*"):
                                        file_name = os.path.basename(dr)[:-4]
                                        file_names.append(file_name)
                                    file_name = find_most_common_element(
                                        file_names, all_name
                                    )
                                    print("file_name: ", file_name)
                                    try:
                                        os.rename(
                                            download_dir + "/" + file_name + ".jpg",
                                            download_dir + "/" + all_name + ".jpg",
                                        )
                                    except:
                                        pass
                                    break
            # except Exception as e:
            #     print("error: ", e)
            #     pass

        # except:

        #     sleep(2)
        #     pass
