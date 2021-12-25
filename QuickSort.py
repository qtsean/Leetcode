def sortArr(arr):
    quickSort(arr, 0, len(arr) - 1)
    print(arr)


def quickSort(arr, left, right):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quickSort(arr, left, pivot - 1)
    quickSort(arr, pivot + 1, right)


def partition(arr, left, right):
    i = left
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


# arr = [7, 6, 4, 9, 3, 2, 8, 1, 5]
arr = [2, 1]
sortArr(arr)
