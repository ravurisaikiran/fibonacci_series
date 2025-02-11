def remove_all_repeated_elements(arr):
    if not arr:
        return arr
    
    # Pointer for the position of unique elements
    j = 0
    
    # Iterate through the array
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    # The array is now truncated up to index j
    return arr[:j+1]

# Test the function
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print(remove_all_repeated_elements(array1))
print(remove_all_repeated_elements(array2))
