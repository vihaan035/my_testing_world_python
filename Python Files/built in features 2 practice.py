Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> a="Vihaan"
>>> a.strip("V")
'ihaan'
>>> programming.upper
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    programming.upper
NameError: name 'programming' is not defined
>>> a.upper
<built-in method upper of str object at 0x03E09960>
>>> country="India,Australia,Italy,Us,Uk"
>>> country.lower()
'india,australia,italy,us,uk'
>>> country.upper
<built-in method upper of str object at 0x03E05800>
>>> country.upper()
'INDIA,AUSTRALIA,ITALY,US,UK'
>>> len(country)
27
>>> print(country.split(',',4))
['India', 'Australia', 'Italy', 'Us', 'Uk']
>>> a=str(input("Enter your name"))
Enter your nameViHaaN
>>> b=a.lower()
>>> c=a.upper
>>> c=a.upper()
>>> print(b)
vihaan
>>> print(a)
ViHaaN
>>> print(b)
vihaan
>>> print(c)
VIHAAN
>>> 