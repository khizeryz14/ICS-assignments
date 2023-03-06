print("0 3 8 series between two values")
series = 0
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))


for x in range(0,num2):
    series = series + (3 + (2*x))
    if (series > num1) and (series <= num2):
        print(series)
        
        

