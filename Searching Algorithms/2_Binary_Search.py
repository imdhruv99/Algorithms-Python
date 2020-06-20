def binarySearch(a, left, right, search_item):
    mid = int(left + right) // 2

    if left > right:
        print("Item Not Found!!")
    elif search_item > a[mid]:
        left = mid + 1
        binarySearch(a, left, right, search_item)
    elif search_item < a[mid]:
        right = mid - 1
        binarySearch(a, left, right, search_item)
    else:
        print("Item found at index " + str(mid))


arr = []
num = int(input("Enter Number For insert:"))
for i in range(num):
    value = int(input("Enter Numbers:"))
    arr.append(value)
array = sorted(arr)
print("Sorted Array is:", array)

start = 0
last = len(arr) - 1
x = int(input("Enter Item to search:"))


binarySearch(array, start, last, x)

