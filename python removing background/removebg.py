from rembg import remove 
from PIL import Image

input=Image.open("./225029152.jpg")
output=remove(input)

output.save("./225029152_no_bg.png")