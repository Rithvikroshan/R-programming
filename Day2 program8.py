# Set seed for reproducibility
set.seed(123)

# Create a factor from a random sample of LETTERS
letters_factor <- factor(sample(LETTERS, 20, replace = TRUE))

# Display the original factor levels
cat("Original Factor Levels:\n")
print(levels(letters_factor))

# Extract five levels from the factor
selected_levels <- sample(levels(letters_factor), 5)

# Display the selected levels
cat("\nSelected Levels:\n")
print(selected_levels)
