# This is a  basic Python  script with comments to explain each part

# Print a greeting message
print("Hello to python  world") # opt : hello  to  python  world
# ----------------------------------------------

# Define a variable and assign a value
name = "Alice"  # Variable 'name' holds the string "Alice"

print(f"Hello, {name}!")  # Output: Hello, Alice!


# ----------------------------------------------

# Perform a basic arithmetic operation
a = 10  # Assign 10 to variable 'a'
b = 5   # Assign 5 to variable 'b'
sum_result = a + b  # Add 'a' and 'b' and store the result in 'sum_result'

print(f"the sun  of {a} and b  is  {sum_result}") # Output: The sum of 10 and 5 is 15
# ----------------------------------------------

# Define a simple function
def  greet_msg(name) :
    """This functions greets a  user with  name  attribute"""
    print(f"welcome, {name}" )  # Output: Welcome, <name>!
greet_msg("Bob")  # Output: Welcome, Bob!

# ----------------------------------------------


# Use a loop to print numbers from 1 to 5
for i in range (1,6) :
    print(i)  # Output: 1 2 3 4 5 (each number on a new line)


# using conditional statements
if  a > b : 
    print(f"{a} is  greater  than {b}") # output : 10 is  greater than  5
