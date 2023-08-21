import numpy as np
import matplotlib.pyplot as plt

precision = np.arange(500) + 1
digits = np.arange(10)
irrational_numbers = ["π", "e", "φ", "√2"]

plt.figure(figsize=(8, 4))

for number in irrational_numbers:
    with open(f"constants/{number}.txt", "r") as file:
        decimals = file.read().strip()

    differences = []
    for p in precision:
        counts = [decimals[:p].count(str(digit)) for digit in digits]
        diff = np.sum(np.abs(counts - np.average(counts))) / (p / 10)
        differences.append(diff)

    plt.plot(precision, differences, label=number)

plt.xlabel("Decimal Precision")
plt.ylabel("Difference between Digit Frequencies")
plt.title("Difference between Digit Frequencies of Irrational Numbers")
plt.legend()
plt.tight_layout()
plt.show()

# 2nd plot
plt.bar(digits, counts)
plt.xlabel("Digit")
plt.xticks(digits)
plt.ylabel("Frequency")
plt.title(f"Digit Frequencies of {irrational_number}")
plt.show()
