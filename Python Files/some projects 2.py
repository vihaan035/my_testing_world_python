Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=1
>>> for A in range(5,26)
SyntaxError: invalid syntax
>>> for A in range(5,26):
	print(A)

5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
>>> 
>>> B=1
>>> for B in range(3,11)
SyntaxError: invalid syntax
>>> for B in range(3,11):
	print("3","X",B,"=",B*3)

3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30
>>> for B in range(1,11):
	print("3","X",B,"=",B*3)

3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30
>>> 