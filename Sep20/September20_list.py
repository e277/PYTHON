# Write a Python program to interchange first and last elements in a list by using all the approaches
# Given a list, write a Python program to swap first and last element of the list.

# Examples: 
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
# Input : [1, 2, 3]
# Output : [3, 2, 1]

# Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.
def appr_1(list_1):
    for i in list_1:
        first = list_1[0]
        len_of_list = len(list_1)
        last = list_1[len_of_list - 1]

    first, last = last, first
    
    return list_1

if __name__ == '__main__':
    print()
    print("Approach_1: Original= [12, 35, 9, 56, 24]", "Swapped=", appr_1([12, 35, 9, 56, 24]))
    print("Approach_1: Original= [1, 2, 3]", "Swapped=", appr_1([1, 2, 3]))
    print()

# Approach #2: The last element of the list can be referred as list[-1]. 
# Therefore, we can simply swap list[0] with list[-1].
def appr_2(list_2):
    first = list_2[0]
    last = list_2[-1]

    list_2[0] = last
    list_2[-1] = first

    return list_2

if __name__ == '__main__':
    print("Approach_2: Original= [1, 2, 3, 4]", "Swapped=", appr_2([1, 2, 3, 4]))
    print()

# Approach #3: Swap the first and last element is using tuple variable. 
# Store the first and last element as a pair in a tuple variable, 
# say get, and unpack those elements with first and last element in that list. 
# Now, the First and last values in that list are swapped.
def appr_3(list_3):
    first = list_3[0]
    last = list_3[-1]
    first_last = first, last
    
    # uppack
    (i1, i2) = first_last

    list_3[0], list_3[-1] = i2, i1

    return list_3

if __name__ == "__main__":
    print("Approach_3: Original= [12, 35, 9, 56, 24]", "Swapped=", appr_3([12, 35, 9, 56, 24]))
    print("Approach_3: Original= [1, 2, 3]", "Swapped=", appr_3([1, 2, 3]))
    print()

# Approach #4: Using * operand. 
# This operand proposes a change to iterable unpacking syntax, allowing to specify 
# a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name.
def appr_4(list_4):
    (first, *middle, last) = list_4
    # print(first)
    # print(middle)
    # print(last)
    list_4 = (last, *middle, first)
    return list_4

if __name__ == "__main__":
    print("Approach_4: Original= [6, 7, 8, 9]", "Swapped=", appr_4([6, 7, 8, 9]))
    print()

# Approach #5: Swap the first and last elements is to use the inbuilt function list.pop(). 
# Pop the first element and store it in a variable. Similarly, pop the last element and 
# store it in another variable. Now insert the two popped element at each other’s original position.
def appr_5(list_5):
    first = list_5.pop(0)
    last = list_5.pop()
    list_5.insert(0, last)
    list_5.insert(3, first)
    # print(first, last)
    # print(list_5)
    # print(list_5)
    return list_5 

if __name__ == "__main__":
    print("Approach_5: Original= [6, 7, 8, 9]", "Swapped=", appr_5([6,7,8,9]))
    print()
