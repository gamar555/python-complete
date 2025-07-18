# # Declares your name, age and learning status..
# name = "amar"
# age = 23
# is_learning = "Python And Data Science"

# print(f"My name is {name}\nI'm {age} years old \nI'm {is_learning}")
      

# # Calculate your age in months and days
# age_in_months = age * 12
# age_in_days = age * 365
# print(f"I am {age_in_months} months old and {age_in_days} days old.")


# #Swaps two numbers and returns the result
# def swap_numbers(a, b):
#     return b, a
# # Example usage of swap_numbers
# num1 = 5
# num2 = 10
# swapped_num1, swapped_num2 = swap_numbers(num1, num2)
# print(f" Swapped numbers: {swapped_num1} and {swapped_num2}")



# # user input swapping
def swap_numbers(a, b):
    return b, a
def swap_user_input():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number:"))
    a, b = swap_numbers(a, b)
    print(f"Swapped numbers: {a} and {b}")
# Uncomment the line below to run user input swapping
swap_user_input()




# Uses a constant for pi and calculates the area of a circle
PI = 3.14
def calculate_circle_area(radius):
    return PI * radius * radius
# Example usage of calculate_circle_area
radius = 5
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area}")
