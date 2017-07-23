#-------------------------------------------------------------------------------
# Function:			betterEnumeration
# Description:      Calculates the maximum sub-array and and associated sum using
#					the "better enumeration" algorithm.
# Receives:         values - list of integers
# Returns:          maximum sub-array sum, and maximum sub-array
# Preconditions:    "array" contains at least 1 positive integer
# ------------------------------------------------------------------------------
def betterEnumeration(array):
	# Initialize to -Infinity so that any computed sum will be greater
	maxSum= -float("inf")

	# Loop over starting index over list of values
	for i in range(len(array)):

		# Keep a track of running sum for each starting index
		currSum= 0

		# loop ending index over list of values
		for j in range(i, len(array)):
			currSum += array[j]

			# If running sum is highest seen, save the sum and the indices
			if currSum > maxSum:
				maxSum = currSum
				startIndex = i
				endIndex = j

	# Return the maximum sub-array sum, and the maximum sub-array itself
	return maxSum, array[startIndex : endIndex + 1]

if __name__=="__main__":
	insert = open("MSS_TestResults-1.txt","w")
	with open('MSS_TestProblems-1.txt') as f:
		for line in f:
			int_list = [int(i) for i in line.split()]
			max_sum,values =betterEnumeration(int_list)
			insert.write("%s\n" % values)
			insert.write("%s\n" % max_sum)
