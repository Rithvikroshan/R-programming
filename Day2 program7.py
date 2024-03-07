# Load the built-in dataset women
data(women)

# Create a factor corresponding to the height
height_factor <- cut(women$height, breaks = c(50, 60, 70, 80), labels = c("Short", "Medium", "Tall"))

# Display the factor levels
cat("Factor Levels for Height:\n")
print(levels(height_factor))

# Display the original data frame with the new factor
cat("\nOriginal Data Frame with Height Factor:\n")
women_with_height_factor <- data.frame(women, HeightCategory = height_factor)
print(women_with_height_factor)
