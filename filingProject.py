import os

print("Taking input in file")

seatNo = input("Enter seat no: ")
myFile = open('studentData.txt','w')
while int(seatNo) > 0:
    studentName = input("Enter student name: ")
    Isl = input("Islamiyat marks: ")
    Pst = input("PST marks: ")
    Ics = input("ICS marks: ")
    Phy = input("Phy marks: ")
    Calc = input("Calculus marks: ")
    Eng = input("English marks: ")
    Stat = input("Statistics marks: ")
    myFile.write(seatNo + "\t" + studentName + "\t" + Isl + "\t" + Pst + "\t" + Ics + "\t" + Phy + "\t" + Calc + "\t" + Eng + "\t" + Stat +"\n")
    seatNo = input("Enter seat no: ")

myFile.close()

os.system("CLS")
print("Reading and processing from file")
readFile = open('studentData.txt','r')
totalLines = len(readFile.readlines())
readFile.seek(0)
print("Total lines:",totalLines)
for i in range(0,totalLines):
    line = readFile.readline().split("\t")
    total = 0
    for x in range(2,9):
        total += int(line[x])

    print("Total is:",total)
    percentage = (total/700)*100
    print("Percentage is:",percentage)

    if(percentage >= 90):
        print("Grade: A")
    elif(percentage >= 80) and (percentage < 90):
        print("Grade: B")
    elif(percentage >= 70) and (percentage <80):
        print("Grade: C")
    elif(percentage >= 60) and (percentage <70):
        print("Grade: D")
    elif(percentage >= 50) and (percentage <60):
        print("Grade: E")
    else:
        print("Grade: F")
print("End!")
    
