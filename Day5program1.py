# Load the diet dataset
data(diet)

# a. Create Box plot for "weight" grouped by "Diet"
boxplot(weight ~ Diet, data = diet, main = "Box Plot of Weight Grouped by Diet", xlab = "Diet", ylab = "Weight")

# b. Create Histogram for "weight" for Diet-1
hist(diet$weight[diet$Diet == 1], main = "Histogram of Weight for Diet-1", xlab = "Weight", ylab = "Frequency")

# c. Create Scatter plot for "weight" vs "Time" grouped by Diet
plot(weight ~ Time, data = diet, col = Diet, main = "Scatter Plot of Weight vs Time Grouped by Diet", xlab = "Time", ylab = "Weight")
legend("topright", legend = levels(diet$Diet), col = 1:3, pch = 1, title = "Diet")
