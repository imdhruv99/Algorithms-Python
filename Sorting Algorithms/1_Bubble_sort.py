"""
Bubble Sort is the simplest sorting algorithm that works by 
repeatedly swapping the adjacent elements if they are in wrong order.

"""


class BubbleSort:
    
    @staticmethod
    def bubbleSort(a):
    
        n = len(a)

        # Traverse through all array elements
        for index in range(n):

            # Optimization Flag
            swapped = False
            
            # Last i elements are already in place 
            for j in range(0, n - index - 1):
                
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if a[j] > a[j + 1]:
    
                    a[j], a[j + 1] = a[j + 1], a[j]

                    swapped = True
            
            # IF no two elements were swapped 
            # by inner loop, then break 
            if swapped == False:

                break   


class Main:
    
    arr = []
    
    num = int(input("Enter Number For how much elements you wants to sort:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Numbers:"))
    
        arr.append(value)
    
    print("Before Sorting:", arr)

    bs = BubbleSort()
    
    bs.bubbleSort(arr)
    
    print("Sorted array is:", arr)