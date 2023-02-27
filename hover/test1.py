import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

x = ['a', 'b', 'c', 'd', 'e']
y = [1, 2, 3, 4, 5]

names = np.array(list("ABCDE"))
#is names just an array for linking up original data 
# when hover'd?
print(list("ABCDE"))
print(names)

fig, ax = plt.subplot()