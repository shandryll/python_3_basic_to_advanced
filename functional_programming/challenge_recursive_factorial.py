"""
CHALLENGE:
Using recursion, create a method to show the factorial of a number
"""

def factorial(number):
    return number * (factorial(number - 1) if (number - 1) > 1 else 1)


if __name__ == '__main__':
    print(f'10! = {factorial(10)}')
