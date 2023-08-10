import numpy as np
import matplotlib.pyplot as plt

N = 100
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
radii = np.arange(1, N + 1)

ax = plt.subplot(111, polar=True)
ax.set_title("Natural numbers in polar coordinates")

for angle, radius in zip(angles, radii):
    color = plt.cm.viridis(radius / N)
    ax.bar(angle, radius, width=0.2, bottom=0, alpha=0.7, color=color)

plt.show()
