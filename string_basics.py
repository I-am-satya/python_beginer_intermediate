# 01_strings_basics.py
"""
String Basics in Python
------------------------
This file covers essential string operations in Python, ideal for beginners and interview preparation.
"""

# 1. Creating strings
s1 = "Hello"
s2 = 'World'
s3 = '''Multiline
String'''
print(s1, s2)

# 2. Indexing and slicing
print("First character:", s1[0])
print("Last character:", s1[-1])
print("Slice (0:3):", s1[0:3])

# 3. Immutability (this will raise an error if uncommented)
# s1[0] = 'h'  # Strings are immutable

# 4. String methods
sample = "  python programming  "
print("Upper:", sample.upper())
print("Lower:", sample.lower())
print("Title:", sample.title())
print("Stripped:", sample.strip())
print("Replaced:", sample.replace("python", "java"))

# 5. String concatenation and repetition
print("Concat:", s1 + " " + s2)
print("Repetition:", s1 * 3)

# 6. Membership and looping
print("'p' in sample:", 'p' in sample)
for char in s1:
    print(char, end=" ")
print()

# 7. String formatting
name = "Satya"
age = 25
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

# 8. Splitting and joining
csv = "apple,banana,cherry"
fruits = csv.split(',')
print("Split:", fruits)
print("Join:", "; ".join(fruits))

# 9. Practice Problem 1: Palindrome check
def is_palindrome(word):
    return word == word[::-1]

print("Palindrome check for 'madam':", is_palindrome("madam"))

# 10. Practice Problem 2: Anagram check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print("Anagram check for 'listen' and 'silent':", is_anagram("listen", "silent"))

# 11. Practice Problem 3: Character frequency
from collections import Counter
word = "hello world"
freq = Counter(word.replace(" ", ""))
print("Character frequency:", freq)
