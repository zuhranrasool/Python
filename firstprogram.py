# ---------------------------------------------
# Program 1: Addition of two numbers
# ---------------------------------------------

# Using variables makes the code readable and easy to modify
a = 5
b = 10

# Calculating the sum
total_sum = a + b

# Displaying the result using formatted output
print(f"The sum of {a} and {b} is {total_sum}")


# ---------------------------------------------
# Program 2: Palindrome Number Checker
# ---------------------------------------------

# Taking input from the user
# Input is taken as a string to easily reverse it
num = input("Enter a number to check if it is a palindrome: ")

# Checking if the original string is equal to its reverse
if num == num[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
