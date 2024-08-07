"""
> Exercise 1

Create a program that receives two numbers from the user and multiplies them.
Use the provided functions.
"""


def ReadInput():
    print(
        "Input two numbers, this application returns the result of their multiplication."
    )
    num1 = input("num1: ")
    num2 = input("num2: ")
    CalculateAndPrint(num1, num2)


def CalculateAndPrint(num1, num2):
    result = float(num1) * float(num2)
    print(f"result: {result}")


ReadInput()
