import sys

a = 3
b = 3.123
c = [a, b]
d = []
for obj in [a, b, c, d]:
  print(obj, sys.getsizeof(obj))