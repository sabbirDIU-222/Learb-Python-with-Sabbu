# so what is unpacking ugument
# i am surprised to know about the horriable things
# and that is , what i learn about the arbetery argument \
# or can i call it paking and unpaking
# so what i learn aboout variable argument \
'''

def _thisFunction(*args):
    sum = 0
    for n in range(0,len(args)):
        sum = sum+args[n]

    return sum

print(_thisFunction(10,20,30,40,50))
print(_thisFunction(1,2,3,4,5))


'''

# so this called packing to packing

# now the things


def helth_calculator(age,eatingapple,tosingCigr):
    res = (100-age) + (eatingapple*3.25) - (tosingCigr * 2)
    if res <= 100:
        print("your condition is not good")
    elif res>=100:
        print("your health condition is goood")
    print(res)



sabbuInfo = [23,2,14]
moonInfo = [22,10,0]

helth_calculator(*sabbuInfo) # that is called unpacking sequence
helth_calculator(*moonInfo)








