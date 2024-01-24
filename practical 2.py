Choice = int(input("""Select 1.For Area of Rectangle 
                   2. For Perimeter of rectangle     :  """))

fh=open('ram 2.txt','w')
if Choice == 1 :
    len = int(input("Enter the length of Rectangle :"))
    bre = int(input("Enter the Breadth of Rectangle :"))
    Area = len * bre
    fh.write(f'area of rectangle is {str(Area)}')
    print(Area)
elif Choice == 2 :
    length = int(input("Enter the length of Rectangle :"))
    breadth = int(input("Enter the Breadth of Rectangle :"))
    Perimeter = 2 *( length + breadth)
    print(Perimeter)
    fh.write(f'area of rectangle is {str(Perimeter)}')
else :
    print( )

fh.close()
