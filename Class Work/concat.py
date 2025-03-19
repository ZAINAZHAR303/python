import numpy as np

b = np.array([[1, 2, 3, 4],[5, 6, 7,8]])
c= np.array([[11,12,13,14],[15,16,17,18]] )

print(b[np.newaxis,:].ndim)

print(np.expand_dims(b,axis=0).shape)
# print (np.concatenate((b,c)))
# print (np.concatenate((b,c), axis=1))

# size function gives us no of elements in the array


## reshaping

four_dim_array = np.array([
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ],
    [
        [[9, 10], [11, 12]],
        [[13, 14], [15, 16]]
    ]
])
19

24

print(four_dim_array.shape)

print(four_dim_array.reshape())


