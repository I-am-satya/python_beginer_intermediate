# 08_frequency_counter.py
"""
Simple Character Frequency Counter
-----------------------------------

Counts how many times each character appears in the input string using two methods:
1. Using a dictionary with a simple loop.
2. Using the built-in collections.Counter for convenience.
"""

# Input from user
input_str = input("Enter a string: ")

# Method 1: Using dictionary
frequency = {}
for char in input_str:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nCharacter frequencies using dictionary:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

# Method 2: Using collections.Counter
from collections import Counter
counter_freq = Counter(input_str)

print("\nCharacter frequencies using collections.Counter:")
for char, count in counter_freq.items():
    print(f"'{char}': {count}")
