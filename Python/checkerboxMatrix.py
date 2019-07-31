# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:12:19 2019
Create checker box
@author: vikash
"""

import numpy as np
# Read the variable from STDIN
n = int(input())

matrix = np.zeros((n,n), dtype=int)
matrix[1::2,::2] = 1
matrix[::2,1::2] = 1
print(matrix)