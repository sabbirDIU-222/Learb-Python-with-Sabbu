# making a matrix
# and print it out

Matrix = [

    [1,2,3],
    [4,5,6]

]



# print any spacifiq row and coloumn
print(Matrix[0][2])
# 3 print

# we can also update

Matrix[0][2] = 10

# print all value

for row in Matrix:
    for coloum in row:
        print(coloum,end=" ")
    print(" ")


