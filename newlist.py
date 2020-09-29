# add two list
list1 = [1,90,4,32,89,3]
list2 = [2,54,66]

# we can use many ways to add  two list

list3 = list1 + list2
print(list3)


# another way to add to list




list4 = list1.copy()
list2.append(list4)
print(list2)

# making list using list constructor


list5 = list(("sabir"," manu","jinia"))
print(list5)

list6 = list((1,2,3,4,4,54))

list6.extend(list5)
print(list6)


# how many 4 i have in my list

innn = list6.count(4)
print(innn)
# now it print 2
# i have 2 four in my list
list5.sort()
print(list5)
