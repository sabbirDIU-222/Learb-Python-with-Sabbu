'''

   i learn a new awasome things that is tuple
   tuple is called that immutable so it can't be changed
   we can access it's value
   we can not modify it's value
   we use () first bracate to use tuple
   i noticed some use list into a tuple



'''
# let's make a group that never changed
aTuple = (

    "Sabbir",
    "MOti",
    "Sagor",
    "Ridwan",
    "Mamun",
    "Robi",
    "Sinthia",
    "MAhin",
    "Lopa",
    "Lopa",

)

# let's try to access lopa
print(aTuple[8])

# using negative indexing we can also access lopa
print(aTuple[-1])
# it again print lopa

# hey !! can we find the len of the tuple

print(len(aTuple))
# it print 9
# so we did it

#now we can have the range idea not using loop
print(aTuple[2:8])
#('Sagor', 'Ridwan', 'Mamun', 'Robi', 'Sinthia', 'MAhin')
# i notice one thing it start from 2 but not end in 8
# it end in 7

# so i look out  a tricks
# through we can not change the value of tuple but we are marily need one person extra or more
# then we can type cast
# make the tuple into  a list

making_tuple_list = list(aTuple)
making_tuple_list.append("yasin")
aTuple = tuple(making_tuple_list)
print(aTuple)
'''
# we can print the tuple through the loop
for x in aTuple:
    print(x)'''

'''# check if item is exists or not
if "Sabbir" in aTuple:
    print("yes sabbir is in the tuple")
else:
    print("who is this shit")
   '''
print("lopa name enter times ",aTuple.count("Lopa"))