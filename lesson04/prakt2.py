# Написати програму, яка виводить сама себе

from os.path import abspath

filename = abspath(__file__)
f = open(filename, 'r')
for line in f:
    print(line)
f.close()
