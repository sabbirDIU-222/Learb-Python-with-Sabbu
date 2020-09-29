# in java we are very motiveted to file handling
# right now we are doing so well
# and  i wanna learn how to file handling work in python
# and i notice that it is easy and making fun
# we create a txt file in our package
# that is country road take me home
# now creating a file


'''

  initialy they teach us to open a python file like that
  object = open("filename',mode="r")
  print(object.read())

so read will take care of my file and making the consol read to me

but i learn anything else

if our program crash anytime our private file data can be hacked
so i need to safe




'''


with open("countryroad.txt",mode="r") as f_name:
    words_all = []

    for line in f_name:
        words = line.strip().split(" ")
        words_all.append(words)



    print(len(words_all))

    f_name.close()


print("finished")




