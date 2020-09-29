'''

   in java i learn about HashMap
   and the hash map was very benefitial for me
   even when i started to learn android i used this hash map where the key value conscept
   are very helpful

       HashMap<String,Integer> staff = new HashMap<>();


       staff.put("shamim", 33334);
       staff.put("emem", 44443);
       staff.put("robi", 11112);
       staff.put("koli", 333331);


so we put the key and value
but the key must be different

lets see how to ride of the Dictionary in python




'''

# suppose we have a key value pair of my friend zone
classmate = {"moti":" callu mal","nemo":" callu and fotka ","sagor":" faul","ibrahim":" adult"}
print(classmate)

# in this way we can print only key

for item in classmate:
    print(item)

print("\n")

# but how to print key and value pairlly

for key,value in classmate.items():
    print(key + value)

'''    moti  callu  mal
       nemo callu and fotka
       sagor  faul
       ibrahim   adult
'''

print("\n")
# we can print only the value
for v in classmate.values():
    print(v)



# length of the dictionary

print(f"{len(classmate)} is the length of the dictionary")

# contain any value
if "moti" in classmate:
    print("yes ! mota fucker are stilll alive")
else:
    pass

print("*********************************************")
print("\n")
print("removing items using pop() method ")

classmate.pop("nemo")
print(classmate)
'''removing items using pop() method 
{'moti': ' callu mal', 'sagor': ' faul', 'ibrahim': ' adult'}'''

# popitem() method doesn't take aby perameter
# it delete the last element

# first add an element


'''classmat={"tyy":"sds"}
print(classmate)
we can not add element like this 
'''
# we have to define the index and key value pair
print("addig an extra element in this way")
classmate["kana"] = "null"
print(classmate)


print("\n"+"the popitem() method ")
classmate.popitem()
for k,v in classmate.items():
    print(k + " " + v)

# using del key word delete any specified key  the dictionary
# use third braces
del classmate["moti"]
print(classmate)

'''
del classmate
print(classmate)
NameError: name 'classmate' is not defined

this will cause an error because "thisdict" no longer exists

'''



# adding some extra

classmate["mamun"]=" my friend"
classmate["nobel"]=" my nephew"
print(classmate)

# copy method

another_dictionary = classmate.copy()
print("new dictionary are loook")
print(another_dictionary)



# remove aagain

another_dictionary.pop("nobel")
print(another_dictionary)

# another way to copy dictionary using dict() method
print("all vaue copy in ok")
ok = dict(another_dictionary)
print(ok)
print("\n")
print("to making a new dictionary using dict() constructor ")


myname = dict(first="sabbir",middle="islam",last="shimul")
print(myname)
myname["nick"] = "sabbu"
myname.pop("middle")
print(myname)

d = myname.get("first")
print(d)