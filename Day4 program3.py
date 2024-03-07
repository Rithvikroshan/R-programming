# Load the air quality dataset
data(airquality)

# (i) Find any missing values (NA) in features and drop the missing values if it's less than 10%, else replace with the mean of that feature
missing_values <- colMeans(is.na(airquality))
threshold <- 0.1  # 10% threshold for missing values

for (col in names(airquality)) {
  if (missing_values[col] < threshold) {
    airquality <- na.omit(airquality, cols = col)
  } else {
    mean_value <- mean(airquality[[col]], na.rm = TRUE)
    airquality[[col]][is.na(airquality[[col]])] <- mean_value
  }
}

# (ii) Apply a linear regression algorithm using Least Squares Method on "Ozone" and "Solar.R"
linear_model <- lm(Ozone ~ Solar.R, data = airquality)

# (iii) Plot Scatter plot between Ozone and Solar and add a regression line created by the above model
plot(airquality$Solar.R, airquality$Ozone, xlab = "Solar Radiation", ylab = "Ozone Concentration", main = "Scatter Plot and Regression Line")
abline(linear_model, col = "red")
