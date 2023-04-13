'''
Name: Shriyansh Singh
studentID: 028243304

assignment: PA0
'''
import sys

class Solution:

	def data_conversion(self, data, convert_to):
		if convert_to == "int":
			return int(data)

		if convert_to == "list":
			new_input = []
			data = data.split(",")		
			for item in data: 
				new_input.append(int(item))
			
			return new_input

		if convert_to == "bool":
			return bool(data)


	# Writing a bubble sort algorithm to sort a list of numbers
	def pa0 (self, s: list ) -> list:
		sorted_list = s
		'''My code starts here'''
		for i in range(0, len(sorted_list) - 1): # Travserse through all the array elements
			for j in range(0, len(sorted_list) - i - 1): # Traverse through all the array elements that are not sorted
				# Checking if the element is equal to the next element
				if sorted_list[j] == sorted_list[j+1]:
					# Deleting the duplicate element
					# del sorted_list[j] # <- Doesn't work for lists like "2,2,1" for some reason
					continue
				# Checking if the element is greater than the next element
				if sorted_list[j] > sorted_list[j+1]: 
					# Swapping the element with the next element in the list
					temp = sorted_list[j]
					sorted_list[j] = sorted_list[j+1]
					sorted_list[j+1] = temp
		return sorted_list 


if __name__ == '__main__':
	# argv takes the input as a string.
	# to run pa1 we need to convert argv (or input data)
	# to the datatype that pa0 accepts.
	# data_conversion function converts an string to 
	# convert_to variable suitable for pa1 program input. 
	# "convert_to" variable can be one of the followings:
	# "list", "int", "bool"
	# note: a list of integers should be entered as a 
	# comma separated sequence in command line as input for a program.
	# For example, myproject.py 1,2,3,4,5

    # Setting convert_to variable
	convert_to = "list"

	# Read the input string from the command line
	s = sys.argv[1]

	# Craeting an object from Solution class
	obj = Solution()

	# Call "data_conversion" method to convert s (input string )
	# to a desire input datatype that is set for convert_to
	s = obj.data_conversion(s, convert_to)

	# calling tha pa0 mnethod to run the program 
	ret = obj.pa0(s)

	print(ret)
