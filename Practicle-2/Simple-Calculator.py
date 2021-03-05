# Author: Frazer Mills
# Date: 05/03/21
# program name: 'Simple-Calculator.py'
# Python 3.9.2
# Description: This program is a simple calculator that takes two numbers and performs an operation chosen by the user.

# ------------------------------------ Initialising variables ------------------------------------ #
num1 = 0
num2 = 0
result = 0
operator = None
menu = """
Which operator would you like:
1. Subtract
2. Multiply
3. Divide
4. Add
Input operator: """

# --------------------------------------- Takes user input --------------------------------------- #
num1 = int(input("Input number 1: "))
num2 = int(input("Input number 2: "))

operator = int(input(menu))

# -------------------------------- Selects which calculation to do ------------------------------- #
if operator == 1:
    result = num1 - num2
    
elif operator == 2:
    result = num1 * num2
    
elif operator == 3:
    result = num1 / num2
    
elif operator == 4:
    result = num1 + num2

else:
    print("That was an illegal input, please try again")

# ----------------------------------- Outputs result to console ---------------------------------- #
print(result if result else "No result caculated")
