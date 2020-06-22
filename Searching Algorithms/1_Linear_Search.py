"""

linear search or sequential search is a method for finding an element within a list.
It sequentially checks each element of the list until a match is found or the whole list has been searched

"""

class LinearSearch:

    @staticmethod
    def linearSearch(a, search_item):
        
        i = flag = 0
        
        while i < len(a):
            
            # array element is what we want to search then break
            if a[i] == search_item:
                
                flag = 1
        
                break
        
            i += 1

        if flag == 1:
        
            print("Item found at position:", i )
        
        else:
        
            print("Item Not Found!!")


class Main:
    
    arr = []
    
    num = int(input("Enter Number For insert into array:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Numbers:"))
    
        arr.append(value)
    
    print("Array is:", arr)

    x = int(input("Enter Item to search:"))
    
    ls = LinearSearch()

    ls.linearSearch(arr, x)
