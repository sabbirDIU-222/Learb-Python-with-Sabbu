# we make a tuple that have a list

aTuple = (
    "sabbir",
    [23, 3, 1997],
    "Chandpur"

)
# so the list is my borth day date
# now i wanna to change the year cz i already changed it
# 1997 to 2000

aTuple[1][2] = 2000
print(aTuple[1]) #[23, 3, 2000]


# pari nai
# lambda use korse ty


'''xercise Question 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

Expected output:

(('c', 11), ('a', 23), ('d', 29), ('b', 37))


solution 

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

'''

# now i have a problem that
# check if all item are same

bTuple = (2,2,2,2)

def same(tuple):
    return all(i==tuple[0] for i in tuple) # i don't know what it is

print(same(bTuple))


