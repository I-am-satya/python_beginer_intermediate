# 02_list_operations.py
"""
List Operations in Python
--------------------------
This file covers essential list operations, commonly asked in interviews and useful for beginners.
"""

# 1. Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = list(range(1, 6))
mixed = [1, "apple", 3.14, True]
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# 2. Accessing elements
print("First fruit:", fruits[0])
print("Last number:", numbers[-1])

# 3. List slicing
print("Slice (1:3):", fruits[1:3])

# 4. Modifying elements
fruits[0] = "mango"
print("After modification:", fruits)

# 5. Adding elements
fruits.append("orange")
print("After append:", fruits)
fruits.insert(1, "grape")
print("After insert:", fruits)

# 6. Removing elements
fruits.remove("grape")
print("After remove:", fruits)
removed_item = fruits.pop()
print("After pop (removed {}):".format(removed_item), fruits)

# 7. List concatenation and repetition
more_fruits = ["kiwi", "pineapple"]
all_fruits = fruits + more_fruits
print("Concatenated list:", all_fruits)
print("Repetition:", fruits * 2)

# 8. Membership testing
print("Is 'banana' in fruits?", "banana" in fruits)

# 9. Iterating a list
for fruit in fruits:
    print(fruit)

# 10. List comprehension
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# 11. Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print("Matrix[1][1]:", matrix[1][1])

# 12. Sorting and reversing
numbers = [3, 1, 4, 2, 5]
numbers.sort()
print("Sorted numbers:", numbers)
numbers.reverse()
print("Reversed numbers:", numbers)

# 13. Removing duplicates
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print("Unique numbers:", unique)

# 14. Flatten a nested list
nested = [[1, 2], [3, 4], [5]]
flattened = [num for sublist in nested for num in sublist]
print("Flattened list:", flattened)

# 15. Practice Problem 1: Find second largest element
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

print("Second largest:", second_largest([5, 3, 1, 4, 5, 3]))

# 16. Practice Problem 2: Remove all occurrences of an element
def remove_all_occurrences(lst, val):
    return [x for x in lst if x != val]

print("Removed 3s:", remove_all_occurrences([1, 3, 3, 2, 3, 4], 3))
