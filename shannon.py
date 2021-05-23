import sys
import collections
import math

def shannon(file_name):
  with open(file_name, "r") as file:
    source = file.read()
    w = collections.Counter(source)
    total = len(source)
    for k in w.keys():
       w[k] /= total
    h = -sum([w_i * math.log2(w_i) for w_i in w.values()])
    print(h)

if __name__ == '__main__' and len(sys.argv) == 2:
  shannon(sys.argv[1])
