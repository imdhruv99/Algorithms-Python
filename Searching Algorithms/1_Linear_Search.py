def linearSearch(a, search_item):
    i = flag = 0
    while i < len(a):
        if a[i] == search_item:
            flag = 1
            break
        i += 1

    if flag == 1:
        print("Item found at position:", i + 1)
    else:
        print("Item Not Found!!")


arr = []
num = int(input("Enter Number For insert:"))
for i in range(num):
    value = int(input("Enter Numbers:"))
    arr.append(value)
print("Array is:", arr)

x = int(input("Enter Item to search:"))
linearSearch(arr, x)

