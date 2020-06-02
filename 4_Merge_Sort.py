def mergeSort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        mergeSort(left)
        mergeSort(right)

        index = j = k = 0

        while index < len(left) and j < len(right):
            if left[index] < right[j]:
                a[k] = left[index]
                index += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while index < len(left):
            a[k] = left[index]
            index += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1


arr = []
num = int(input("Enter Number For insert:"))
for i in range(num):
    value = int(input("Enter Numbers:"))
    arr.append(value)
print("Before Sorting:", arr)

mergeSort(arr)
print("Sorted array is:", arr)
