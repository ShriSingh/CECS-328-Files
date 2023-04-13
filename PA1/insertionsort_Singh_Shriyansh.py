'''
1- Please use the code template below to complete your assignment.
2- Your code must be written in the pa1_insertionsort method. 
3- You can define as many as functions needed but 
4- Your algorithms' execution must be started from the 
   pa1_insertionsort method.
5- Do not change any other code. 
6- The evaluation code uses this template to run your test cases.
   Any changes other than the pa1_insertionsort method would cause 
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
		for i in range(elements_count, 0, -1):
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


	def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		if input_type == "a":
			output = self.function_a(elements_count)
		if input_type == "b":
			output = self.function_b(elements_count)
		if input_type == "c":
			output = self.function_c(elements_count, seed)
		return output	


	def pa1_insertionsort (self, input_type: str, elements_count: int, seed: int) -> list:
		# input_type: a, b, c, d ; elements_count: 1000, 2000, etc.; seed: 1, 2, 3, etc.
		query_list = self.select_input(input_type, elements_count, seed)
		# Length of the array
		n = len(query_list)

		# Getting the start time
		st = time.process_time()
		
    	# your insertion sort algorithm comes here ...

		# Loop that iterates through the array
		for i in range(1, n):
			# Setting the initial element as the key
			key = query_list[i]
			# Setting the initial index as the previous index of the key
			j = i - 1 # j is the index of the previous element of the key
			# Comparing the key with the previous element of the key
			while j >= 0 and key < query_list[j]:
				# Swapping the elements
				query_list[j + 1] = query_list[j]
				# Decrementing the index
				j -= 1
			# Setting key to its sorted position
			query_list[j + 1] = key
    	# end of insertion sort
		
		# Getting the end time
		et = time.process_time()
		# Calculation of elapsed time
		res = et - st

		return [query_list, res]




if __name__ == '__main__':

	# the input type is either a, b or c 
	# corresponding to function_a, function_b and function_c.
	input_type = sys.argv[1]

	elements_count = int(sys.argv[2])

	# input seed as 2, so we have the same randomly 
	# generated array.
	# you can change it for your testing.
	seed = sys.argv[3]
	
	obj = Solution()
	# the return value is an array of array.
	ret = obj.pa1_insertionsort(input_type, elements_count, seed) # type: ignore
	print(ret)

