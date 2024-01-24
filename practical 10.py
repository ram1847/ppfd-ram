a=int(input('choose one 1.Binary 2.Decimal:'))
fh=open('ram 10.txt','w')
if a==1:
    binary_number=input('Enter :')
    n=int(binary_number,2)
    print(n)
    fh.write(f'the decimal form of {str(binary_number)} is {str(n)}')
if a==2:
    number=int(input('Enter '))
    abc=bin(number)
    print(abc[2:])
    fh.write(f'the binary form of {str(number)} is {str(abc)}')

fh.close()
