Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome to my mini calculator")
Welcome to my mini calculator
>>> A=int(input("Enter first number"))
Enter first number
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    A=int(input("Enter first number"))
ValueError: invalid literal for int() with base 10: ''
>>> A=int(input("Enter first number"))
Enter first number56
>>> B=int(input("Enter second number"))
Enter second number12
>>> add=A+B
>>> Sub=A-B
>>> div=A/B
>>> Mul=A*B
>>> sub
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sub
NameError: name 'sub' is not defined
\
>>> Sub
44
>>> Mul
672
>>> A=int(input("Enter first number"))
Enter first number5
>>> B=int(input("Enter second number"))
Enter second number6
>>> div
4.666666666666667
>>> print("Welcome to my mini calculator")
Welcome to my mini calculator
>>> A=int(input("Enter first number"))
Enter first number