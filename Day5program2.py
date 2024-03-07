# Load the diet dataset
data(diet)

# a. Create multi regression model to find weight of the chicken, by "Time" and "Diet" as predictor variables
multi_regression_model <- lm(weight ~ Time + Diet, data = diet)

# b. Predict weight for Time=10 and Diet=1
new_data <- data.frame(Time = 10, Diet = 1)
predicted_weight <- predict(multi_regression_model, newdata = new_data)

# c. Find the error in the model for the same
actual_weight <- diet$weight[diet$Time == 10 & diet$Diet == 1]
error <- actual_weight - predicted_weight

# Print results
print("Multi Regression Model:")
print(summary(multi_regression_model))
print("Predicted Weight:")
print(predicted_weight)
print("Error in Model:")
print(error)
