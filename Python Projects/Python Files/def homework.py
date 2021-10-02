Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Addition
>>> def add(a,b):
	print("Addition is", a+b)

>>> add(10, 6)
Addition is 16
>>>  #Subtraction
>>> def sub(c,d):
	print("Subtraction is", c-d)

>>> sub(10, 5)
Subtraction is 5
>>> #Multiplication
>>> def mul(e,f):
	print("Multiplication is", e*f)

>>> mul(10, 7)
Multiplication is 70
>>> def div(g,h):
	print("Division is", g*h)

>>> div(50*5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    div(50*5)
TypeError: div() missing 1 required positional argument: 'h'
>>> div(50, 5)
Division is 250
>>> 