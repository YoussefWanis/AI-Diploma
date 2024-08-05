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






def inverse_matrix(matrix):
    # Check if the matrix is 3x3
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        try:
         def determinant(matrix):
            return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
        except: "non invertible"
    det = determinant(matrix)

    if det == 0:
        return None
    adjoint = [[matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1],
        matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2],
        matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]],
        [matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2],
        matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0],
        matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]],
        [matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0],
        matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1],
        matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]]]

    cofactor = [[adjoint[j][i] for j in range(3)] for i in range(3)]

    inverse = [[cofactor[i][j] / det for j in range(3)] for i in range(3)]

    return inverse

# Example:
matrix = [[1, 2, 3],[0, 1, 4],[5, 6, 0]]

inverse = inverse_matrix(matrix)
if inverse:
    for row in inverse:
        print(row)
else:
    print("The matrix is not invertible.")









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
