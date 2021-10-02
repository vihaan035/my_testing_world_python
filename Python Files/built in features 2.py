Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> help(in)
SyntaxError: invalid syntax
>>> help(int)

>>> a=Vihaan
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=Vihaan
NameError: name 'Vihaan' is not defined
>>> a="Vihaan"
>>> a.strip("  h")
'Vihaan'
>>> a.strip("V")
'ihaan'
>>> a="Vihaan"
>>> a.strip("  h")
'Vihaan'
>>> a.strip("  h ")
'Vihaan'
>>> a="Vihaan"
>>> a.strip("  h   ")
'Vihaan'
>>> a="Vihaan"
>>> print(a.strip("  h "))
Vihaan
>>> 
>>> 
>>> a="vihaan"
>>> print(a.strip())
vihaan
>>> print(a.strip("v"))
ihaan
>>> a="vihaan"
>>> print(a.strip())
vihaan
>>> print(a.strip(" i    "))
vihaan
>>> a="vihaan"
>>> print(a.strip())
vihaan
>>> print(a.strip(" i"))
vihaan
>>> a="PY FOR PY"
>>> print(a.strip())
PY FOR PY
>>> print(a.strip("PY"))
 FOR 
>>> a="vihaan"
>>> print(a.strip())
vihaan
>>> print(a.strip("a"))
vihaan
>>> programming="Python"
>>> programming.upper
<built-in method upper of str object at 0x00892820>
>>> programming.upper()
'PYTHON'
>>> country="India,Australia,Italy,US,UK"
>>> country.lower()
'india,australia,italy,us,uk'
>>> len(country)
27
>>> print(country)
India,Australia,Italy,US,UK
>>> country.upper()
'INDIA,AUSTRALIA,ITALY,US,UK'
>>> print(country.split(',',4))
['India', 'Australia', 'Italy', 'US', 'UK']
>>> a=str(input("Enter your name"))
Enter your namevIhAAn
>>> b=a.lower
>>> b=a.lower()
>>> c=a.upper()
>>> print(c)
VIHAAN
>>> print(b)
vihaan
>>> 