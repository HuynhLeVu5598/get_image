import glob
import os

# if down by roboflow
for filename in glob.glob("test1/*.jpg"):
    index1 = filename.rfind("_")

    new_filename = filename[:index1] + ".jpg"
    if new_filename[-3:-1] == "-1-":
        new_filename = new_filename[:-3]

    os.rename(filename, new_filename)
