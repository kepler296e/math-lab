import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

with open("constants/π.txt", "r") as file:
    pi_digits = file.read().strip()

pi_digits = pi_digits[:1000000]

# Calculate the dimensions of the image based on the number of digits
total_digits = len(pi_digits)
width = int(np.sqrt(total_digits))
height = (total_digits + width - 1) // width

# Create a blank image
image = Image.new("RGB", (width, height))

# Convert each digit to a vibrant color and set pixel in the image
for i, digit in enumerate(pi_digits):
    color_value = int(digit) * 50
    r = (color_value * 11) % 255
    g = (color_value * 12) % 255
    b = (color_value * 13) % 255
    x = i % width
    y = i // width
    image.putpixel((x, y), (r, g, b))

# Save the image
image.save("images/pi.png")
