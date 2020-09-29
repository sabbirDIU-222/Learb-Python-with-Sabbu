# so we did it before ,
# and we call it arbetary argument

# in this term of code we can use our function as we want

# we learn it in java as variable argument or varAgrs

'''

public void methodname(int... variablename){

    sum = 0;
    for(int x : variablename){

        sum = sum+x
     }
    System.out.println(sum);


 }

'''

# same as in python we can use variable argument in different way

def addnumber(*args):
    sum = 0
    for x in args:
        sum += x
    print(sum)


addnumber(3)
addnumber(3,10)
addnumber(3,10,40)
addnumber(100,300,322,540,302,33)


# or sum of all negative number


argument = int(input("take the range"))
def addAllNegativenumber(agrument):
    sum =0
    for x in range(argument):
        if (x%2)==0:
            continue
        else:
            sum += x

    print(sum)


addAllNegativenumber(argument)

# alternative way to print all odd number

sum = 0
for x in range(1,10,2):
    sum += x
print(sum)


























