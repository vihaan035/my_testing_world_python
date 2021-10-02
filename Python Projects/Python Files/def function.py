Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=1
>>> while A < 6:
	print("10"*A)
	A+=1

10
1010
101010
10101010
1010101010
>>> def person(name):
	print(" Hi "+name)

>>> person("Ashwini")
 Hi Ashwini
>>> def country(hello):
	print(" I live in "+hello)

>>> country("India")
 I live in India
>>> def name(first,last):
	print("My name is "+first,last)

>>> def name(first,last):
	print("My name is "+first+last)

>>> name("Vihaan","Gupta")
My name is VihaanGupta
>>> def name(first,last):
	print("My name is "+first+last)

>>> name("Vihaan"," Gupta")
My name is Vihaan Gupta
>>> def fav(first,second,third):
	print("My favourite color is "+first+second+third)

>>> fav("red"," green"," blue")
My favourite color is red green blue
>>> def multiplication(a,b,c):
	print("Multiplicatioin is", a*b*c)

>>> multiplication(2, 1, 3)
Multiplicatioin is 6
>>> def div(x,y):
	print("division is", x/y)

>>> div(5, 10)
division is 0.5
>>> def square(l):
	print("SQUARE is", x*x)

>>> def square(l):
	print("SQUARE is", l*l)

>>> square(5)
SQUARE is 25
>>> 