# Given data frame
exam_data <- data.frame(
  name = c('Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'),
  score = c(12.5, 9, 16.5, 12, 9, 20, 14.5, 13.5, 8, 19),
  attempts = c(1, 3, 2, 3, 2, 3, 1, 1, 2, 1),
  qualify = c('yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes')
)

# Add a new column 'country'
exam_data$country <- c("USA", "USA", "USA", "USA", "UK", "USA", "USA", "India", "USA", "USA")

# Extract 3rd and 5th rows with 1st and 3rd columns
result <- exam_data[c(3, 5), c(1, 3)]

# Display the result
print(result)
