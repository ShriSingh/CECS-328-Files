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


class Solution:
    def pa2(self, arr: list[int], k: int) -> int:
        retval = 0
        print("Input:", arr, "and k =", k)

        """My code starts here"""

        # Using the Partition function from QuickSort algorithm
        def partition(array, left, right):
            # Setting up the pivot index as the rightmost element
            pivot_index = array[right]
            # Setting up the index of the smallest element
            i = left - 1
            # Going through the array from left to right
            for j in range(left, right):
                # If the current element is smaller than or equal to the pivot
                if array[j] <= pivot_index:
                    # Increment the index of the smallest element to swap with the greater element
                    i += 1
                    # Swap/Exchange Array[i] with Array[j]
                    array[i], array[j] = array[j], array[i]
            # Swap/Exchange Array[i + 1] with Array[right]
            array[i + 1], array[right] = array[right], array[i + 1]

            # Return the partition position
            return i + 1

            # Writing a function to find the kth-smallest element in the array
        def kth_smallest(array, left, right, index):
            # Setting up the variable to the first element of the array
            position = array[0]
            # If index is equal to 0 and smaller than the size of the array
            if index >= 0 and index <= right - left:
                # Paritioning the array from the last element using the partition function
                position = partition(array, left, right)
                # If the position is equal to the index element
                if position - left == index:
                    return array[position]
                # If the position is greater than the index element
                if position - left > index:
                    # Returning the kth-smallest element in the left subarray of the pivot element.
                    # Recursively calling the function
                    return kth_smallest(array, left, position - 1, index)
            # Returning if the index element is located in the right subarray of the pivot element.
            return kth_smallest(array, position, right, index - position + left)

        # Writing an print statement to indicate the output
        print("Output:")
        # Storing the result from kth_smallest function
        retval = kth_smallest(arr, 0, len(arr) - 1, k)
        # Returning the result
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
