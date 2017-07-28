#! /usr/bin/python


def max_subarray(val):
  max_sum = float("-inf")
  
  for outer in range(len(val)):
    for inner in range(outer, len(val)):
      current_sum = 0
        
      for k in range(outer, inner + 1):
        current_sum += val[k]
  
        if current_sum < max_sum:
          continue
        else:
          max_sum = current_sum

  if max_sum < 0:
    return 0
  else:
    return max_sum

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
              import pdb; pdb.set_trace()
              raise Exception('sum not equal')
