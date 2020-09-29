# ternary operator
# suppose we have to digit to find what is the biggest
'''

what we simply do

we do the things

num1 = 10
num2 = 30
if num1>num2:
    print(f"{num1} is the big number")
else:
    print(f"{num2} is the big number")


# print 30 is the big number
'''

# now using ternary operator we can easily do
# take two number
num1 = 1933
num2 = 2022
print(num1 if num1>num2 else num2," is  the big number")
# this is ternary operator তিনটি operator
# we can not put any string in the middle of the ternary operator
# but after the ternary operator we can do it


# program to checking the imputing value is how much word and how much digt and how much letter
numofWord =0
numofLeter =0
numofdigit =0

sentence = input("your basic info ")

for  x in sentence:
    x.lower()
    if x >='a' and x <='z':
        numofLeter += 1
    elif x >='0' and x <= '9':
        numofdigit += 1
    elif x >= ' ':
        numofWord +=1


print("number of worrds are : ", numofWord)
print("number of letter are : ", numofLeter)
print("number of digit are : ", numofdigit)
print(sentence.count("i"))