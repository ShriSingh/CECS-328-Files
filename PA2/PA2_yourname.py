'''
Please use the code template below to complete your assignment.
Your code must go under pa2 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa2 method would cause the evaluation method 
stop working and you will not get credit for your submission.

name: Your name
studentID: 99999999

assignment:PA2
'''
import sys

class Solution:
	def pa2 (self, arr: list[int], k: int )	-> int:
		retval = 0
		print(arr, k)	
		
		# your code must return an integer
        # for example return True
		
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

