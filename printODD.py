# print all odd number

for x in range(1,101):
    if(x%2)==0:
        continue

    else:
        print(x)
# arbitory argument same as variable argument in java

def age(*age):

    print("total age of your life ",age[:])

age(56,8765,887)

