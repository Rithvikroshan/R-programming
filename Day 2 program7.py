# Create a vector of values
values_vector <- c(1, 2, 3, 4, 5, 6, 7, 8)

# Create a vector of dimensions
dimensions_vector <- c(2, 2, 2)  # This represents a 3-dimensional array with dimensions 2x2x2

# Provide names for each dimension
dimnames_list <- list(
  c("Row1", "Row2"),
  c("Col1", "Col2"),
  c("Depth1", "Depth2")
)

# Create the array
my_array <- array(values_vector, dim = dimensions_vector, dimnames = dimnames_list)

# Display the array
print("Array with Names for Dimensions:")
print(my_array)
