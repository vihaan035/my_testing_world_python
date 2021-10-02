Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=int(input("Enter the first number"))
Enter the first number-10
>>> print("Abs value of the following number=",abs(A))
Abs value of the following number= 10
>>> B=int
>>> 
>>> B=int(input("Enter the first number"))
Enter the first number5
>>> C=int(input("Enter the second number"))
Enter the second number4
>>> print("The Division of the following number=",divmod(B,C))
The Division of the following number= (1, 1)
>>> D=int(input("Enter the number which you want to round"))
Enter the number which you want to round
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    D=int(input("Enter the number which you want to round"))
ValueError: invalid literal for int() with base 10: ''
>>> D=int(input("Enter the first number which you want to round"))
Enter the first number which you want to round50
>>> E=int(input("Enter the second number which you want to round"))
Enter the second number which you want to round50
>>> print("The round of the following numbers=",round(D,E))
The round of the following numbers= 50
>>> D=float(input("Enter the first number which you want to round"))
Enter the first number which you want to round
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    D=float(input("Enter the first number which you want to round"))
ValueError: could not convert string to float: ''
>>> D=float(input("Enter the first number which you want to round"))
Enter the first number which you want to round50.33
>>> print("The round of the following numbers=",round(D))
The round of the following numbers= 50
>>> E=int(input("Enter the first number"))
Enter the first number50
>>> F=int(input("Enter the second number"))
Enter the second number50
>>> print("The power of the following numbers are")
The power of the following numbers are
>>> print("The power of the following numbers are",pow(E,F))
The power of the following numbers are 8881784197001252323389053344726562500000000000000000000000000000000000000000000000000
>>> 