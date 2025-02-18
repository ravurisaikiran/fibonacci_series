Problem-0
![image](https://github.com/user-attachments/assets/09f3e894-44fc-4eec-a6cd-2483ca9c43b9)


PROBLEM_1 

![image](https://github.com/user-attachments/assets/d912a347-965d-4064-8275-08c6d8f9384f)


Use a Minimum-Heap:
Insert the first element from each array into the minimum-heap.
The heap will always contain the smallest element at the root.
Extract the smallest element and insert the next element from the same array as the extracted element.
Repeat the extraction and insertion until the heap is empty.

Time Complexity proof:


Inserting an element into the heap takes O(log K) where K is the number of arrays.
For each of the K * N elements, you perform an insertion and extraction.
So, the overall time complexity is O(K * N * log K).

PROBLEM-2

![image](https://github.com/user-attachments/assets/ec652cdf-bc45-40de-88d0-d2fa55a227f6)



Use Two Pointers:
One pointer i will iterate over the array.
Another pointer j will track the position to overwrite duplicate elements.
Whenever array[i] != array[i-1], we move array[j] to array[i].
This ensures that only unique elements remain in the array.


Time Complexity proof:


Since we only need one pass through the array, the time complexity is O(N) where N is the number of elements in the array.
