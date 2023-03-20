from PIL import Image
import glob
import os

path = "3/*.png"
for p in glob.glob(path):
    image = Image.open(p)
    width, height = image.size
    image.close()

    # Check if image is smaller than 200x200 pixels
    if width < 200 or height < 200:
        os.remove(p)
