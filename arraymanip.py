#Week 3 HW CS 162
#Manupulating Arrays in Python
#Paul Debruine

import random
import numpy as np

#creates a random array with an upper bound of 11, and a size of 5x5
a= np.random.randint(11, size=(5,5))

#prints entire array
print(a)
#prints element in 2nd row 3rd collumn (python starts at 0)
print(a[1,2])
#prints the sum of all the elements in an array
print(a.sum())
#prints the mean value of the elements for each row
print(np.mean(a, 1))
#prints the max value for each column in the array
print(np.max(a, 0))

