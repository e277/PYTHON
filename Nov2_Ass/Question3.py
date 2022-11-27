# 3. Write a program to implement Sorting of elements in an array. (10 marks)
# Use method Overloading to sort in ascending order and descending order.
# Input:
# Given array is 12 11 13 5 6 7
# Output:
# Sorted array (ascending Order) is 5 6 7 11 12 13
# Sorted array (descending Order) is 13 12 11 7 6 5
class Question3:
    temp = 0
    def sortedArr(self, numbers, flag=None):
        if flag == None:
            for i in range(0, len(numbers)):    
                for j in range(i+1, len(numbers)):    
                    if(numbers[i] > numbers[j]):    
                        temp = numbers[i];    
                        numbers[i] = numbers[j]   
                        numbers[j] = temp
    
            print("Elements of array sorted in ascending order: ", end=' ')   
            for i in range(0, len(numbers)):    
                print(numbers[i], end=" ");  
        else:
            for i in range(0, len(numbers)):    
                for j in range(i+1, len(numbers)):    
                    if(numbers[i] < numbers[j]):    
                        temp = numbers[i];    
                        numbers[i] = numbers[j]   
                        numbers[j] = temp
            print("\nElements of array sorted in descending order: ", end=' ')  
            for i in range(0, len(numbers)):
                print(numbers[i], end=" ")    

        
        
print()
numbers = [12, 11, 13, 5, 6, 7]
q3 = Question3()
q3.sortedArr(numbers)
print()
q3.sortedArr(numbers, 'd')
print()
    
