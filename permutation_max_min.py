# 04_permutations_max_min.py
"""
Permutations - Find Maximum and Minimum Numbers
-------------------------------------------------
Given a list of digits, this script generates all possible permutations,
then finds the maximum and minimum numbers formed by concatenating the digits.
"""

from itertools import permutations

def max_min_permutation(nums):
    # Generate all permutations of the input list
    permuts = permutations(nums)
    
    # Convert each permutation tuple to an integer
    numbers = [int(''.join(map(str, p))) for p in permuts]
    
    # Find maximum and minimum number from permutations
    max_num = max(numbers)
    min_num = min(numbers)
    
    return max_num, min_num

# Input list from user (space separated integers)
nums = list(map(int, input("Enter digits separated by space: ").split()))

max_number, min_number = max_min_permutation(nums)

print(f"Maximum number from permutations: {max_number}")
print(f"Minimum number from permutations: {min_number}")

# Example:
# Input: 1 2 3
# Output:
# Maximum number from permutations: 321
# Minimum number from permutations: 123
