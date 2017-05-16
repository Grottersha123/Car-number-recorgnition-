from PIL import Image
from pytesseract import image_to_string


image_file = Image.open(r'D:\Git_project\VKR\Pytesser\fnord.tif')
print("df")
print(image_to_string(image_file))