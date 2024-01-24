fh=open('ram5.txt','w')
a=int(input('Enter year: '))
if(a%4==0):
    print('It is a leap year')
    fh.write('Leap Year')
else:
    print('Not a leap year')
    fh.write(' Not a Leap Year')
    fh.close()
