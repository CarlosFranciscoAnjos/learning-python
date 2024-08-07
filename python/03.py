"""
> Exercise 3

Create a program that iterates through a list of numbers printing each one and then returns their sum.
Use the provided functions.
"""


def SumAndPrint(numbers):
    pass


# Unit tests
assert SumAndPrint([1, 2, 3]) == 6, "Test case 1 failed"
assert SumAndPrint([-1, 1, 5]) == 5, "Test case 2 failed"
assert SumAndPrint([0]) == 0, "Test case 3 failed"
assert SumAndPrint([]) == 0, "Test case 4 failed"
assert SumAndPrint([-1]) == -1, "Test case 5 failed"

print("All test cases passed!")
