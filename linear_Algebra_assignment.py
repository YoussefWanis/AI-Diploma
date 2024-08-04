import numpy as np

## Arrays to test on
array1 = np.array([[1,2,3], [3,4,6], [5,9,5]])

# Dominant Value Function
def dominant(Mat):
    x= np.linalg.eigvals(Mat)
    return x.max()

## Test on dominant value function 
print(dominant(array1))



# inverse matrix
def matrix_inverse(Mat):
    if np.linalg.det(Mat) != 0:
        return np.linalg.inv(Mat)
    else : return 'The Matrix is not invertible'

print("inverse matrix: ", str(matrix_inverse(array1))) 



# Identity Matrix
def identity_matrix(Mat):
    if len(Mat) == len(Mat[0]):
        singular_matrix = []
        for i in range(len(Mat)):
            singular_matrix_row = []
            for j in range(len(Mat[i])):
                if i == j:
                    singular_matrix_row.append(1)
                else : singular_matrix_row.append(0)
            singular_matrix.append(singular_matrix_row)
        return singular_matrix
    else: return "not square matrix"

print(identity_matrix(array1))
