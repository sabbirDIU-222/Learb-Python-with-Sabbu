'''
  list comprhension is a very easy and fun things



'''

number = [1,2,3,4,5]
multiple = [x*x for x in number]
print(multiple)

fname = ['s','p','d','s']
lname = ['f','q','rr','ee']

concate = [x+y for x in fname for y in lname]

print(concate)
# so it print like all the value

result = [x for x in number if x%2==0]
print(f"all even number in list {result}")

