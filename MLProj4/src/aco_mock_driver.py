#!/usr/bin/env python3


from acoc import AntClustering as ACC


path = ''

f = open(path, 'r')

data = []
for line in f:
    line = line.split(',')
    data.append(line)
f.close()

#acc = ACC(ants, epochs, size, neighborhood size, data, max_move)
acc = ACC(50, 1000, 4, 2, data, 10)
acc.cluster()
acc.output()
