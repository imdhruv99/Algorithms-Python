def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quickSort(a, low, pi - 1)
        quickSort(a, pi + 1, high)


arr = []
num = int(input("Enter Number For insert:"))
for i in range(num):
    value = int(input("Enter Numbers:"))
    arr.append(value)
print("Before Sorting:", arr)
n = len(arr)

quickSort(arr, 0, n -1)
print("Sorted array is:", arr)
