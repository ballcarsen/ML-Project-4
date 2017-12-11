#!/usr/bin/env python3


from acoc.acco import AntClustering as ACC


#path = '../seeds.txt'
path = 'fake.txt'

f = open(path, 'r')

data = []
for line in f:
    line = line.replace('\n', '')
    line = line.split(',')
    data.append(line)
f.close()

#acc = ACC(ants, epochs, size, neighborhood size, data, max_move, alpha, sig)
acc = ACC(100, 1000, 4, 10, data, 2, 1, 1)
#acc.print_cemetery()
acc.output()
acc.cluster()
acc.output()
acc.show()
