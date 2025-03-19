import numpy as np


b = np.array([[[1, 2, 3],
             [5, 6, 7],
            [8, 9, 10]]])

print(b.shape)
print("second row third column", b[0,1,2])
print("second columd",b[0,:,1])
# print(b[:,1])