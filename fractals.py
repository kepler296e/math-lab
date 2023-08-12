import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def mandelbrot(c, max_iterations):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z**2 + c
        n += 1
    return n


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

real_range = [(-2, 1), (-1.5, 1.5)]
imag_range = [(-1, 1), (-1.5, 1.5)]

julia_c = complex(-0.62772, -0.42193)

img = np.zeros((2, height, width))

k = 1
# for k in range(2):
for i in range(height):
    for j in range(width):
        x = real_range[k][0] + (real_range[k][1] - real_range[k][0]) * j / width
        y = imag_range[k][0] + (imag_range[k][1] - imag_range[k][0]) * i / height
        if k == 0:
            c = complex(x, y)
            img[k][i, j] = mandelbrot(c, max_iterations)
        else:
            img[k][i, j] = julia(x, y, julia_c, max_iterations)

# Creating a custom colormap for better visualization
colors = [
    (1, 1, 1),
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 1),
    (0, 1, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 0, 0),
]
cmap = LinearSegmentedColormap.from_list("custom_cmap", colors, N=max_iterations)


"""Plot Mandelbrot"""
# Create the main figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

# Plot the full Mandelbrot set in the first subplot
img1 = ax1.imshow(
    img[0],
    cmap=cmap,
    extent=[real_range[0][0], real_range[0][1], imag_range[0][0], imag_range[0][1]],
)
plt.colorbar(img1, ax=ax1, label="Iterations", orientation="vertical")
ax1.set_title("Mandelbrot Set")
ax1.set_xlabel("Real")
ax1.set_ylabel("Imaginary")
ax1.grid(False)

# Plot a zoomed-in view in the second subplot
zoom_real = (-2, -1)
zoom_imag = (-0.4, 0.4)
zoom_img = img[0][
    int(
        (zoom_imag[0] - imag_range[0][0])
        * height
        / (imag_range[0][1] - imag_range[0][0])
    ) : int(
        (zoom_imag[1] - imag_range[0][0])
        * height
        / (imag_range[0][1] - imag_range[0][0])
    ),
    int(
        (zoom_real[0] - real_range[0][0])
        * width
        / (real_range[0][1] - real_range[0][0])
    ) : int(
        (zoom_real[1] - real_range[0][0])
        * width
        / (real_range[0][1] - real_range[0][0])
    ),
]
ax2.imshow(zoom_img, cmap=cmap, extent=[*zoom_real, *zoom_imag])
ax2.set_title("Zoomed-in View")
ax2.set_xlabel("Real")
ax2.set_ylabel("Imaginary")
ax2.grid(False)

# Display the plot
plt.tight_layout()
plt.show()

"""Plot Julia"""
plt.figure(figsize=(10, 10))
plt.imshow(img[1], cmap="inferno")
# plt.colorbar(label="Iterations", orientation="vertical")
plt.title("Julia Set")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.show()
