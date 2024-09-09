def counting_sort(arr):
    max_val = max(arr)
    
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    result = [0] * len(arr)

    for num in reversed(arr):
        result[count[num] - 1] = num
        count[num] -= 1
    for i in range(len(arr)):
        arr[i] = result[i]

arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print(arr)
