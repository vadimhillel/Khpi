from pprint import pprint
import math
import numpy as np

N = ord("V") % 5 + 1
print("\n\tVariant: ", N)


def my_func(interval: list, res: list) -> list:
      for x in np.arange(interval[0], interval[1], 0.2):
            if (x > 1):
                  y = np.sqrt(math.tan(x**2 - 1))
                  res.append(float(f'{y:.2f}'))
            elif (0<=x<=1):
                  y = -2*x
                  res.append(float(f'{y:.2f}'))
            elif (x < 0):  
                  y = math.exp(np.cos(x))
                  res.append(float(f'{y:.2f}'))
            
      return res

pprint(my_func([-1, 1.5], []))