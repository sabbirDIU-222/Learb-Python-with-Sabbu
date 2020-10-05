lis = [1,2,3,5,5]
lis2 = [6,7,8,9,2]

lis3 = dict(zip(lis,lis2))

print(lis3)
# list comprehension
lis2 = [x*x for x in lis2]
print(lis2)

first = ["hello","take"]
last = [" dear"," sir"]

result = [x+y for x in first for y in last]
print(result)

seq1 = [10,20,30,40,50]
seq2 = [100,200,300,400,500]

for x,y in list(zip(seq1,seq2[::-1])):
    print(x,y)

sequence = ["mike","","mike","","","ema","je"]
ne = filter(None,sequence)
print(ne)

pagla = [10, 20, [300, 400, [5000,[1,2,3], 6000], 500], 30, 40]
pagla[2][2][1].append(7000)
print(pagla)
list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)
list1[index] = 200
print(list1)


r1 = [5, 20, 15, 20, 25, 50, 20]

def without20(list,value):
    return [x for x in list if x!=value]

d = without20(r1,20)
print(d)



def ev(nu):
    if nu%2!=0:
        return nu



u = [1,2,3,4,5,6,7,8,9,10]
i = list(filter(ev,u))
print(i)