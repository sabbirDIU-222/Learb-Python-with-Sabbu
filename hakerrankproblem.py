number = int(input())
if (number%2)==0:
    if(number>1 and number<6):
        print(" NOt Weired")
    elif(number>5 and number<21):
            print("Weired")
    elif(number>20):
        print("Not Weird")

else:
        print("Weired")



a = int(input())
b = int(input())

def calculate(a,b):
    sum =  a+b
    sub = a-b
    pro = a*b

    print(sum)
    print(sub)
    print(pro)


calculate(a,b)

# division problem

a = int(input())
b = int(input())

def newcalculate(x,y):
    floorvalue = x//y
    floatvalue = x/y

    print(floorvalue)
    print(floatvalue)


newcalculate(a,b)




