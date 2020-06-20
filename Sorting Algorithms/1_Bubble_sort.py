def bubbleSort(a):
    n = len(a)

    for index in range(n):
        for j in range(0, n - index - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


arr = []
num = int(input("Enter Number For insert:"))
for i in range(num):
    value = int(input("Enter Numbers:"))
    arr.append(value)
print("Before Sorting:", arr)

bubbleSort(arr)
print("Sorted array is:", arr)
