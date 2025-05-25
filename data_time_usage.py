# 07_datetime_usage.py
"""
Using Python's datetime Module
------------------------------

This script demonstrates how to work with dates and times using
the built-in datetime module.
"""

import datetime

# Get current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Access individual components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Format date and time as string
print("Formatted date (DD-MM-YYYY):", now.strftime("%d-%m-%Y"))
print("Formatted time (HH:MM:SS):", now.strftime("%H:%M:%S"))

# Display full weekday and month name
print("Weekday:", now.strftime("%A"))  # e.g., Monday
print("Month name:", now.strftime("%B"))  # e.g., May

# Create a specific date object
birthday = datetime.datetime(1990, 12, 25)
print("Birthday:", birthday.strftime("%d %B %Y"))

# Calculate difference between two dates
delta = now - birthday
print(f"Days since birthday: {delta.days}")

# Additional formatting examples
print("ISO format:", now.isoformat())
print("Date as MM/DD/YY:", now.strftime("%m/%d/%y"))

"""
Summary:
- Use datetime.datetime.now() to get current date/time.
- Use strftime() to format dates/times as strings.
- You can calculate differences between dates using subtraction.
"""

