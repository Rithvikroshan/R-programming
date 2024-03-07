# Create a 5x4 matrix with labels and fill by rows
matrix_rows <- matrix(1:20, nrow = 5, ncol = 4, byrow = TRUE,
                      dimnames = list(c("Row1", "Row2", "Row3", "Row4", "Row5"),
                                      c("Col1", "Col2", "Col3", "Col4")))

# Create a 3x3 matrix with labels and fill by rows
matrix_rows_3x3 <- matrix(21:29, nrow = 3, ncol = 3, byrow = TRUE,
                          dimnames = list(c("RowA", "RowB", "RowC"),
                                          c("Col1", "Col2", "Col3")))

# Create a 2x2 matrix with labels and fill by columns
matrix_columns <- matrix(31:34, nrow = 2, ncol = 2, byrow = FALSE,
                         dimnames = list(c("RowX", "RowY"),
                                         c("ColA", "ColB")))

# Display matrices
cat("Matrix 5x4 (Filled by Rows):\n")
print(matrix_rows)

cat("\nMatrix 3x3 (Filled by Rows):\n")
print(matrix_rows_3x3)

cat("\nMatrix 2x2 (Filled by Columns):\n")
print(matrix_columns)
