# a. Draw a Bar chart to show details of "Survived" on the Titanic based on passenger Class
barplot(table(Titanic[,"Survived",,]), main = "Survival Count Based on Passenger Class", xlab = "Survived", col = c("red", "green"), legend = TRUE)

# b. Modify the above plot based on gender of people who survived
barplot(table(Titanic[,"Survived",,], Titanic[,"Sex",,]), beside = TRUE, legend = TRUE,
        col = c("lightblue", "pink"), main = "Survival Count Based on Passenger Class and Gender")

# c. Draw histogram plot to show distribution of feature "Age"
hist(Titanic$Age, main = "Histogram of Age on Titanic", xlab = "Age", ylab = "Frequency", col = "lightgreen")
