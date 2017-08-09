from pulp import *

# declare your variables
num_polyester = LpVariable("num_polyester", 10000, 14000, cat='Integer')
num_b1 = LpVariable("num_b1", 13000, 16000, cat='Integer')
num_silk = LpVariable("num_silk", 6000, 7000, cat='Integer')
num_b2 = LpVariable("num_b2", 6000, 8500, cat='Integer')
 
# defines the problem
prob = LpProblem("problem", LpMaximize)

#materials constraints

#silk
prob += 0.125*num_silk <= 1000
prob += 0.125*num_silk >= 0

#polyester
prob += 0.08*num_polyester + 0.05*num_b1 + 0.03*num_b2 <= 2000
prob += 0.08*num_polyester + 0.05*num_b1 + 0.03*num_b2 >= 0

#cotton
prob += 0.05*num_b1 + 0.07*num_b2 <= 1250
prob += 0.05*num_b1 + 0.07*num_b2 >= 0

'''
prob += num_polyester <= 14000
prob += num_polyester >= 10000

prob += num_silk >= 6000
prob += num_silk <= 7000

prob += num_b1 <= 16000
prob += num_b1 >= 13000

prob += num_b2 <= 8500
prob += num_b2 >= 6000
'''


# defines the objective function to maximize
prob += 3.45*num_silk + 2.32*num_polyester + 2.81*num_b1 + 3.25*num_b2
 
# solve the problem
status = prob.solve(GLPK(msg=0))
LpStatus[status]
 
# print the results x1 = 20, x2 = 60
print value(num_silk)
print value(num_b2)
print value(num_b1)
print value(num_polyester)

print(3.45*value(num_silk) + 2.32*value(num_polyester) + 2.81*value(num_b1) + 3.25*value(num_b2))
