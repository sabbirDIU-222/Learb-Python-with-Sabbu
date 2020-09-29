#for loop problem



# leap year problem

def lep_year(year):
    leap = False
    if(year%4)==0 and (year%100)==0 and (year%400)==0:
        leap = True
    elif(year%4)==0 and (year%100)!=0 and (year%400)!=0:
        leap = False


    return leap

year = int(input())
print(lep_year(year))

