'''Divide and Conquer Approach in Sorting Algorithms'''
import math

# Insertion Sort
'''This code sorts a list of numbers. The sorting is done by comparing
the first two numbers and swapping them if they are out of order.
Then the first three numbers are compared and swapped if necessary.
This process is repeated until the last two numbers are compared and
swapped if necessary.'''
def InsertionSort(A, n):
    for i in range(1, n):
        key = A[i] # 1.Key is equal to the i-th element of the array
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j] # 2. A[j + 1] is equal to A[j]
            j -= 1
        A[j + 1] = key # 3. A[j + 1] is equal to key
        

# Writing a MergeSort algorithm
'''
Merge() takes two sorted subarrays of A and then merges them into a single sorted subarray of A
(How many should this take?: 2n)
'''
def Merge(Array, left, mid, right):
	# Calculating the size of the left subarray
	n1 = mid - left + 1
	# Calculating the size of the right subarray
	n2 = right - mid
	# Creating two temporary subarrays
	L = [0] * (n1) # Left subarray
	R = [0] * (n2) # Right subarray

	# Copying the elements to the left subarray
	for i in range(0, n1):
		L[i] = Array[left + i]

	# Copying the elements to the right subarray
	for j in range(0, n2):
		R[j] = Array[mid + 1 + j]

	# Indexes of the subarrays
	i = j = 0 # Initial index of the 1st and 2nd subarrays	
	k = left # Initial index of the merged subarray

	while i < n1 and j < n2:
		# Comparing the first element of the left subarray with the first element of the right subarray
		if L[i] <= R[j]:
			Array[k] = L[i]
			i += 1
		else:
			Array[k] = R[j]
			j += 1
			k += 1
			
	# Copying the remaining elements of the left subarray
	while i < n1:
		Array[k] = L[i]
		# Incrementing the index of the left subarray
		i += 1
		# Incrementing the index of the merged subarray
		k += 1
			
	# Copying the remaining elements of the right subarray
	while j < n2:
		Array[k] = R[j]
		# Incrementing the index of the right subarray
		j += 1
		# Incrementing the index of the merged subarray
		k += 1

# Merge Sort function to call the Merge function and recursively call itself
def MergeSort(Array, left, right):
	if (left < right):
		# Calculating the mid value
		mid_value = math.floor((left + right) / 2) # using floor function to get the integer value
		# Recursively calling the MergeSort function
		MergeSort(Array, left, mid_value)
		MergeSort(Array, mid_value + 1, right)
		# Calling the Merge function
		Merge(Array, left, mid_value, right)



'''Divide-and-Conquer Approach: Finding Maximum-Subarray'''
# Writing a Maximum-Subarray algorithm
def findMaxSubArray(A,):
    max = []
    curren_Max = []
    start = 0
    end = 0
    m_start = 0
    m_end = 0


'''Multiplying Matrices'''
'''Assume the input matrices are square[each matrix's # of rows = # of columns]
   Or the rows/columns of the input matrics must be a power of 2'''
'''Average case: Θ(n^3)'''
# Writing a function to multiply two matrices
def Square_Matrix_Multiply(A, B): # A, B are square matrices
    n = len(A) # -> n = # of rows = # of columns
    # Let C be the new n X n matrix 
    C = []
    for i in range(1, n):
        for j in range(1, n):
            C[i][j] = 0
            for k in range(1, n):
                C[i][j] += A[i][k] * B[k][j] # C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C

'''
def Square_Matrix_Multiply_Recursive(A, B):
    n = len(A)
    C = []
    P = []
    if n == 1:
        C[1][1] = A[1][1] * B[1][1]
    else:
        P[1] = Square_Matrix_Multiply_Recursive(A[1][2] - A[2][2], B[2][1] + B[2][2])
        P[2] = Square_Matrix_Multiply_Recursive(A[1][1] + A[2][2], B[1][1] + B[2][2])
        P[3] = Square_Matrix_Multiply_Recursive(A[1][1] - A[2][1], B[1][1] + B[1][2])
        P[4] = Square_Matrix_Multiply_Recursive(A[1][1] + A[1][2], B[2][2])
        P[5] = Square_Matrix_Multiply_Recursive(A[1][1], B[1][2] - B[2][2])
        P[6] = Square_Matrix_Multiply_Recursive(A[2][2], B[2][1] - B[1][1])
        P[7] = Square_Matrix_Multiply_Recursive(A[2][1] + A[2][2], B[1][1])

        C[1][1] = P[1] + P[2] - P[4] + P[6]
        C[1][2] = P[4] + P[5]
        C[2][1] = P[6] + P[7]
        C[2][2] = P[2] + P[3] - P[5] + P[7]
    
    return C
'''

'''
Notes on QuickSort:
- QuickSort is a Divide-and-Conquer and a Recursive algorithm
- Sorts in place
- Sorts in (n log n) time in the average case
- Sorts in (n^2) time in the worst case
'''
# Writing the Partition function
def Partition(Array, left, right):
    # Setting up the pivot index as the rightmost element
    pivot_index = Array[right]
    # Setting up the index of the smallest element
    i = left - 1
    # Going through the array from left to right
    for j in range(left, right):
        # If the current element is smaller than or equal to the pivot
        if Array[j] <= pivot_index:
            # Increment the index of the smallest element to swap with the greater element
            i += 1
            # Swap/Exchange Array[i] with Array[j]
            Array[i], Array[j] = Array[j], Array[i]
    # Swap/Exchange Array[i + 1] with Array[right]
    Array[i + 1], Array[right] = Array[right], Array[i + 1]

    # Return the partition position 
    return i + 1

def QuickSort(Array, left, right):
    if (left < right):
        # Setting the pivot to the output of the Partition() function
        partition = Partition(Array, left, right)
        # Recursively calling QuickSort on the left and right subarrays
        QuickSort(Array, left, partition - 1)
        QuickSort(Array, partition + 1, right)

