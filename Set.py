# in java we learn about HashSet
'''

  HashSet<String> email= new HashSet<>();
        email.add("asif@gmail");
        email.add("rajib@gmail");

        System.out.println("all elements are : " + email);

        so the basic properties of any HashSet are

        1. the hashset is not contain duplicate value
        2. we can add item by add method
        3. if any value contain we can check it by contain method
        4. we can loop through the set
        5. we can remove item by calling remove method
        6. we can add two different set by Addall method
        7. we can iterator the set


        so hash set was very much useful when we use it by passing any duplicate value it return only one



        but look what happen in python set class

        list , tuple , set , dictionary
        [   ], (   ) , {  },  { }






'''

print("making a set ")
# suppose we are in a buffet restaurent
# and we are offered to eat anythings but only one conditionn
# we can not take any item twice
# if we take , we have to pay for all food

# remember in set we use curly braces
dhanmondiBufet = {"thai soup","corn soup","fried rice","salad","godzilla pizza","chicken curry"}

# now simply print the set
print(dhanmondiBufet)
#{'chicken curry', 'fried rice', 'corn soup', 'thai soup', 'salad', 'godzilla pizza'}

# it print like that

# now one things very much interesting is that we can not change what we have
# so its means that if onces the set declare we can not replace any item of it
# but the happy things is that we can add more item
# to add any item we use simply add method ] in list we use append
dhanmondiBufet.add("salad")
# so look that we have already salad in our list
for item in dhanmondiBufet:
    print(item) # loop through the list


'''fried rice
thai soup
godzilla pizza
salad
corn soup
chicken curry
'''

# see we don't get the salad in our list , so same as java hash set we can not add duplicate item

# but if we have many item have to take
# we have to use update method

dhanmondiBufet.update(["semai","beef curry","salad","potato cips "]) # remember the third bracate

# now print through the loop
print(dhanmondiBufet)
#{'potato cips ', 'corn soup', 'fried rice', 'beef curry', 'chicken curry', 'salad', 'godzilla pizza', 'thai soup', 'semai'}

# the set are unordered so i don;t know where any of value or elements are contain
# so that's why we can not access any item

# do we listen one things
# in update we also put salad but this time also we are rejected to make salad twice
# but i bearly need salad again cZ the food is two oily

# one things i can do ,in the restaurant i should take another ticket or set
anotherSetMeal = {"salad","juice"}
# now add two sets
# so how we add two sets
# we can use union method
# or we can use update method

# first know the length of the first set
print(len(dhanmondiBufet)) # 9
union_item = dhanmondiBufet.union(anotherSetMeal)
for ui in union_item:
    print(ui.strip().split(" "))


# another way to concatation two different set

dhanmondiBufet.update(anotherSetMeal)
print(dhanmondiBufet)



'''['godzilla', 'pizza']
['chicken', 'curry']
['thai', 'soup']
['salad']
['corn', 'soup']
['juice']
['beef', 'curry']
['fried', 'rice']
['semai']
['potato', 'cips']'''

# this time also salad is not printed

# so i decide to remove the salad and dont eat it in here
print("removing the salad ")
dhanmondiBufet.remove("salad")
print(dhanmondiBufet)

# we can clear or delete all the set anytime and get out the restaurant
# to do this i need to clear method
print("\n")
print("clear the set")
dhanmondiBufet.clear();
print(dhanmondiBufet) # set()

# so now the set() is empty

# now we can use the set constructor to make any set again
print("\n")
print("the set() is a constructor and we can use it")
dhanmondiBufet = set(("kacci","morog polao","beer"))
print(dhanmondiBufet)

# lets see we contain any value or not

dhanmondiBufet.update(["biriani"])
print(dhanmondiBufet)
if "salad" in dhanmondiBufet:
    print("oh my salad")
else:
    pass

# we can remove but one suggestion , if our desire value is not in the set we get any error
# we already remove the salad
# lets see what happenn
'''dhanmondiBufet.remove("salad")
print("\n")
print(dhanmondiBufet) '''
# KeyError: 'salad'

# so the safe way is use discard method

dhanmondiBufet.discard("salad")
print("\n")
print(dhanmondiBufet)
if "salad" not in dhanmondiBufet:
    print("salad does not exists")
else:
    pass
print("finshed")

# using pop() method we can delete the last item


'''
{'morog polao', 'kacci', 'biriani', 'beer'}
salad does not exists
finshed

'''



'''del dhanmondiBufet
we can also delete the list like this '''


'''

   so its all about the list , 
   there are some different and simmiler with set and tuple 
   next i learn tuple 
   in tuple we make the list like ( ) using first braces 
   and also tuple are unchangable or immuatble 
   we can not insert any item also 
   but in set we can add 
   we can not access nay element in set but we can access any element by calling its index number in tuple 
   tuple are ordered 
   

'''
def addItem(addd):
    dhanmondiBufet.add(addd)

    # for single item add we need add method
    # for multiple item add we need update
