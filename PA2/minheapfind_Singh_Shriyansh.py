'''
Please use the code template below to complete your assignment.
Your code must go under pa2 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa2 method would cause the evaluation method 
stop working and you will not get credit for your submission.

name: Shriyansh Singh
studentID: 028243304

Assignment: PA2
'''
import sys
import math


class Solution:
    def pa2(self, arr: list[int], k: int) -> int:
        retval = 0
        print("Input:", arr, "and k =", k)

        """My code starts here"""

        # Writing the min_heapify function to create a min-heap
        def min_heapify(array, i, heap_size):
            left_index = 2 * i + 1  # --> Setting the left index
            right_index = 2 * i + 2  # --> Setting the right index
            smallest = i  # --> Setting the smallest element as the root element

            # Conditional statement to set the smallest element as the left index
            if left_index < heap_size and array[left_index] > array[smallest]:
                smallest = left_index

            # Conditional statement to set the smallest element as the right index
            if right_index < heap_size and array[right_index] > array[smallest]:
                smallest = right_index

            # Conditional statement to check if the smallest element is not the root element
            if smallest != i:
                # Swapping the smallest element with the root element
                array[i], array[smallest] = array[smallest], array[i]
                # Recursively calling the min_heapify function
                min_heapify(array, smallest, heap_size)

        # Writing the build_min_heap function
        def build_min_heap(array):
            # Setting up the heap size to the length of the array
            heap_size = len(array)
            # Running a loop until the heap_size count backwards
            for i in range(math.floor(heap_size // 2), -1, -1):
                # Recursively calling the min_heapify function to the heap_size
                min_heapify(array, i, heap_size)

        # Writing a function to find the kth-smallest element in the array
        def find_kth_smallest(array, k):
            # Setting up the heap size to the length of the array
            heap_size = len(array)
            # Calling the build_min_heap function to create a min-heap
            build_min_heap(array)
            # Running a loop from first element to heap_size - k
            for num in range(1, heap_size - k): # I know "num" is not being accessed, but I couldn't figure out another way
                # Swapping the first element with the last element
                array[0], array[heap_size - 1] = array[heap_size - 1], array[0]
                # Decrementing the heap size
                heap_size -= 1
                # Recursively calling the min_heapify function
                min_heapify(array, 0, heap_size)
            # Storing the kth-smallest element from array to a variable
            kth_smallest_element = array[0]
            # Returning the kth-smallest element
            return kth_smallest_element

        # Writing an print statement to indicate the output
        print("Output:")
        # Calling the find_kth_smallest function and storing it in retval
        retval = find_kth_smallest(arr, k)
        # Returning retval
        return retval

# Please make your function call as
# PA2_yourname.py 2,3,4,5 4


if __name__ == '__main__':
    arr = []
    arrtemp = sys.argv[1].split(",")
    for item in arrtemp:
        arr.append(int(item))

    k = int(sys.argv[2])
    obj = Solution()
    ret = obj.pa2(arr, k)
    print(ret)
