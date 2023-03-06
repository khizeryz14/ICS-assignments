print("Print common divisors")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
if num2 > num1:
    runner = num2
else:
    runner = num1

for x in range(1,runner):
    if (num1 % x == 0) and (num2 % x == 0):
        print(x)
        

