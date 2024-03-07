# Function to get unique elements of a string
getUniqueString <- function(input_string) {
  unique_chars <- unique(strsplit(input_string, NULL)[[1]])
  return(unique_chars)
}

# Function to get unique numbers of a vector
getUniqueNumbers <- function(input_vector) {
  unique_numbers <- unique(input_vector)
  return(unique_numbers)
}

# Example usage
input_string <- "hello world"
input_vector <- c(1, 2, 3, 2, 4, 5, 3, 6)

unique_string_elements <- getUniqueString(input_string)
unique_vector_numbers <- getUniqueNumbers(input_vector)

cat("Unique elements of the string:", unique_string_elements, "\n")
cat("Unique numbers of the vector:", unique_vector_numbers, "\n")
