def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        already_sorted = True
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        if already_sorted:
            break
    return arr

array = [38, 27, 43, 3, 9, 82, 43, 0, -1]
sorted_array = bubble_sort(array)
print(sorted_array)
