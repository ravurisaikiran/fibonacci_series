import heapq

def merge_k_sorted_arrays(arrays):
    minimum_heap = []
    final_output = []

    for i in range(len(arrays)):
        if arrays[i]:  
            heapq.heappush(minimum_heap, (arrays[i][0], i, 0))  
    while minimum_heap:
        val, arr_idx, ele_idx = heapq.heappop(minimum_heap)
        final_output.append(val)
        if ele_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][ele_idx + 1]
            heapq.heappush(minimum_heap, (next_val, arr_idx, ele_idx + 1))
    return final_output
arrays1 = [[1,3,5,7], [2,4,6,8], [0,9,10,11]]
arrays2 = [[1,3,7], [2,4,8], [9,10,11]]

print(merge_k_sorted_arrays(arrays1))
print(merge_k_sorted_arrays(arrays2))
