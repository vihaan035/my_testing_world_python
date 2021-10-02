Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> count=0
>>> login=str(input("Enter login"))
Enter loginabc
>>> password=int(input("Enter password"))
Enter password1234
>>> while True:
	count+=1
	if count == 3:
		break
	else:
		if login == "abc" and password == "1234":
			print("Welcome")
		else:
			print("Wrong input or out of attempts")

Wrong input or out of attempts
Wrong input or out of attempts
>>> count=0
>>> login=str(input("Enter login"))
Enter loginabc
>>> password=int(input("Enter password"))
Enter password1234
>>> while True:
	count+=1
	if count == 3:
		break
	else:
		if login == "abc" and password == "1234":
			break
		else:
			print("Wrong input or out of attempts")

Wrong input or out of attempts
Wrong input or out of attempts
>>> 