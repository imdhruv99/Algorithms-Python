"""
Heapsort is a comparison based sorting technique based on a Binary Heap data structure. 
It is similar to selection sort where we first find the maximum element and place the maximum element at the end. 
We repeat the same process for the remaining element.
"""

class HeapSort:

    @staticmethod
    def heapify(arr, n, i): 
        
        # Initialize largest as root 
        largest = i  

        left = 2 * i + 1      
        
        right = left + 1     

        # See if left child of root exists and is 
        # greater than root 
        if left < n and arr[i] < arr[left]: 
        
            largest = left 

        # See if right child of root exists and is 
        # greater than root 
        if right < n and arr[largest] < arr[right]: 
        
            largest = right 

        # Change root, if needed 
        if largest != i: 
        
            arr[i],arr[largest] = arr[largest],arr[i]  # swap 

            # Heapify the root. 
            HeapSort.heapify(arr, n, largest) 


    # The main function to sort an array of given size 
    @staticmethod
    def heapSort(arr): 
        
        n = len(arr) 

        # Build a maxheap. 
        # Since last parent will be at ((n//2)-1) we can start at that location. 
        for i in range(n // 2 - 1, -1, -1): 
        
            HeapSort.heapify(arr, n, i) 

        # One by one extract elements 
        for i in range(n-1, 0, -1): 
        
            arr[i], arr[0] = arr[0], arr[i]   # swap 
        
            HeapSort.heapify(arr, i, 0) 


class Main:

    arr = []
    
    num = int(input("Enter Number For how much elements you wants to sort:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Non-Negative Numbers:"))
    
        arr.append(value)
    
    print("Before Sorting:", arr)

    hs = HeapSort()

    hs.heapSort(arr)
    
    print("Sorted array is:", arr)