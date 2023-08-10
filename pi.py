import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

N_values = np.arange(1000) + 1
constants = {"pi": np.pi, "e": np.e, "sqrt2": np.sqrt(2)}

# Create a list of the digits 0-9
digits = np.arange(10)

plt.figure(figsize=(8, 4))

for const_name, const_value in constants.items():
    with open(f"constants/{const_name}.txt", "r") as file:
        const_digits = file.read().strip()

    values = []
    for n in N_values:
        # Count the number of times each digit appears in const_digits
        counts = [const_digits[:n].count(str(digit)) for digit in digits]
        values.append((np.max(counts) - np.min(counts)) / (n / 10))

    plt.plot(N_values, values, label=const_name)

plt.xlabel("N")
plt.ylabel("Difference")
plt.title("Difference Between Digits Counts")
plt.legend()
plt.tight_layout()
plt.show()

"""
# Plotting
plt.bar(digits, counts)
plt.xlabel("Digit")
plt.ylabel("Count")
plt.title(f"Digit Counts in the First {N_values[-1]} Digits of Pi")
plt.show()
"""

"""
# Calculate the dimensions of the image based on the number of digits
total_digits = len(pi_digits)
width = int(math.sqrt(total_digits))
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
image.save("pi.png")
"""
