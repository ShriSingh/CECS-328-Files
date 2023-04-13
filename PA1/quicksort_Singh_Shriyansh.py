'''
1- Please use the code template below to complete your assignment.
2- Your code must be written in the pa1_quicksort method. 
3- You can define as many as functions needed but 
4- Your algorithms' execution must be started from the 
   pa1_quicksort method.
5- Do not change any other code. 
6- The evaluation code uses this template to run your test cases.
   Any changes other than the pa1_quicksort method would cause 
   the evaluation program error and you will not get credit for your
   submission.


Name: Shriyansh Singh
Student ID: 028243304

Assignment: PA1
'''
import sys
import random
import time

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
		for i in range(0,elements_count+1):
			output.append(random.randint(1,1000000))

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

	def pa1_quicksort (self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		query_list = self.select_input(input_type, elements_count, seed)
		
		n = len(query_list)

		# get the start time
		st = time.process_time()
		
    	# your quicksort algorithm comes here ...

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

		# Calling the QuickSort function inside the pa1_quicksort() function
		QuickSort(query_list, 0, n - 1)
    	# end of quicksort
		
		et = time.process_time()
		res = et - st

		return [query_list, res]



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
	sys.setrecursionlimit(1000000)
	# the return value is an array of array.
	ret = obj.pa1_quicksort(input_type, elements_count, seed) # type: ignore
	print(ret)

