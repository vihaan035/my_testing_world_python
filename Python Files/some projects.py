Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(input("value for a"))
value for a50
>>> b=int(input("value for a"))
value for a
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b=int(input("value for a"))
ValueError: invalid literal for int() with base 10: ''
>>> b=int(input("value for b"))
value for b35
>>> c=int("division of a and b"))
SyntaxError: unmatched ')'
>>> c=a/b
>>> print c
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(c)?
>>> c
1.4285714285714286
>>> print("Division of a and b =",c)
Division of a and b = 1.4285714285714286
>>> Name=str(input("What is your name?"))
What is your name?Vihaan
>>> Surname=str(input("What is your surname"))
What is your surnameGupta
>>> print("My name is",Name, Surname)
My name is Vihaan Gupta
>>> Color=str(input("What is your favourite color:)"))
What is your favourite color:)Blue
>>> Cartoon=str(input("What is your favourite cartoon?"))
What is your favourite cartoon?I dont have any favorite cartoon
>>> Age=int(input("What is your age?"))
What is your age?immortal
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Age=int(input("What is your age?"))
ValueError: invalid literal for int() with base 10: 'immortal'
>>> Age=int(input("What is your age?"))
What is your age?11
>>> print("My favourite color is",Color,"\n","My favorite cartoon is",Cartoon, "My age is",Age)
My favourite color is Blue 
 My favorite cartoon is I dont have any favorite cartoon My age is 11
>>> print(" My favourite color is",Color,"\n","My favorite cartoon is",Cartoon, "My age is",Age)
 My favourite color is Blue 
 My favorite cartoon is I dont have any favorite cartoon My age is 11
>>> 