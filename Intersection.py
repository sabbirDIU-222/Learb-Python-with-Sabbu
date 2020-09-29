'''

    symectric difference we learn how to find
    uniq elements from two list
    now find the common elements from the list


'''


list1 = ['sabbir','mamun','moti']
list2=  ['sabbir','mamun','ibrahim']

set1 = set(list1)
set2 = set(list2)

list3 = list(set1.intersection(set2))
print(list3) # sabbir and mamun are common
"""
        Return the intersection of two sets as a new set.

        (i.e. all elements that are in both sets.)
"""