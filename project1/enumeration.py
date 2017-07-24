#!/usr/bin/python3

# Enumeration
# BY : Dennie Devito, Jared Gregory Wasinger, Rohan Milind Barve 
# CS 325 // Summer 2017 
# Function: enumeration

#---------------------------------------------------------------------------------------------------------------------------------
# Algorithm 1 Instruction : Loop over each pair of indices i, j and compute the sum ∑ 𝐴[𝑘] Keep the best sum you have found so far.
#---------------------------------------------------------------------------------------------------------------------------------

# Returns: maximum sub-array sum, and maximum sub-array



from sys import argv

def enumeration(val):
  
  # Checking if the val array is empty if so the function returns
  if len(val) != 0:
    max_sum = float("-inf")
  else:
    return 0, val

  
  for i in range(len(val)):

    
    for j in range(i, len(val)):
      current_sum = 0
        
      for k in range(i, j + 1):
        current_sum += val[k]
  
        if current_sum > max_sum:
          max_sum = current_sum
          start_idx = i
          end_idx = j

  # Return the max sum and the maximum sub-array
  return max_sum, val[start_idx : end_idx + 1]

if __name__=="__main__":
    insert = open("MSS_TestResults-1.txt","w")
    with open('MSS_TestProblems-1.txt') as f:
        for line in f:
            int_list = [int(i) for i in line.split()]
            max_sum,val =enumeration(int_list)
            insert.write("%s\n" % val)
            insert.write("%s\n" % max_sum)