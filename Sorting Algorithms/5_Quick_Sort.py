"""

QuickSort is a Divide and Conquer algorithm. 
It picks an element as pivot and partitions the given array around the picked pivot.
There are many different versions of quickSort that pick pivot in different ways.
1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, 
given an array and an element x of array as pivot, 
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, 
and put all greater elements (greater than x) after x. All this should be done in linear time.

"""

class QuickSort:

    @staticmethod
    def partition(array, low, high):
        
        # index of smaller element 
        i = (low - 1)
        
        # pivot
        pivot = array[high]
        
        for j in range(low, high):
            
            # If current element is smaller than the pivot 
            if array[j] <= pivot:
                
                # increment index of smaller element 
                i += 1
        
                array[i], array[j] = array[j], array[i]
        
        array[i + 1], array[high] = array[high], array[i + 1]
        
        return i + 1

    # The main function that implements QuickSort 
    # arr[] --> Array to be sorted, 
    # low  --> Starting index, 
    # high  --> Ending index 
    @staticmethod
    def quickSort(a, low, high):
        
        if low < high:
            
            # pi is partitioning index, arr[p] is now
            # at right place 
            pi = partition(a, low, high)

            # Separately sort elements before 
            # partition and after partition 
            quickSort(a, low, pi - 1)
        
            quickSort(a, pi + 1, high)


class Main:
    
    arr = []
    
    num = int(input("Enter Number For how much elements you wants to sort:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Numbers:"))
    
        arr.append(value)
    
    print("Before Sorting:", arr)
    
    n = len(arr)

    qs = QuickSort()

    qs.quickSort(arr, 0, n -1)

    print("Sorted array is:", arr)
