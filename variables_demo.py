# GitHub-Ready Python File: Variables in Python (Beginner to Advanced)
# Author: Amarjeet
# Description: This script demonstrates the usage of variables in Python,
# including declaration, arithmetic operations, swapping, user input, and constants.

# -------------------------------
# Section 1: Declaring Variables
# -------------------------------
name = "amar"
age = 23
is_learning = "Python And Data Science"

# Print basic information using f-string formatting
print(f"My name is {name}\nI'm {age} years old\nI'm learning {is_learning}")

# -----------------------------------------------
# Section 2: Calculate Age in Months and Days
# -----------------------------------------------
age_in_months = age * 12
age_in_days = age * 365  # Approximate calculation

print(f"I am {age_in_months} months old and {age_in_days} days old.")

# -----------------------------------------------
# Section 3: Swapping Two Numbers (Static)
# -----------------------------------------------
def swap_numbers(a, b):
    """Function to swap two numbers."""
    return b, a

# Example usage of swap_numbers
num1 = 5
num2 = 10
swapped_num1, swapped_num2 = swap_numbers(num1, num2)
print(f"Swapped numbers (static): {swapped_num1} and {swapped_num2}")

# ---------------------------------------------------
# Section 4: Swapping Two Numbers (User Input)
# ---------------------------------------------------
def swap_user_input():
    """Function to swap two numbers entered by the user."""
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    a, b = swap_numbers(a, b)
    print(f"Swapped numbers (user input): {a} and {b}")

# Uncomment the line below to enable user input swapping
# swap_user_input()

# ---------------------------------------------------
# Section 5: Calculate Area of Circle Using Constant
# ---------------------------------------------------
PI = 3.14  # Constant value for Pi

def calculate_circle_area(radius):
    """Function to calculate the area of a circle."""
    return PI * radius * radius

# Example usage of calculate_circle_area
radius = 5
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area}")
