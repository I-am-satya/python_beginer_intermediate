# 03_pan_validation.py
"""
PAN Card Validation
---------------------
This script validates Indian PAN card numbers.
PAN Format: 5 uppercase letters, 4 digits, 1 uppercase letter (e.g., ABCDE1234F)
"""

def is_valid_pan(pan):
    if len(pan) != 10:
        return False
    if not (pan[:5].isalpha() and pan[:5].isupper()):
        return False
    if not (pan[5:9].isdigit()):
        return False
    if not (pan[9].isalpha() and pan[9].isupper()):
        return False
    return True

# Input from user
pan_input = input("Enter PAN number to validate: ").strip()

if is_valid_pan(pan_input):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")

# Sample runs
# Input: ABCDE1234F  => Valid PAN Number
# Input: ABC1234FDE  => Invalid PAN Number

# Explanation:
# 1. First 5 characters must be uppercase alphabets.
# 2. Next 4 characters must be digits.
# 3. Last character must be an uppercase alphabet.
