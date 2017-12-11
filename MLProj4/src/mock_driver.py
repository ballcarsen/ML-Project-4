#!/usr/bin/env python3


#from acoc.acco import AntClustering as ACC
from acoc.ants import ACC

path = 'indians2.txt'
#path = 'HTRU2.txt'
#path = 'seeds.txt'
#path = 'fake.txt'
#path = 'energy.txt'
#path = 'shuttle.trim.txt'

f = open(path, 'r')

data = []
for line in f:
    line = line.replace('\n', '')
    line = line.split('\t')
    #line = line.split(',')
    if line[-1] == '':
        del line[-1]
    data.append(line)
f.close()

#acc = ACC(ants, epochs, size, neighborhood size, data, max_move, alpha, sig)
#acc = ACC(50, 1000, 4, 3, data, 25, 1, 1)
#acc.print_cemetery()
#acc.output()
#acc.cluster()
#acc.output()
#acc.show()
acc = ACC(100, 10, 12, data, 0.1)
acc.cluster()
