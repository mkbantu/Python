from rembg import remove
from PIL import Image
import io

# Read the original image
with open("kagarama.jpg", "rb") as f:
    input_data = f.read()

# Remove the background
output_data = remove(input_data)

# Open the transparent image
img = Image.open(io.BytesIO(output_data)).convert("RGBA")

# Create a white background
white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
white_bg.paste(img, (0, 0), img)

# Save the final image
white_bg.convert("RGB").save("kagarama_white_bg.jpg")

print("Background removed and replaced with white.")