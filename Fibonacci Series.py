# fibonacci series in pyhton
num = int(input(" which number fibo u want "))

num1 , num2 = 0,1
count =0



'''while count<num:
    print(num1 , end=' ')
    nextnum = num1+num2

    num1 = num2
    num2 = nextnum
    count +=1'''



for x in range(0,num,1):
    print(num1, end=' ')
    nextnum = num1 + num2

    num1 = num2
    num2 = nextnum


# two differernt way