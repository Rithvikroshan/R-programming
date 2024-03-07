# Create three example arrays
array1 <- matrix(1:3, nrow = 1)
array2 <- matrix(4:6, nrow = 1)
array3 <- matrix(7:9, nrow = 1)

# Combine arrays by stacking their first rows
combined_array <- rbind(array1, array2, array3)

# Print the combined array
cat("Combined Array by Stacking First Rows:\n")
print(combined_array)
