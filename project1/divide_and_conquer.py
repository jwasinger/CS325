#!/usr/bin/python3

# Enumeration
# BY : Dennie Devito, Jared Gregory Wasinger, Rohan Milind Barve 
# CS 325 // Summer 2017 
# Function: enumeration

#---------------------------------------------------------------------------------------------------------------------------------
# Algorithm 3 Instruction : If we split the array into two halves, we know that the maximum subarray will either be
#                           -  Contained entirely in the first half
#                           -  Contained entirely in the second half or
#                           -  Made of a suffix of the first half of the subarray and a prefix of the second half
#---------------------------------------------------------------------------------------------------------------------------------

# Returns: maximum sub-array sum, and maximum sub-array

from sys import argv

def div_and_conq(values):
    # Checking if the values array is either empty or only contains
    # a single element
    if len(values) == 0:
        return 0, values
    elif len(values) == 1:
        return values[0], values

    # Initializing variables to track the maximums and the indices for the
    # middle max subarray to check against the left and right halves
    tempmax = 0
    midmax = 0
    midstart = 0
    midend = 0

    leftmax = 0
    rightmax = 0

    # Calculating and storing the index at which the array is cut in approx.
    # half
    midpoint = int(len(values) / 2)

    midstart = midpoint
    midend = midpoint

    # Reverse iterating through the values array starting from the midpoint
    # and ending at the first element
    for i in reversed(range(midpoint)):
        tempmax += values[i]
        if tempmax > leftmax:
            leftmax = tempmax
            midstart = i

    # Resetting the tempmax variable
    tempmax = 0

    # Iterating through the right half of the values array to determine
    # the maximum right subarray
    for i in range(midpoint, len(values)):
        tempmax += values[i]
        if tempmax > rightmax:
            rightmax = tempmax
            midend = i + 1

    # Summing the leftmax and rightmax and setting that to be the midmax
    midmax = leftmax + rightmax

    # Recursively calling the main method to act on the left and 
    # right halves of the values array
    leftmax, leftsubarr = div_and_conq(values[:midpoint])
    rightmax, rightsubarr = div_and_conq(values[midpoint:])

    # If-else block used to determine the biggest subarray max
    # and to return that max with the subarray it reflects
    if midmax >= leftmax and midmax >= rightmax:
        return midmax, values[midstart:midend]
    elif leftmax >= rightmax and leftmax > midmax:
        return leftmax, leftsubarr
    elif rightmax > leftmax and rightmax > midmax:
        return rightmax, rightsubarr

if __name__=="__main__":
    insert = open("MSS_TestResults-1.txt","w")
    with open('MSS_TestProblems-1.txt') as f:
        for line in f:
            int_list = [int(i) for i in line.split()]
            max_sum,values =div_and_conq(int_list)
            insert.write("%s\n" % values)
            insert.write("%s\n" % max_sum)