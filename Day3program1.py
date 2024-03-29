# Create two input vectors
vector1 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)
vector2 <- c(10, 11, 12, 13, 14, 15, 16, 17, 18)

# Combine vectors into two matrices
matrix1 <- matrix(vector1, nrow = 3, ncol = 3, byrow = TRUE)
matrix2 <- matrix(vector2, nrow = 3, ncol = 3, byrow = TRUE)

# Combine matrices into an array
my_array <- array(c(matrix1, matrix2), dim = c(3, 3, 2))

# Print the second row of the second matrix
cat("Second row of the second matrix:\n")
print(my_array[2, , 2])

# Print the element in the 3rd row and 3rd column of the 1st matrix
cat("Element in the 3rd row and 3rd column of the 1st matrix:\n")
print(my_array[3, 3, 1])
