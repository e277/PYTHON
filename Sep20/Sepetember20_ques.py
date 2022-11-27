# 1. Program to accept the strings which contains all vowels
# Given a string, the task is to check if every vowel is present or not. 
# We consider a vowel to be present if it is present in upper case or lower case. 
# i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .
from collections import Counter


# def check_str(str):
#     lc_str = str.lower()
#     list_of_vowels = ['a', 'e', 'i', 'o', 'u']
#     vowels_from_word = []

#     for i in lc_str:
#         if i in list_of_vowels:
#             vowels_from_word.append(i)

#     # return list_of_vowels, vowels_from_word
#     if len(vowels_from_word) == len(list_of_vowels):
#         return True
#     return False

# if __name__ == '__main__':
#     print(check_str('EUlOgIA'))

# 2. Program to check if a string contains any special character
# def check_special_ch(str2):
#     symbols = ['`','~','!','@','#','$','%','^','&']

#     return [i for i in str2 if i in symbols]
    

# if __name__ == '__main__':
#     print("The list of special characters:", check_special_ch('ezramuir12@gmail.com'))

# 3. Python program to create a list of tuples from given list having number and its cube in each tuple
# def list_to_tuple(list3):
#     print("List of Elements:", list3)
#     to_tuple = tuple(list3)
#     print("Tuple of Elements:", to_tuple)
#     # print(to_tuple)
#     cube_of_el = tuple((x**3 for x in to_tuple))
#     return cube_of_el

# if __name__ == '__main__':
#     print("Cube of tuple el:", list_to_tuple([1,2,3,4,5,6,7]))

# 4. Python program to create all pair combinations of 2 tuples
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
# def tuple_comb(tup1, tup2):
#     matches_xy = [(x,y) for x in tup1 for y in tup2]
#     matches_yx = [(y,x) for x in tup1 for y in tup2]

#     list_of_matches = matches_xy + matches_yx

#     return list_of_matches

# if __name__ == "__main__":
#     print(tuple_comb((7,2), (7,8)))

# 5. Python program to find the sum of all items in a dictionary
# def sum_of_items(dict_ny):
#     sum = 0
#     for value in dict_ny.values():
#         sum += value
#     return sum

# if __name__ == "__main__":
#     print("The sum of the values is:", sum_of_items({'a': 11, 'b': 12, 'c': 43, 'd': 54, 'e': 65}))

# 6.Ways to sort list of dictionaries by values in Python – Using lambda function
# def sort_dict_by_values(dict_vals):
#     return sorted(dict_vals.items(), key=lambda item: item[1])

# if __name__ == '__main__':
#     print(sort_dict_by_values({'a': 61, 'b': 12, 'c': 3, 'd': 24, 'e': 5}))

# 7. Python Counter to find the size of largest subset of anagram words
# def largest_subset_of_words(words):
#     input = words.split(' ')
#     for i in range(len(input)):
#         input[i] = ''.join(sorted(input[i]))

#     freq = Counter(input)

#     return max(freq.values()), max(freq.keys())

# if __name__ == '__main__':
#     print(largest_subset_of_words("ant magenta magnate tan gnamate"))

# 8. Program to print the pattern ‘G’
def dis_pattern_G():
    result_str="";    
    for row in range(0,7):    
        for column in range(0,7):     
            if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):  
                result_str=result_str+"*"    
            else:      
                result_str=result_str+" "    
        result_str=result_str+"\n"    
    print(result_str);

if __name__ == '__main__':
    dis_pattern_G()

# 9. How to convert timestamp string to datetime object in Python?


# 10. What is the output of the following program?


# data = 50

# try:

# data = data/0

# except ZeroDivisionError:

# print('Cannot divide by 0 ', end = '')

# else:

# print('Division successful ', end = '')



# try:

# data = data/5

# except:

# print('Inside except block ', end = '')

# else:

# print('GFG', end = '')