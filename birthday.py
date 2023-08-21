import numpy as np
import matplotlib.pyplot as plt

irrationals = ["π", "e", "φ", "√2"]

birthday = input("Enter your birthday in DDMM format: ")
print(f"Searching for {birthday}...")

for num in irrationals:
    with open(f"constants/{num}.txt", "r") as file:
        decimals = file.read().strip()

    if birthday in decimals:
        print(f"Found after {decimals.index(birthday)} digits of {num}")
    else:
        print(f"Not found in the first {len(decimals)} digits of {num}")
