# Load required library for logistic regression
library(caTools)
library(nnet)

# Set seed for reproducibility
set.seed(123)

# Sample 80% for training and 20% for testing
split <- sample.split(iris$Species, SplitRatio = 0.8)
train_data <- subset(iris, split == TRUE)
test_data <- subset(iris, split == FALSE)

# Create Logistic Regression model
log_reg_model <- multinom(Species ~ Petal.Length + Petal.Width, data = train_data)

# Predict probability using test data
predicted_prob <- predict(log_reg_model, newdata = test_data, type = "probs")

# Create Confusion Matrix
confusion_matrix <- table(test_data$Species, colnames(predicted_prob)[apply(predicted_prob, 1, which.max)])

print("Confusion Matrix:")
print(confusion_matrix)

# (i) Compute mean, median, mode of the given values
values <- c(90, 50, 70, 80, 70, 60, 20, 30, 80, 90, 20)

mean_value <- mean(values)
median_value <- median(values)
mode_value <- names(sort(table(values), decreasing = TRUE))[1]

print("Mean:")
print(mean_value)

print("Median:")
print(median_value)

print("Mode:")
print(mode_value)

# (ii) Find 2nd highest and 3rd lowest value
second_highest <- sort(unique(values), decreasing = TRUE)[2]
third_lowest <- sort(unique(values))[3]

print("2nd Highest Value:")
print(second_highest)

print("3rd Lowest Value:")
print(third_lowest)

