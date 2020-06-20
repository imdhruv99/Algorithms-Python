def selectionSort(a):
    for index in range(len(a)):
        minimum = index
        for j in range(index + 1, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[index], a[minimum] = a[minimum], a[index]


arr = []
num = int(input("Enter Number For insert:"))
for i in range(num):
    value = int(input("Enter Numbers:"))
    arr.append(value)
print("Before Sorting:", arr)

selectionSort(arr)
print("Sorted array is:", arr)
