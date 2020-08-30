"""
Radix sort is a sorting technique that sorts the elements by 
first grouping the individual digits of the same place value. 
Then, sort the elements according to their increasing/decreasing order.

"""


class RadixSort:

    @staticmethod
    def radixSort(a):
        
        """
        sort elements by power using buckets to store list based on integer columns
        """

        base = 10

        n = 0

        # finding max number and getting length of digits

        maxDigit = len(str(max(a)))

        while maxDigit > n:

            # create 2d array for buckets
            bucket = [[] for _ in range(10)]

            # split the list
            for i in a:
                
                # add remainder to bucket in position based on column

                bucket[i // (base ** n) % 10].append(i)

            index = 0

            # Loop through bucket
            for i in range(len(bucket)):
                
                # find lists of numbers in bucket
                stageTwo = bucket[i]

                for nums in stageTwo:
                    
                    # add sorted list into original list
                    a[index] = nums

                    index += 1

            # increasing the power of N
            n += 1


class Main:

    arr = []
    
    num = int(input("Enter Number For how much elements you wants to sort:\t"))
    
    for i in range(num):
    
        value = int(input("Enter Non-Negative Numbers:"))
    
        arr.append(value)
    
    print("Before Sorting:", arr)

    rs = RadixSort()
    
    rs.radixSort(arr)
    
    print("Sorted array is:", arr)