# Написати програму, яка виводить сама себе задом наперед

from os.path import abspath

filename = abspath(__file__)
f = open(filename, 'r')
lst = []
for line in f:
    lst.append(line)
f.close()
N = len(lst)
for i in range(N-1,-1,-1):
    print(lst[i])
