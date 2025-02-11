def remove_all_repeated_elements(arr):
    if not arr:
        return arr
        j = 0
        for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    return arr[:j+1]
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print(remove_all_repeated_elements(array1))
print(remove_all_repeated_elements(array2))
