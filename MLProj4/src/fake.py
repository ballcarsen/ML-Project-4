#!/usr/bin/env python3 

import random


path = 'fake.txt'

f = open(path, 'a')

for i in range(100):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    z = random.randint(0, 100)
    f.write(str(x) + ',' + str(y) + ',' + str(z) + '\n')


f.close()
