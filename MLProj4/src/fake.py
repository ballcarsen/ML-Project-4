#!/usr/bin/env python3 

import random


path = 'fake.txt'

f = open(path, 'a')

for i in range(10):
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    z = random.randint(0, 10)
    f.write(str(x) + ',' + str(y) + ',' + str(z) + '\n')


f.close()
