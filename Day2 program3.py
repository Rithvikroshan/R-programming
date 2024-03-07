# Create an array with specific dimensions
columns <- 4
rows <- 3
tables <- 2
my_array <- array(1:(columns * rows * tables), dim = c(rows, columns, tables))

# Display the content of the array
cat("Array Content:\n")
print(my_array)
# Create a 5x3 array of even integers greater than 50
even_integers_array <- matrix(seq(from = 52, by = 2, length.out = 5 * 3), nrow = 5, ncol = 3)

# Display the content of the array
cat("5x3 Array of Even Integers Greater than 50:\n")
print(even_integers_array)

