# Existing data frame
exam_data <- data.frame(
  name = c('Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'),
  score = c(12.5, 9, 16.5, 12, 9, 20, 14.5, 13.5, 8, 19),
  attempts = c(1, 3, 2, 3, 2, 3, 1, 1, 2, 1),
  qualify = c('yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes')
)

# Add new row(s) to the existing data frame
new_exam_data <- data.frame(
  name = c('Robert', 'Sophia'),
  score = c(10.5, 9),
  attempts = c(1, 3),
  qualify = c('yes', 'no')
)

exam_data <- rbind(exam_data, new_exam_data)

# Display the updated data frame
cat("Updated Data Frame with New Row(s):\n")
print(exam_data)

# Sort the data frame by name and score
exam_data_sorted <- exam_data[order(exam_data$name, exam_data$score), ]

# Display the sorted data frame
cat("\nSorted Data Frame by Name and Score:\n")
print(exam_data_sorted)

# Save the information of the data frame in a file (CSV format)
write.csv(exam_data_sorted, "exam_data_sorted.csv", row.names = FALSE)

# Display the content of the saved file
cat("\nContent of the Saved File (exam_data_sorted.csv):\n")
saved_data <- read.csv("exam_data_sorted.csv")
print(saved_data)
