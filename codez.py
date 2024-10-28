# Python Basics

# 1. Print Statement
# `print()` is used to display information in the console
print("Hello, World!")  # Outputs: Hello, World!

# 2. Variables
# Variables are used to store information that can be reused later.
name = "Alice"  # String variable
age = 25        # Integer variable
height = 5.6    # Float variable

# Display the variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)

# 3. Data Types
# Python has several built-in data types. Here are a few common ones:
my_string = "Hello, Python!"     # String
my_integer = 10                  # Integer
my_float = 3.14                  # Float
my_boolean = True                # Boolean
my_list = [1, 2, 3, 4, 5]        # List
my_tuple = (1, 2, 3)             # Tuple (immutable)
my_dict = {"name": "Alice", "age": 25}  # Dictionary (key-value pairs)

# 4. Basic Math Operations
# You can perform math operations like addition, subtraction, etc.
x = 10
y = 3
print("Addition:", x + y)          # Outputs: 13
print("Subtraction:", x - y)       # Outputs: 7
print("Multiplication:", x * y)    # Outputs: 30
print("Division:", x / y)          # Outputs: 3.333...
print("Integer Division:", x // y) # Outputs: 3 (floors the result)
print("Modulus:", x % y)           # Outputs: 1 (remainder of division)
print("Exponent:", x ** y)         # Outputs: 1000 (10 raised to power 3)

# 5. Conditional Statements
# Conditional statements (if, elif, else) are used to make decisions.
number = 15
if number > 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is exactly 10")
else:
    print("Number is less than 10")

# 6. Loops
# `for` loops allow you to iterate over a sequence (like a list)
for i in range(5):  # range(5) gives [0, 1, 2, 3, 4]
    print("Loop iteration:", i)

# `while` loop repeats as long as a condition is true
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Same as count = count + 1

# 7. Functions
# Functions allow you to encapsulate code for reuse
def greet(name):
    """Function to greet a person with their name."""
    print("Hello,", name)

greet("Alice")  # Calls the function with "Alice" as the argument

# 8. Lists (Arrays)
# Lists store multiple items in a single variable
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adds "orange" to the list
print("Fruits:", fruits)

# 9. Dictionary Operations
# Access values in a dictionary by key
print("Name from dictionary:", my_dict["name"])
my_dict["age"] = 26  # Update the age value
print("Updated dictionary:", my_dict)

# 10. Exception Handling
# Use try-except to handle errors gracefully
try:
    result = 10 / 0  # This will raise a division by zero error
except ZeroDivisionError:
    print("You can't divide by zero!")

# 11. Importing Libraries
# You can import libraries to extend Python's capabilities
import math
print("Square root of 16 is:", math.sqrt(16))  # Outputs: 4.0
