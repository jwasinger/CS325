#-------------------------------------------------------------------------------
# Function:			linearTime
# Description:      Calculates the maximum sub-array and the sum using
#					the Kadane's algorithm.
# Receives:         values - list of integers
# Returns:          maximum sub-array sum, and maximum sub-array
# Preconditions:    "array" contains at least 1 positive integer
# ------------------------------------------------------------------------------
def linearTime(array):
	# Initialize to -Infinity so that any computed sum will be greater
	maxSum = -float("inf")
	endSum = -float("inf")

	for i in range(len(array)):

		# Index of sub-array that ends with current index
		endHighIndex = i

		# If the sum to this point is positive, continue the running sum
		if endSum > 0:
			endSum = endSum + array[i]
		# Otherwise, start the running sum from here
		else:
			endLowIndex = i
			endSum = array[i]

		# If running sum is highest so far, save the sum and the indices
		if endSum > maxSum:
			maxSum = endSum
			startIndex = endLowIndex
			endIndex = endHighIndex

	# Return the maximum sub-array sum, and the maximum sub-array itself
	return maxSum, array[startIndex : endIndex + 1]

if __name__=="__main__":
	insert = open("MSS_TestResults-1.txt","w")
	with open('MSS_TestProblems-1.txt') as f:
		for line in f:
			int_list = [int(i) for i in line.split()]
			max_sum,values =linearTime(int_list)
			insert.write("%s\n" % values)
			insert.write("%s\n" % max_sum)
