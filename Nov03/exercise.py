# Python Program for Selection Sort
# The selection sort algorithm sorts an array by repeatedly finding the minimum element 
# (considering ascending order) from unsorted part and putting it at the beginning. 
# The algorithm maintains two subarrays in a given array. 

# 1) The subarray which is already sorted. 
# 2) Remaining subarray which is unsorted. In every iteration of selection sort, 
# the minimum element (considering ascending order) from the unsorted subarray is 
# picked and moved to the sorted subarray. try to do Insertion sort is a simple sorting algorithm 
# that works the way we sort playing cards in our hands.

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])
        # print(arr[i])

    print("\nArray in sorted order: ", arr)


def main():
    selectionSort([-2, 45, 0, 11, -9, 88, -97, -202, 747])

if __name__ == "__main__":
    main()
