import numpy as np
import matplotlib.pyplot as plt

real_part = float(input("Enter the real part: "))
imag_part = float(input("Enter the imaginary part: "))
n = int(input("How many roots? "))

complex_number = complex(real_part, imag_part)

# Calculate n-th roots
root_magnitude = np.abs(complex_number) ** (1 / n)
roots = []
for k in range(n):
    angle = np.angle(complex_number)
    root = root_magnitude * (
        np.cos((angle + 2 * np.pi * k) / n) + 1j * np.sin((angle + 2 * np.pi * k) / n)
    )
    roots.append(root)

# Plotting...
fig, ax = plt.subplots()
ax.scatter(np.real(roots), np.imag(roots), color="blue", marker="o")

# Connect the roots to form a polygon
roots = np.append(roots, roots[0])  # Repeat the first root to close the polygon
ax.plot(np.real(roots), np.imag(roots), color="green")

# Plot the unit circle
unit_circle = plt.Circle((0, 0), root_magnitude, color="red", fill=False)
ax.add_artist(unit_circle)

# Set plot limits and aspect ratio
ax.set_xlim(-1.5 * root_magnitude, 1.5 * root_magnitude)
ax.set_ylim(-1.5 * root_magnitude, 1.5 * root_magnitude)
ax.set_aspect("equal", adjustable="datalim")

# Print roots
for i, root in enumerate(roots[:-1]):
    print(f"Root {i + 1}: {root}")

# Axes labels
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_title(f"Roots of {complex_number}")
plt.show()
