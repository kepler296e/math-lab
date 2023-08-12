import numpy as np
import matplotlib.pyplot as plt

precision = np.arange(500) + 1
digits = np.arange(10)
constants = {"π": np.pi, "e": np.e, "√2": np.sqrt(2), "φ": (1 + np.sqrt(5)) / 2}

plt.figure(figsize=(8, 4))

for const_name, const_value in constants.items():
    with open(f"constants/{const_name}.txt", "r") as file:
        const_digits = file.read().strip()

    differences = []
    for p in precision:
        counts = [const_digits[:p].count(str(digit)) for digit in digits]
        avg = np.average(counts)
        diff = np.sum(np.abs(counts - avg)) / (p / 10)
        differences.append(diff)

    plt.plot(precision, differences, label=const_name)

plt.xlabel("Precision (Number of Digits Considered)")
plt.ylabel("Digit Count Variation")
plt.title("Convergence of Digit Frequencies")
plt.legend()
plt.tight_layout()
plt.show()

# 2nd plot
plt.bar(digits, counts)
plt.xlabel("Digit")
plt.xticks(digits)
plt.ylabel("Count")
plt.title(f"Digit Frequencies of {const_name}")
plt.show()
