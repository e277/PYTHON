# To count the numbers of characters in the string and store them in a dictionary data structure 
# Write a program to use split and join methods in the string and trace a birthday 
# of a person with a dictionary data structure
# def man_person_birthday(birth_str):
#     num_of_chars = len(birth_str)
#     print("Number of characters:", num_of_chars)

#     for ch in birth_str:
#         print("Character:", ch)

# if __name__ == "__main__":
#     man_person_birthday('1997-01-28')

def enterString():
    str1=input("Enter String:\n")
    dict1={}
    for ch in str1:
        keys=dict1.keys()
        if(ch in keys):
            dict1[ch]=dict1[ch]+1
        else:
            dict1[ch]=1
    print("Dictionary is:\n",dict1)

enterString()


def birth_str():
    bdaystr=input("Enter date of birth:\n")
    bdaylist=bdaystr.split("/")
    bday='-'.join(bdaylist)
    bdaydict={"birthday":bday}
    if 'birthday' in bdaydict:
        print(bdaydict['birthday'])