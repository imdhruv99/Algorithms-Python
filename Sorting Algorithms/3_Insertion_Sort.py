def insertionSort(a):
    for index in range(1, len(a)):
        key = a[index]
        j = index - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


arr = []
num = int(input("Enter Number For insert:"))
for i in range(num):
    value = int(input("Enter Numbers:"))
    arr.append(value)
print("Before Sorting:", arr)

insertionSort(arr)
print("Sorted array is:", arr)
