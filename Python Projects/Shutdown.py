import os

shut=input("Do you wish to shutdown No/Yes")
if shut == "no":
    exit()
else:
    os.system("shutdown /s /t 1")         
