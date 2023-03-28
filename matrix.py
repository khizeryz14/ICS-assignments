A = [[2,3,5,8],[1,3,5,5],[2,0,9,1]]
B = [[5,2,3,6],[2,9,11,3],[6,10,3,4]]
C = []

if (len(A) == len(B)) and (len(A[0]) == len (B[0])):
    for i in range(len(A)):
        row = []
        for x in range(len(A[0])):
            row.append(A[i][x] + B[i][x])
        C.append(row)

for i in C:
    for x in i:
        print("%5.0f" % (x),end='')

    print()

