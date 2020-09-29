'''

  so i have a challenge that can make a new list from
  two list  make out what the difference

  supppose we have two list
  list1 = [1,2,3,4,5]
  list2 = [12,3,4]

  now in these two lists what the difference
  5 is the different

  it;s like the intersaction

'''


list1 = ['kalam','jabbar','borkot','jahangir','munsi abdur rouf','motiur']
list2 = ['kalam','jabbar','borkot','munsi abdur rouf']

set1 = set(list1)
se2 = set(list2)

list3 = list(set1.symmetric_difference(se2))


print(f"the officeres of birshrestho  {list3}")


# the method of set is symmetric difference
# that's why we need set 