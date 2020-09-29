a = int(input(" take a number  : "))

if (a%2)==0:
    print("even number")
else:
    print("odd")

# nested if else

b = int(input("take another number : "))
c = int(input("take one more number : "))

if b>c:
    result = b * 3.1416
    print(result)
elif (b/2)==0 :
    result = b%2
    print(f"reminder {b}")
else:
    print(f"{c} is the number alone")


# if you have only one statement then write it all in single line

name = str(input("name : "))
if name=="sabbir" : print(f"welcome {name}")
if name.__eq__("ssa") : print("not welcome")


# terenary operation
#or we can say it conditional expression

a = 9
b = 33
print("Alomgir is my best friend ") if a>b else print("fuck up")



# AND keyword in python

print("\n")
print("and keyword in python")


a = 89
b = 32
c = 6
if a>b and a>c:
    print(f"{a} is the big number ")
elif b>a and b>c:
    print("b is gretest")
else:
    print(f"{c} is the gretest number")


    # program to check OR keyword


a = 20
b = 45
c = 8

if a>b or b<a:
        print("error")
else:
    print("no")

