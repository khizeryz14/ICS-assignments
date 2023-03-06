print("Factorial program")
num = int(input("Enter number: "))
for i in range(num,2,-1):
    num = num*(i-1)
print(num)
