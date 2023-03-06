flag = False
print("Each digit even between 100 and 400")
for i in range(100,401):
    a = str(i)
    for x in a:
        if int(x) % 2 == 0:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print(i)
