"""

Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

"""

class InsertionSort:

    @staticmethod
    def insertionSort(a):
        
        # Traverse through 1 to len(arr) 
        for index in range(1, len(a)):
        
            key = a[index]

            # Move elements of arr[0..i-1], that are 
            # greater than key, to one position ahead 
            # of their current position 
            j = index - 1
        
            while j >= 0 and key < a[j]:
        
                a[j + 1] = a[j]
        
                j -= 1
        
            a[j + 1] = key

class Main:

    arr = []
    
    num = int(input("Enter Number For how much elements you wants to sort:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Numbers:"))
    
        arr.append(value)
    
    print("Before Sorting:", arr)

    Is = InsertionSort()

    Is.insertionSort(arr)
    
    print("Sorted array is:", arr)
