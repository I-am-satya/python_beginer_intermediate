"""Day1:- Introduction and setup your programming journey"""
"""
1,wap to calulate area of a rectangle given its length and width
"""
# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# Area_of_rectange = length * width 
# print(f"Area of rectagle with length {length} and width {width} is : {Area_of_rectange} squeare units")



"""
# 2, Create a program that takes a user's name and age as input and prints a greeting message
"""
# user_name = input("Enter username: ")
# age = input("Enter age: ")
# greeting_message = f"Hello, {user_name}! You are {age} years old!\nHave a great day ahead."
# print(greeting_message)

"""
# 3, Write a program to check if a number is even or odd
"""
# num = int(input("Enter a number to check the num is even or odd: "))
# if num % 2 == 0:
#     print(f"Given num {num} is Even")
# else:
#     print(f"Given num {num} is odd")

"""
# 4, Given a list of numbers, find the maximum and minimum values
"""

# list_of_numbers = [1, 3, 4, 2, 1, 3, 6, 7, 8, 9, 12, 13, 14, 52, 25, 76, 58, 90, 99]
"""### using built in methods"""
# minimum = min(list_of_numbers)
# maximum = max(list_of_numbers)
# print(f"minimum value from list_of_numbers is {minimum}")
# print(f"maximum value from list_of_numbers is {maximum}")
"""### using sorting and without using built in methods"""
# for i in range(len(list_of_numbers)):
#     for j in range(i-1):
#         if list_of_numbers[j] > list_of_numbers[j+1]:
#             list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
# n = len(list_of_numbers)
# print(n)
# print(f"Minimum value from list_of_numbers is : {list_of_numbers[0]}")
# print(f"Maximum value from list_of_numbers is : {list_of_numbers[n - 1]}")
# print(f"Second Maximum value from list_of_numbers is : {list_of_numbers[n - 2]}")
# print(f"Third Maximum value from list_of_numbers is : {list_of_numbers[n - 3]}")

"""
# 5, Create a Python function to check if a given string is a palindrome
"""
# def palindrome(name):
#     if name == name[::-1]:
#         return f"Given {name} is palindrome"
#     else:
#         return f"Given {name} is not a palindrome"
        
# string = input("Enter the string you want to check weather it is palindrome or not : ")
# print(palindrome(string))

"""
# 6, Calculate the compound interest for a given principal amount, interest rate, and time period
"""
# def calculate_CI():
#     pass

"""
# 7, Write a program that converts a given number of days into years, weeks, and days
"""
# def days_to_years_weeks_days(days):
#     total_days_year = 365 
#     total_days_week = 7 
    
#     years = round(days / total_days_year)
#     remaining_days = days % total_days_year
#     weeks = remaining_days // total_days_week
#     remaining_days_left = remaining_days % total_days_week
#     return years, weeks, remaining_days_left

# print(days_to_years_weeks_days(500)) # (years, weeks,days)


"""
# 8, Given a list of integers, find the sum of all positive numbers
"""

# list_of_integers = [-1, 1, 0, 2, 5, 7, 8, 9, 1, 2, -10, -7, -8, -4, -3]
# positive_integers = []
# negative_integers = []
# for num in list_of_integers:
#     if num > 0:
#         positive_integers.append(num)
#     else:
#         negative_integers.append(num)

# print(f"Positive Integers sum: {sum(positive_integers)}")
# print(f"Negative Integers Sum: {abs(sum(negative_integers))}") # using abs converted -ve integer to +ve integer.

"""
# 9, Create a program that takes a sentence as input and counts the number of words in it
"""
# sentence = "Hello world hello again i mean hello to everyone in the world again"
# sentence = sentence.lower().split(" ")
# word_count = {}
# for word in sentence:
#     if word in word_count:
#         word_count[word] += 1 
#     else:
#         word_count[word] = 1 
# print(word_count)

"""
# 10, Implement a program that swaps the values of two variables
"""
# value1 = 1000 
# value2 = 2000
# print(f"Values before swap: {value1, value2}")
# value1, value2 = value2, value1
# print(f"Values After swap: {value1, value2}")

