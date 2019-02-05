import sys
import numpy as np

a = np.array([])
b = np.array([1, 2, 3])
c = np.zeros(10**6)

for obj in [a, b, c]:
  print('sys:', sys.getsizeof(obj), 'np:', obj.nbytes)