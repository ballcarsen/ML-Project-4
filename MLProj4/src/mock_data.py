#!/usr/bin/env python3 

import random


path = 'fake.txt'

f = open(path, 'a')

for i in range(10):
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    z = random.randint(0, 3)
    f.write(str(x) + ',' + str(y) + ',' + str(z) + '\n')

for i in range(10):
    x = random.randint(7, 10)
    y = random.randint(7, 10)
    z = random.randint(7, 10)
    f.write(str(x) + ',' + str(y) + ',' + str(z) + '\n')


f.close()
