Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Language=str(input("Which language do you speak"))
Which language do you speakHindi
>>> Class=int(input("Which class do you study in?"))
Which class do you study in?6
>>> Year=int(input("Which year you were born in"))
Which year you were born in2009
>>> Country=str(input("Which country do you live in"))
Which country do you live inIndia
>>> print("You speak",Language" You study in Class",Class" You were born in",Year "You live in India")
SyntaxError: invalid syntax
>>> print("You speak",Language,n\" You study in Class",Class" You were born in",Year "You live in India")
      
SyntaxError: unexpected character after line continuation character
>>> print("You speak",Language, " You study in Class",Class " You were born in",Year "You live in India")
SyntaxError: invalid syntax
>>> print("You speak",Language, " You study in Class",Class, " You were born in",Year, "You live in India")
You speak Hindi  You study in Class 6  You were born in 2009 You live in India
>>> Language=str(input("Which language do you speak"))
Which language do you speakEnglish
>>> Class=int(input("Which class do you study in?"))
Which class do you study in?11
>>> Year=int(input("Which year you were born in"))
Which year you were born in2002
>>> Country=str(input("Which country do you live in"))
Which country do you live inAmerica
>>> print("You speak",Language, " You study in Class",Class, " You were born in",Year, "You live in India")
You speak English  You study in Class 11  You were born in 2002 You live in India
>>> 