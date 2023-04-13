'''
1- Please use the code template below to complete your assignment.
2- Your code must be written in the pa1_mergesort method. 
3- You can define as many as functions needed but 
4- Your algorithms' execution must be started from the 
   pa1_mergesort method.
5- Do not change any other code. 
6- The evaluation code uses this template to run your test cases.
   Any changes other than the pa1_mergesort method would cause 
   the evaluation program error and you will not get credit for your
   submission.


Name: Shriyansh Singh
Student ID: 028243304

Assignment: PA1
'''

import sys
import random
import time
import math

class Solution:
	
# this function returns a descending sorted array.
	def function_a (self, elements_count: int) -> list:
		output = []
		for i in range(elements_count,0, -1):
			output.append(i)
		return output

	# this function returns an ascending sorted array.	
	def function_b (self, elements_count: int) -> list:
		output = []
		for i in range(1, elements_count):
			output.append(i)
		return output

	# this function returns a randomly generated array	
	def function_c(self, elements_count: int, seed: int):
		output = []
		random.seed(seed)
		for i in range(0, elements_count + 1):
			output.append(random.randint(1, 1000000))

		return output

	# this function selects a correct action based on the input a, b or c.	
	def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		if input_type == "a":
			output = self.function_a(elements_count)
		if input_type == "b":
			output = self.function_b(elements_count)
		if input_type == "c":
			output = self.function_c(elements_count, seed)
		return output	

	def pa1_mergesort (self, input_type: str, elements_count: int, seed: int) -> list:
		# input_type: a, b, c, d ; elements_count: 1000, 2000, etc.; seed: 1, 2, 3, etc.
		query_list = self.select_input(input_type, elements_count, seed)
		# Length of the array
		n = len(query_list)

		# Getting the start time
		st = time.process_time()

    	# your merge sort algorithm comes here ...

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

		MergeSort(query_list, 0, n - 1) 
    	# end of merge sort
		
		# Getting the end time
		et = time.process_time()
		# Calculating elapsed time
		res = et - st

		return [query_list, res] # Return the sorted array and the elapsed time



if __name__ == '__main__':
	# the input type is either a, b or c 
	# corresponding to function_a, function_b and functin_c.
	input_type = sys.argv[1]

	elements_count = int(sys.argv[2])

	# input seed as 2, so we have the same randomly 
	# generated array.
	# you can change it for your testing.
	seed = sys.argv[3]
	
	obj = Solution()
	sys.setrecursionlimit(100000)
	# the return value is an array of array.
	ret = obj.pa1_mergesort(input_type, elements_count, seed)  # type: ignore
	print(ret)