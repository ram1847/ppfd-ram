fileh=open("ram 1.txt",'w')
temp = int(input("""Select  your choice to enter the temperature in respected degree
               1.Farenheit
               2.Celsius  
               : """))
if temp == 1 :
    Fa=int(input("Enter the temp in Farenheit:"))
    C=(Fa-32)*5/9
    fileh.write(str(C)+'Degrees in celsius')
elif temp == 2 :
    ce=int(input("Enter the temp in Celsius : "))
    F=(9/5)*ce+32
    fileh.write(str(F)+" DEGREES FAHRENHEIT")
else :
        fileh.write( )
        fileh.close()
    