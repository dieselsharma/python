import numpy as np

#create an array using .array() function

A = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]])

#finding shape of the array using 

print(A.shape)

#length of elements

print(A.itemsize)

#array of elements in the second column of each row

print(A[:,1])

#new array with square of each element

print(np.square(A))

#Print the array elements in the reverse order

print(A.flatten()[::-1])

# Create a 10x10 array with random values and find the minimum and maximum values.

B = np.random.randint(1,100,(10,10))
print(B)
print(B.min())
print(B.max())


