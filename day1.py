# day1.py
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are eligible to vote.")
else:
    print(f"Sorry {name}, you are too young to vote.")

def greet(person):
    return f"Welcome, {person}!"

print(greet(name))
