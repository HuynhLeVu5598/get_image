import os
import glob

download_dir = "W:/vu/khac/image/publish/"

for do in glob.glob(download_dir + "*.jpg"):
    # Assume filename contains the name of the downloaded image file
    base_name, ext = os.path.splitext(do)
    text_file_name = base_name + ".txt"

    # Create the text file with the same name as the downloaded image file
    with open(os.path.join(download_dir, text_file_name), "w") as f:
        f.write("0 0.1 0.2 0.3 0.4")


with open(os.path.join(download_dir, "classes.txt"), "w") as f:
    f.write("a")
