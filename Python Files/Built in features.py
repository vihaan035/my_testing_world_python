Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=-75.96
>>> print(abs(num))
75.96
>>> print("Abs value=",(abs(num)))
Abs value= 75.96
>>> Temperature=-40
>>> print("My current temperature is",(abs(num)))
My current temperature is 75.96
>>> print("My current temperature is",(abs(Temperature),"degree Celcius"))
My current temperature is (40, 'degree Celcius')
>>> print("My current temperature is",(abs(Temperature)),"degree Celcius")
My current temperature is 40 degree Celcius
>>> x=int(input("Enter the value of X"))
Enter the value of X56
>>> y=int
>>> y=int(input("Enter the value of Y"))
Enter the value of Y43
>>> print("After division answer is",divmod(x,y))
After division answer is (1, 13)
>>> 
>>> print ord(v)
SyntaxError: invalid syntax
>>> print(ord(v))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(ord(v))
NameError: name 'v' is not defined
>>> print(ord("v"))
118
>>> print(ord("b"))
98
>>> print("division=",divmod(118,98))
division= (1, 20)
>>> a=(ord("v"))
>>> b=
SyntaxError: invalid syntax
>>> 

>>> 

>>> 
>>> b=ord("b"))
SyntaxError: unmatched ')'
>>> b=ord("b")
>>> print('division=',divmod(a,b))
division= (1, 20)
>>> a=int(input("Enter the number which you want to round"))
Enter the number which you want to round80.9126
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a=int(input("Enter the number which you want to round"))
ValueError: invalid literal for int() with base 10: '80.9126'
>>> a=float(input("Enter the number which you want to round"))
Enter the number which you want to round80.9126
>>> round(a,2)
80.91
>>> print(pow(10,10))
10000000000
>>> a=int
>>> a=int(input("Enter the value of A"))
Enter the value of A6
>>> b=int(input("Enter the value of B"))
Enter the value of B7
>>> print("A is greater than B",a>b)
A is greater than B False
>>> print(" A is greater than B",a>b,"\n","B is greater than A",b>a,"\n","A=B or not",a==b)
 A is greater than B False 
 B is greater than A True 
 A=B or not False
>>> 