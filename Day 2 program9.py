# Create vectors, matrices, and a function
vector_example <- c(1, 2, 3)
matrix_example <- matrix(4:9, nrow = 2)
function_example <- function(x) { return(x^2) }

# Create a list with vectors, matrices, and a function
my_list <- list(
  vector_example,
  matrix_example,
  function_example
)

# Print the content of the list
cat("Content of the List:\n")
print(my_list)
