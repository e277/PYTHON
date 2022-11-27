# 1. Python program to check if the list contains three consecutive common numbers in Python
# def com_3_con(list_1):
#     count = 1
#     for i in range(0, len(list_1)):
#         if list_1[i-1] == list_1[i]:
#             count += 1
#             if count == 3:
#                 print("Repeated 3 consecutive times:", list_1[i])

# if __name__ == "__main__":
#     com_3_con([1,3,4,5,6,7,7,7])


# 2. Python Program for Print Number series without using any loop
# Problem – Givens Two number N and K, our task is to subtract a number K from N 
# until number(N) is greater than zero, once the N becomes negative or zero then 
# we start adding K until that number become the original number(N). 
# Note : Not allow to use any loop. 

# Examples :
# Input : N = 15 K = 5
# Output : 15 10 5 0 5 10 15
# Input : N = 20 K = 6
# Output : 20 14 8 2 -4 2 8 14 20
# def num_series(n, N, k, track):
#     print(n, end=' ')
#     if n <= 0:
#         if track == 0:
#             track = 1
#         else:
#             track = 0
        
#     if (n == N and not(track)):
#         return

#     if track == True:
#         num_series(n-k, N, k, track)
#         return

#     if not(track):
#         num_series(n+k, N, k, track)
#         return

# if __name__ == '__main__':
#     print()
#     print("N=15, K=5 ")
#     num_series(15, 15, 5, True)
#     print("\n")
#     print("N=20, K=6 ")
#     num_series(20, 20, 6, True)
#     print()


# 3. Check if a triangle of positive area is possible with the given angles
# Given three angles. The task is to check if it is possible to have a 
# triangle of positive area with these angles. If it is possible print “YES” else print “NO”.

# Examples:
# Input : ang1 = 50, ang2 = 60, ang3 = 70
# Output : YES
# Input : ang1 = 50, ang2 = 65, ang3 = 80
# Output : NO
# def create_tri(ang1, ang2, ang3):
#     sum_of_angles = ang1 + ang2 + ang3
#     if sum_of_angles == 180:
#         print("YES")
#     else:
#         print("NO")

# if __name__ == '__main__':
#     create_tri(50, 60, 70)
#     create_tri(50, 65, 80)


# 4. Python Program for Check if all digits of a number divide it
# Given a number n, find whether all digits of n divide it or not.
# Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Input : 130
# Output : No
# def num_div_by_digits(number):
#     s_number = str(number)
    
#     for i in s_number:
#         if number % int(i) == 0:
#             print("Yes")
#         else:
#             print("No")
    

# if __name__ == "__main__":
#     num_div_by_digits(128)
#     print()
#     # num_div_by_digits(130) # getting modulo division error with 0
#     num_div_by_digits(136)


# 5. Python program to Extract digits from Tuple list
# Input : test_list = [(15, 3), (3, 9)]
# Output : [9, 5, 3, 1]
def extract_digits(test_list):
    digits = ""
    for i in test_list:
        for j in i:
            digits += str(j)

    extract_digits = list(map(int, set(digits)))
    print(extract_digits)

if __name__ == '__main__':
    extract_digits([(15, 3), (3, 9)])

