fh=open('ram 9.txt','w')
n=int(input("Enter the number: "))
i=1
while i <= 10 :
    print(n ," *",i,"=",n*i)
    fh.write(str(n)+" * "+str(i)+"="+str(n*i))
    fh.write('\n')
    i=i+1
fh.close()