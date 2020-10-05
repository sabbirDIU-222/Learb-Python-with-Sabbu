'''

    The map() function executes a specified function for each item in an iterable
    The item is sent to the function as a parameter

     i learn that things in also filter function
     so filter function do the same things


     map( function , iterable   )
   map takes two perametre and a function and a iterable
   iterable can be a list[] , tuple{} , set{} , dict{}


'''

# make a function that can square the value of list

def square(value):
    return value*value

value = [1,2,3,4,5,6]
# error khaisilm
result = list(map(square,value))
print(result)
'''
 to ki error khaisilm 
 map(square(value),value)
 so i did a sin that is inside map function first i called square function
 but what i did ! i did make a perameter of square function and inside it i put the list object
 so the compiler going to crash 
'''

# now i did a program that take the value and return it's length
def findlen(value):
    return len(value)
name = ['mamun','shimul','nemo','moti']
result2 = list(map(findlen,name))
print("so the name have this digit",result2)

# using lambda to  make it easy
result3 = list(map(lambda value : len(value),name))
print("so the name have this digit",result3)

# ****
# make a new program that concate two value or string

def concate(value1,value2):
    return value1 + value2

result4 = list(map(concate, ("shimul", "al", "robi"), (' sabbir', ' mamun', ' nemo')))
print(result4)

def making(h,m):
    return h*m

f = list(map(float,input().split()))
print(making(f[0],f[1]))
