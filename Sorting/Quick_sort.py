# Quick Sor in python
def partition(arr,low,high):
    pivot = arr[(low + high) // 2]
    i, j = low, high
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i

def quick(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick(arr, low, pi - 1)
        quick(arr, pi, high)

arr = [8, 7, 2, 1, 0, 9, 6]
print("Original array:")
print(arr)
quick(arr, 0, len(arr) - 1)
print("Sorted array:")
print(arr)
