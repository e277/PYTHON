# Write a code for the following input / Outputs
# Input
# “Tamil language is the oldest Language”
# Ouput
# [‘Tamil’, ‘language’, ‘is’, ‘the’, ‘oldest ‘, ‘Language’]
def split_string(word_string):
    print("\nOriginal string:", word_string)
    word_list = []
    for i in word_string.split(" "):
        word_list.append(i.strip())
    return word_list

if __name__ == "__main__":
    print("List of languages:", split_string("Tamil language is the oldest Language"))

# Input
# “Jamaican Food”
# Ouput
# Doof naciamaJ
def reversed_string(o_string):
    print("\nOriginal string:", o_string)
    rev_string = ""
    for i in o_string:
        rev_string = i + rev_string
    return rev_string

if __name__ == "__main__":
    print("Reversed string: ", reversed_string("Jamaican Food"))
