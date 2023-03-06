print("Odd numbers between two values")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
for i in range(num1,num2+1):
    if i % 2 == 1:
        print(i)
