'''

   so i learned it before in java
   that was variable argument
   or var args

   public void joj(int...number){

       sum = 0;
       for(int i : number){

            sum = sum + number;

         }
         System.out.println(sum);

   }

same as variable argument python support xargs

'''
# suppose we have a function named details
def details(id,name):
    print(id,name)

details(23,"fafa")
# but now we neeed another argument that told our home district
def details(id,name,homedistrict):
    print(id,name,homedistrict)


# so it quit chores for me and i think all of us

# we need to understand what is the best easy way

def my_detail(*details):
    print(details)





# this * will take any type of perameter
# and print like tuple

my_detail("sabbir",23,"years old","mymensings")
# ('sabbir', 23, 'years old', 'mymensings')

# in varible arg in java we use same data type but python support all
'''
error khaisi
x argument key value pair e booy na 
x argument variable arg er moton . value dilei hoy ,
x argument tuple type

my_detail(name="sabir",id=122)
TypeError: my_detail() got an unexpected keyword argument 'name'
'''