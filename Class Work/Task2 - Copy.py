import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("original array   ", arr)


even_slice = arr[1:10:2] 
print("Even Slice    ", even_slice)


even_slice[0] = 100
print( even_slice)


print("array after modification", arr)
