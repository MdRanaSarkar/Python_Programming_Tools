
"""
Type 1:
How do you write functions in Python?
How do you call functions in Python?

block_keyword block_name(argument1,argument2, ...)
Block keywords you already know are "if", "for", and "while".

Functions in python are defined using the block keyword "def"
if __name__ == '__main__':
"""


def Name():
    print("Rahim")


Name()

"""
type 2:
Functions may also receive arguments(variables passed from the caller to the function).
"""
"""

def Square(a):
    return a*a


b = int(input())
print(Square(b))

"""


def sum(a, b):
    return a+b


c, d = map(int, input().split())


if __name__ == '__main__':
    print(sum(c, d))
