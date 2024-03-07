# Load the ChickWeight dataset
data(ChickWeight)

# (i) Order the data frame in ascending order by feature name "weight" grouped by feature "diet" and extract the last 6 records
ordered_data <- ChickWeight[order(ChickWeight$weight, ChickWeight$diet), ]
last_six_records <- tail(ordered_data, 6)

print("(i) Last 6 Records:")
print(last_six_records)

# (ii) a. Perform melting function based on "Chick", "Time", "Diet" features as ID variables
library(reshape2)
melted_data <- melt(ChickWeight, id.vars = c("Chick", "Time", "Diet"))

print("(ii) a. Melted Data:")
print(melted_data)

# (ii) b. Perform cast function to display the mean value of weight grouped by Diet
mean_weight_cast <- dcast(melted_data, Diet ~ variable, fun.aggregate = mean)

print("(ii) b. Mean Weight Grouped by Diet:")
print(mean_weight_cast)

# (ii) c. Perform cast function to display the mode of weight grouped by Diet
library(DescTools)
mode_weight_cast <- dcast(melted_data, Diet ~ variable, fun.aggregate = Mode)

print("(ii) c. Mode of Weight Grouped by Diet:")
print(mode_weight_cast)
