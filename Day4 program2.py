# Load the air quality dataset
data(airquality)

# i. Compute the mean temperature (without using built-in function)
mean_temperature <- sum(airquality$Temp) / length(airquality$Temp)

print("Mean Temperature:")
print(mean_temperature)

# ii. Extract the first five rows from airquality
first_five_rows <- head(airquality, 5)

print("First Five Rows:")
print(first_five_rows)

# iii. Extract all columns from airquality except Temp and Wind
selected_columns <- airquality[, !(names(airquality) %in% c("Temp", "Wind"))]

print("Selected Columns:")
print(selected_columns)

# iv. Which was the coldest day during the period?
coldest_day <- airquality[which.min(airquality$Temp), ]

print("Coldest Day:")
print(coldest_day)

# (i) Get the Summary Statistics of the air quality dataset
summary_statistics <- summary(airquality)

print("Summary Statistics:")
print(summary_statistics)

# (ii) Melt airquality dataset and display as long-format data
library(reshape2)
melted_data <- melt(airquality)

print("Melted Data (Long Format):")
print(melted_data)

# (iii) Melt airquality data and specify month and day to be "ID variables"
melted_data_with_id <- melt(airquality, id.vars = c("Month", "Day"))

print("Melted Data with ID Variables:")
print(melted_data_with_id)

# (iv) Cast the molten airquality dataset with respect to month and date features
casted_data <- dcast(melted_data_with_id, Month + Day ~ variable)

print("Casted Data:")
print(casted_data)

# (v) Use cast function appropriately and compute the average of Ozone, Solar.R, Wind, and temperature per month
average_per_month <- dcast(melted_data, Month ~ variable, fun.aggregate = mean)

print("Average per Month:")
print(average_per_month)
