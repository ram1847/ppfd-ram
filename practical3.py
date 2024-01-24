fh=open('ram 3.txt','w')
import random 
length = int(input("Enter the  length of password required :"))
char_included = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456790!@#$%^&*"
i = 0
password = ' '
while i < length :
    password =password + random.choice(char_included)
    i = i +1
print("Password=",password) 
fh.write("Password="+str(password)) 
fh.close() 