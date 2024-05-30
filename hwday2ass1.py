# Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

number = int(input("Enter a number: ")) # Convert the input to an integer

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")

# The big error is that the input is a string and not an integer.

# Task 2: Identify the Greatest Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(f"The largest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")

