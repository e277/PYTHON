# 2. Write a python code for the following: (10 marks)
# Use Method Overriding for the each of the operation
# Input :str = &#39;programiz&#39;
# Outuput:
# str = programiz
# str[0] = p
# str[-1] = z
# str[1:5] = rogr
# str[5:-2] = am
class Question2:
    def sliceStr(self, str):
        print("I am parent slice function: ", str)

class Get_p(Question2):
    def sliceStr(self, str):
        print(str[0])
class Get_z(Question2):
    def sliceStr(self, str):
        print(str[-1])
class Get_rogr(Question2):
    def sliceStr(self, str):
        print(str[1:5])
class Get_am(Question2):
    def sliceStr(self, str):
        print(str[5:-2])


print()
str = 'programiz'
# Creating Objects
p = Get_p()
p.sliceStr(str)

print()
z = Get_z()
z.sliceStr(str)

print()
rogr = Get_rogr()
rogr.sliceStr(str)

print()
am = Get_am()
am.sliceStr(str)
print()


