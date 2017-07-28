def max_subarray(nums):
  maxSum = -float("inf"); endingSummation = -float("inf")

  for i in range(len(nums)):
    if endingSummation > 0:
      endingSummation = endingSummation + nums[i]
    else:
      endingSummation = nums[i]

    if endingSummation > maxSum:
      maxSum = endingSummation
  
  if not (maxSum > 0):
    return 0
  else:
    return maxSum

if __name__=="__main__":
    insert = open("MSS_TestResults-1.txt","w")
    with open('MSS_TestProblems.txt') as f:
        for line in f:
            if line == '\n':
              continue

            arr_str = line.split('],')[0]+']'
            int_list = list(map(lambda x: int(x), arr_str.strip('[').strip(']').split(',')))

            desired_sum = int(line.split(']')[1].strip(','))
            max_sum = max_subarray(int_list)
            insert.write(str(int_list))
            insert.write(", ")
            insert.write(str(max_sum))

            if max_sum != desired_sum:
              raise Exception('sum not equal')
