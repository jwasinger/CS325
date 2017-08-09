from pulp import *

# declare your variables
num_polyester = LpVariable("num_polyester", 10000, 14000, cat='Integer')
num_b1 = LpVariable("num_b1", 13000, 16000, cat='Integer')
num_silk = LpVariable("num_silk", 6000, 7000, cat='Integer')
num_b2 = LpVariable("num_b2", 6000, 8500, cat='Integer')

totalPrice = LpVariable("totalPrice")
 
# defines the problem
prob = LpProblem("problem", LpMaximize)

#materials constraints

supply = [150, 450, 250, 150] 
prices = [
  [10, 11, 13, None], #W1
  [15, 8, 8, 14], #W2
  [None, None, 9, 8] #W3
]

sources = [1,2,3,4]
warehouses = [1,2,3] 
num_trips = [
  [LpVariable("p1w1"), LpVariable("p2w1"), LpVariable("p3w1"), LpVariable("p4w1")],
  [LpVariable("p1w2"), LpVariable("p2w2"), LpVariable("p3w2"), LpVariable("p4w2")],
  [LpVariable("p1w3"), LpVariable("p2w3"), LpVariable("p3w3"), LpVariable("p4w3")]
]

#supply constraints
for source in sources:
  prob += num_trips[0][source-1] + num_trips[1][source-1] + num_trips[2][source-1] <= supply[source-1]

total_price = LpVariable("total_price")

for source in sources:
  for warehouse in warehouses:
    if prices[warehouse-1][source-1]:
      total_price += num_trips[warehouse-1][source-1] * prices[warehouse-1][source-1]

prob += total_price
    
# solve the problem
status = prob.solve(GLPK(msg=0))
LpStatus[status]
 
# print the results x1 = 20, x2 = 60
print value(num_silk)
print value(num_b2)
print value(num_b1)
print value(num_polyester)

print(3.45*value(num_silk) + 2.32*value(num_polyester) + 2.81*value(num_b1) + 3.25*value(num_b2))
