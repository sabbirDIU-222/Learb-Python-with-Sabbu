numberOfSub = int(input())
marks = input()
marksAsList = marks.split()


sum = 0
for x in marksAsList:
    sum += int(x)
    avg = sum/numberOfSub
print(avg)
