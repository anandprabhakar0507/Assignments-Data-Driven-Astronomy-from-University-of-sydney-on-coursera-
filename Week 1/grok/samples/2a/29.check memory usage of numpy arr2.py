import numpy as np

a = np.zeros(5, dtype=np.int32)
b = np.zeros(5, dtype=np.float64)

for obj in [a, b]:
  print('nbytes         :', obj.nbytes)
  print('size x itemsize:', obj.size*obj.itemsize)