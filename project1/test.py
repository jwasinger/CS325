#! /bin/env python

import time
from random import randint

testSizes = list(range(1000, 11000, 1000))

def gen_test_data(size):
  result = []

  for i in range(0,size):
    result += [randint(-100, 100)]

  return result
    
def capture_times(algo):
  result = {}

  for size in testSizes:
    start = time.time()
    algo(time)
    delta = start - time.time()
    result[size] = delta

  return result

def Algo(l):
  for o in l:
    time.sleep(0.005)
