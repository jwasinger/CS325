#! /usr/bin/python


def algo(nums):
  maximumSummation= -float("inf")

  for i in range(len(nums)):
    currentMaximumSum= 0
    for j in range(i, len(nums)):
      currentMaximumSum += nums[j]
      if currentMaximumSum < maximumSummation:
        continue
      else:
        maximumSummation = currentMaximumSum

  if maximumSummation > 0:
    return maximumSummation
  else:
    return 0


if __name__=="__main__":
    insert = open("MSS_TestResults-1.txt","w")
    with open('MSS_TestProblems.txt') as f:
        for line in f:
            if line == '\n':
              continue

            arr_str = line.split('],')[0]+']'
            int_list = list(map(lambda x: int(x), arr_str.strip('[').strip(']').split(',')))

            desired_sum = int(line.split(']')[1].strip(','))
            max_sum =algo(int_list)
            insert.write(str(int_list))
            insert.write(", ")
            insert.write(str(max_sum))

            if max_sum != desired_sum:
              import pdb; pdb.set_trace()
              raise Exception('sum not equal')
