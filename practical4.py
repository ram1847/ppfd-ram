fh=open('ram 4.txt','w')

abc=[12,2,3,4,7,68,8,9,5,3]
sum=0
i=0
while(i<len(abc)):
    sum= sum + abc[i]
    i=i+1
avg=int(sum/len(abc))
print('The average is:', avg)
fh.write('The average is '+ str(avg))
fh.close()