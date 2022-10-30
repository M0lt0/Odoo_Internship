
mas = "your age is:"
val = int(input("Enter your age: ") ) + 1

print(mas  , val)
 

x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print();
# this script aim is to show data types in python;
intro = "this is a number type in python"
# this is an integers
a = 7
# this is a float
b = 7.52
# this ia a complex number
c = 1e9
print(intro, "\n", a, "is an intger\n", b, "is a float\n", c, "is a complex\n")

# also we have string type
g = "iam a string"
print("this is a string type", "\n", g)

# also we have boolean type
t = True
f = False
print("we have the truthiness", "\n", t, "\n", f)
"""
# the if statement is used for conditional work
"""
intro = "this is the if statement concept for example we want a script to check if the given number is even or odd so\n the we will check if the number can divide by 2 or not \n "


x = 10
y = 7
if (x % 2) == 0:
    print(intro, "\n", "so when we use number 10 the result is even ")
if (y % 2) != 0:
    print("if we use 7 for example the number is odd")
er = "###############\nso in programming we need to know if something is off \n##############\n for example we have SyntaxError: \n##############\n when we miss some think in typing \n -also we have AssertionError: \n##############\n Raised when the assert statement fails. \n -NameError: \n##############\n Raised when a variable is not found in local or global scope.\n -OverflowError: \n##############\n Raised when the result of an arithmetic operation is too large to be represented."
print(er)
