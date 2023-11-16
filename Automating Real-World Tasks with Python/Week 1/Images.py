# doc https://pillow.readthedocs.io/en/stable/reference/Image.html

from PIL import Image
from os import listdir

src_dir = "/workspaces/CourseraPython/Automating Real-World Tasks with Python/Week 1/images/"
new_dir = "/workspaces/CourseraPython/Automating Real-World Tasks with Python/Week 1/processed_images/"

im = Image.open(src_dir+"bridge.jpg")
im.rotate(90).resize((63,120)).save(new_dir + "bridge_resized.jpg")
