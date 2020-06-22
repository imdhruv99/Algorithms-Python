"""

The selection sort algorithm sorts an array by repeatedly finding the minimum element 
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element 
from the unsorted subarray is picked and moved to the sorted subarray.

"""

class SelectionSort:
    
    @staticmethod
    def selectionSort(a):
        
        # Traverse through all array elements 
        for index in range(len(a)):
            
            # Find the minimum element in remaining  
            # unsorted array 
            minimum = index
    
            for j in range(index + 1, len(a)):
    
                if a[minimum] > a[j]:
    
                    minimum = j

            # Swap the found minimum element with  
            # the first element 
            a[index], a[minimum] = a[minimum], a[index]

class Main:

    arr = []
    
    num = int(input("Enter Number For how much elements you wants to sort:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Numbers:"))
    
        arr.append(value)
    
    print("Before Sorting:", arr)

    
    ss = SelectionSort()
    
    ss.selectionSort(arr)
    
    print("Sorted array is:", arr)
