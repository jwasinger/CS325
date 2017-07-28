import pdb, json
import matplotlib.pyplot as plt
import numpy as np

data = None
with open('data.json', 'r') as f:
  data = json.load(f)

'''
apply a function to a set (similar to map but preservers set order)
'''
def apply_function(fit_fn, data_x):
  result = []
  for x in data_x:
    result.append(fit_fn(x))
  return result

if __name__ == "__main__":
  for algo in data.keys():
    data_x = data[algo]['x']
    data_y = data[algo]['y']

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(algo.replace('_', ' '))
    ax.set_xlabel("List size")
    ax.set_ylabel("Running time (seconds)")

    ax.axis([100, 1000, 0, max(data_y)])

    fit = np.polyfit(data_x, data_y, deg=1)

    better_enumeration_fit =  [  np.float128(2.90793000e-08),  np.float128(-1.66918292e-07),  np.float128(-8.17537308e-05)]
    linear_fit =              [  np.float128(7.48200850e-08),   np.float128(2.14576721e-06)]
    enumeration_fit =         [  np.float128(1.56639883e-05),  np.float128(-7.31257330e-03),   np.float128(8.20168352e-01)]
    divide_and_conquer_fit = [  np.float128(2.15644547e-06),  np.float128(-9.52084859e-06)] 

    data_x = apply_function(lambda x: np.float128(x), data_x)

    if algo == 'Linear':
      fit_data_y = apply_function(lambda x: x*linear_fit[0] + linear_fit[1], data_x)
      ax.plot(data_x, data_y, 'ro', data_x, fit_data_y, '--k')
    elif algo == 'Divide_And_Conquer':
      fit_data_y = apply_function(lambda x: x*divide_and_conquer_fit[0] + divide_and_conquer_fit[1], data_x)
      ax.plot(data_x, data_y, 'ro', data_x, fit_data_y, '--k')
    elif algo == 'Enumeration':
      fit_data_y = apply_function(lambda x: (x*x)*enumeration_fit[0] + x*enumeration_fit[1] + better_enumeration_fit[2], data_x)
      pdb.set_trace()
      ax.plot(data_x, data_y, 'ro', data_x, fit_data_y, '--k')
    elif algo == 'Better_Enumeration':
      pdb.set_trace()
      fit_data_y = apply_function(lambda x: (x*x)*better_enumeration_fit[0] + x*better_enumeration_fit[1] + better_enumeration_fit[2], data_x)
      ax.plot(data_x, data_y, 'ro', data_x, fit_data_y, '--k')

    plt.show()
