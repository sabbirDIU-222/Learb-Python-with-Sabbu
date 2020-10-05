'''

 filter is the same shit as map
 filter() also take two perameter one is fundtion and another is iterable


'''
# a simple program
def findodd(value):
    return value%2 !=0


number = [1,2,3,4,5,6,7]
result = list(filter(findodd,number))
print(result)

# the smae shit i can do in lambda cz there only one expressionn
result2 = list(filter(lambda x:x%2!=0,(1,2,3,4,5,6,7,8,9)))
print(result2)

# now we make a program that print all value under 18
def numbers(value):
    if value >= 18:
        return False
    else:
        return True


values = [44,83,22,10,3,18,17,12]
result3 = list(filter(numbers,values))
print(result3)

# now different program
product_list = ["oil","coil"," ","egg","","rice","cucumber"]

result5 = list(filter(None,product_list))
print(result5)



