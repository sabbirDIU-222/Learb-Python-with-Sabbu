# for singly making a tuple
aTuple = ("sabbit",) # we need a comma after entering one elements
print(aTuple)
print(type(aTuple)) # <class 'tuple'>

# but if we don't give any comma it will not be a tuple
bTuple = ("samiwon akter")
print(bTuple)
print(type(bTuple)) # <class 'str'>



# unpacking a tuple
numberTuple = (1,2,3,4,5)
a,b,c,d,e = numberTuple
print(a)
print(b)
print(c)
print(d)
print(e)

'''
1
2
3
4
5
'''

# swap two different tuple
stringtuple = ("ali","hasan")
numtuplr = (25,23)
print("before swaping ")
print(stringtuple)
print(numtuplr)
print("\n")

stringtuple , numtuplr = numtuplr , stringtuple
print(stringtuple)
print(numtuplr)

ATup = (1,2,23,4,5,6,57,77)
# we copy 6 and 57 from the tuple into a new tuplee
print(f"coping 6 an 57 from {ATup}")
newTuple = ATup[5:-1]
print(newTuple)




