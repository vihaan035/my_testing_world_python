#Program for count all the even numbers between 1 to n.
n=int(input("Enter the number"))
total=0
for n in range(1,n+1):
    if n % 2 == 0:
        total=total+n

print(total)

