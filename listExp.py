dukan = ["ali","kola","potato"]
print(dukan) # ['ali', 'kola', 'potato']

# change item
dukan[2] = "sandwitch"
print(dukan) # ['ali', 'kola', 'sandwitch']

# this statement will print whole the bunch of list


print(dukan[:1])
# length of the list
siize = len(dukan);
print(siize)


dukan.append("new item")
dukan.append("new item1")
dukan.append("new item2")
dukan.append("new item3")
dukan.append("new item4")

print(dukan)

dukan.remove("new item")

print(dukan)


#negative indexing
print(dukan[-1])
#it will print the last value
print(dukan[-3:-1])



# loop through the list

print("looop through the list")
for x in dukan:
    print(x)



# check if item exists

if "sandwitch" in dukan:
    print("sandwitch is in dukan ")
else:
    print("no apple available")

# insert any where
# in java we use set method with the list object to add item an specified index

# but in python we use insert method

print(dukan) #['ali', 'kola', 'sandwitch', 'new item1', 'new item2', 'new item3', 'new item4']

dukan.insert(3,"halim mix") # it will not delete the index 3 item but also add the list and extend

print(dukan) #['ali', 'kola', 'sandwitch', 'halim mix', 'new item1', 'new item2', 'new item3', 'new item4']

dukan.pop() # remove the last item

for x in dukan:
    print(x)



# del keyword
print("\n")

del dukan[0]
print(dukan)


# copy a list
# we can copy a list into another list
newlist = dukan.copy()
print(f"new list are copied into {newlist}")

# we can also clear the list using clear method

#newlist.clear()
#print(newlist)



print(dukan[1:4])
