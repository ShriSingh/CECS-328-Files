
# Writing a Heap Sort Algorithm in Python
import math

'''
Time Taken: T(n) = O(log n) -> Linear Time
'''
def Heapify(A: list, i: int, heap_size: int):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    heap_size = 0

    if left <= heap_size and A[left] > A[i]:
        largest = left
    else:
        largest = i
    
    if right <= heap_size and A[right] > A[largest]:
        largest = right
    
    if largest != i:
        A[i] = A[largest]
        A[largest] = A[i]
        Heapify(A, largest, heap_size)

'''
Run Time: O(n * (log n))
'''
def Build_Heap(A: list):
    heap_size = len(A)
    for i in range(math.floor(len(A) / 2), 0, -1):
        Heapify(A, i, heap_size)

'''
Run Time: 
T(n) = O(n log n) + (n - 1)O(log n)
     = O(n log n) + O(n log n)
     = O(n log n)
'''
def Heap_Sort(A: list):
    Build_Heap(A)
    for i in range(len(A) - 1, 1, -1):
        A[0] = A[i]
        A[i] = A[0]
        heap_size = i
        Heapify(A, 0, heap_size)
    							        								        