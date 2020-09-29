# taking a input

number = input("enter a text ")
# this input must take  a string

nlist = number.split()
sum = 0
for n in nlist:
    sum += int(n)
print(nlist)
print(f"the sum of all number {sum}")
'''
['10', '20', '30', '40', '50']
the sum of all number 150
'''