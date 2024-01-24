a=int(input("Enter a:"))
fh=open('ram 6.txt','w')
fact=1
while(a>1):
    fact=fact*a
    a=a-1

print(fact)
fh.write(f'the factorial of the given number is {str(fact)}')
fh.close()