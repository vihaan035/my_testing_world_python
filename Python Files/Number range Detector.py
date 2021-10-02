Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(input("Enter your number"))
Enter your number201
>>> if a < 10:
	print("The number is between 0 and 10")
elif a < 50:
	print("the number is between 10 and 50")
elif a < 100:
	print("The number is between 50 and 100")
elif a < 250:
	print("The number is between 100 and 250")
elif a < 500:
	print("The number is between 250 and 500")
elif a < 750:
	print("The number is between 500 and 750")
elif a < 1000:
	print("The number is between 750 and 1000")
elif a > 1000:
	print("This number is more than 1000")

The number is between 100 and 250
>>> 