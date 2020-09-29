# for loop exersize in the systamatic way

# so we first work with  the list

party = ['drinks','chicken','apple','snow','ice','bodka','rma','chess board']

for p in party[:4]:
    print(p)
    print(len(p))
    print(sorted(p))


for n in "banana":
    print(n)


# break statement to break the loop in our specifed item

alist = ["sabbir","mamun","ibrahim","moti","sagor","ridwan","yasin","nemo"]
#With the break statement we can stop the loop before it has looped through all the items
for l in alist:
    print(l)
    if l=="moti":
        break



# for loop in range
# alll that time we should not use list
# so we need to contain a range to stop our loop

for x in range(10):
    print(x)
# it is printing to strat 0 to 9
# so it has no start limit>?
# yah it have a start and stop limit

print("range method thake three perametr ")
print("one take start value , second take range or finishing point , and last want increment")
print("")

for c in range(1,6): # the range function default value is 0
    print(c)
    # 1 to 5 printing


print("\n")

print("range function start with 0 so need to print extended level that you desire")

for d in range(5,10,1):
    print(d)
# 5 to 9 print

# nested for loop

# suppose we have two different type of list
print("\n")
print("nested for loop")
point = ["*",'**']

for i in point:
    for j in alist:
        print(i,j)

i = 1
while i<6:
    print(i)
    i += 1
