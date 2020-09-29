for x in range(101):
    if (x%4)==0:
        print(x)


# continue statement
rollnumber = [2,3,7,21,33,45]
print("")

for x in range(1,31):
    if x in rollnumber:
        continue
    else:
        print(x)

