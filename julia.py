import matplotlib.pyplot as plt
import numpy as np


def julia(x, y, c, max_iterations):
    z = complex(x, y)
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return 0


width = 1000
height = 1000
max_iterations = 50

real_range = (-1.5, 1.5)
imag_range = (-1.5, 1.5)

c = complex(-0.62772, -0.42193)

img = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        x = real_range[0] + (real_range[1] - real_range[0]) * j / width
        y = imag_range[0] + (imag_range[1] - imag_range[0]) * i / height
        img[i, j] = julia(x, y, c, max_iterations)

plt.figure(figsize=(8, 8))
plt.imshow(img, cmap="inferno")
plt.show()
