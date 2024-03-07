# Create an array with specific dimensions
columns <- 4
rows <- 3
tables <- 2
my_array <- array(1:(columns * rows * tables), dim = c(rows, columns, tables))

# Display the content of the array
cat("Array Content:\n")
print(my_array)
