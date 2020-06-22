"""

Search a sorted array by repeatedly dividing the search interval in half. 
Begin with an interval covering the whole array. 
If the value of the search key is less than the item in the middle of the interval, 
narrow the interval to the lower half. 
Otherwise narrow it to the upper half. 
Repeatedly check until the value is found or the interval is empty.

"""

class BinarySearch:
    
    @staticmethod
    def binarySearch(a, left, right, search_item):
        
        mid = int(left + right) // 2

        # Check base case
        if left > right:
        
            print("Item Not Found!!")
        
        # search item is greater than mid
        elif search_item > a[mid]:
        
            left = mid + 1
        
            binarySearch(a, left, right, search_item)
        
        # search item is less than mid
        elif search_item < a[mid]:
        
            right = mid - 1
        
            binarySearch(a, left, right, search_item)
        
        else:
        
            print("Item found at index " + str(mid))


class Main:
    
    arr = []
    
    num = int(input("Enter Number For insert into array:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Numbers:"))
    
        arr.append(value)
    
    array = sorted(arr)
    
    print("Sorted Array is:", array)

    start = 0

    last = len(arr) - 1

    x = int(input("Enter Item to search:"))

    bs = BinarySearch()
    
    bs.binarySearch(array, start, last, x)