"""

Merge Sort is a Divide and Conquer algorithm. 
It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. 
The merge() function is used for merging two halves.
The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] 
are sorted and merges the two sorted sub-arrays into one.

"""

class MergeSort:

    @staticmethod
    def mergeSort(a):
        
        if len(a) > 1:
            
            # Finding the mid of the array
            mid = len(a) // 2

            # Dividing the array elements into 2 halves 
            left = a[:mid]
        
            right = a[mid:]

            # Sorting the first half 
            mergeSort(left)

            # Sorting the second half
            mergeSort(right)

            index = j = k = 0

            # Copy data to temp arrays L[] and R[] 
            while index < len(left) and j < len(right):
        
                if left[index] < right[j]:
        
                    a[k] = left[index]
        
                    index += 1
        
                else:
        
                    a[k] = right[j]
        
                    j += 1
        
                k += 1
            
            # Checking if any element was left 
            while index < len(left):
        
                a[k] = left[index]
        
                index += 1
        
                k += 1
        
            while j < len(right):
        
                a[k] = right[j]
        
                j += 1
        
                k += 1


class Main:
    
    arr = []
    
    num = int(input("Enter Number For how much elements you wants to sort:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Numbers:"))
    
        arr.append(value)
    
    print("Before Sorting:", arr)
    
    ms = MergeSort()
    
    ms.mergeSort(arr)
    
    print("Sorted array is:", arr)