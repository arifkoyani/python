# name="arif hussain"
# print("this is my name  ",name);
# def sum_numbers(a,b):
#     return a+b
# result=sum_numbers(5,6)
# print(result)

# print(45>99 and 56>6) 
# # and operator in py
# print(45>99 or 56>6);
# or operator in python

# names=["arif","ali","khan"]
# print("alia" in names)

# age=50
# myage=50
# print(id(age)==id(myage))

# if we assign the same immutable value in variable it automatically address to same memory address
# name="arif"
# name="ali"
# print(name)
# If you assign a new value to the same variable name, Python will overwrite the previous value and update the reference

# x=40
# print(id(x))
# x=60
# print(id(x))

# name=99
# myname=45
# print(name+myname)

# names=["aliza","khan","mubeen","aliyar"]
# fruit=["apple","orange","water melon","bananna"]
# names_fruits=names+fruit
# print(len(names_fruits))

class Name:
    def __setname__(self,name):
        self.name=name
p4=Name()

p4.__setname__("aarif")
print(p4.name)