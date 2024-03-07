# Load the Iris dataset
data(iris)

# (i) Find dimension, Structure, Summary statistics, Standard Deviation of all features.
print("Dimension:")
print(dim(iris))

print("\nStructure:")
str(iris)

print("\nSummary Statistics:")
summary(iris)

print("\nStandard Deviation of All Features:")
sapply(iris[, 1:4], sd)

# (ii) Find mean and standard deviation of features grouped by three species of Iris flowers
aggregate(cbind(Sepal.Length, Sepal.Width, Petal.Length, Petal.Width) ~ Species, data = iris, FUN = function(x) c(mean = mean(x), sd = sd(x)))

# (iii) Find quantile value of sepal width and length
quantile(iris$Sepal.Length)
quantile(iris$Sepal.Width)

# (iv) Create a new data frame named iris1 with a new column named Sepal.Length.Cate that categorizes Sepal.Length by quantile
iris1 <- iris
iris1$Sepal.Length.Cate <- cut(iris$Sepal.Length, breaks = quantile(iris$Sepal.Length), labels = c("Q1", "Q2", "Q3", "Q4"), include.lowest = TRUE)

# (v) Average value of numerical variables by two categorical variables: Species and Sepal.Length.Cate
aggregate(cbind(Sepal.Length, Sepal.Width, Petal.Length, Petal.Width) ~ Species + Sepal.Length.Cate, data = iris1, FUN = mean)

# (vi) Average mean value of numerical variables by Species and Sepal.Length.Cate
aggregate(cbind(Sepal.Length, Sepal.Width, Petal.Length, Petal.Width) ~ Species + Sepal.Length.Cate, data = iris1, FUN = function(x) c(mean = mean(x)))

# (vii) Create a Pivot Table based on Species and Sepal.Length.Cate
library(tidyr)
pivot_table <- spread(aggregate(Sepal.Length ~ Species + Sepal.Length.Cate, data = iris1, FUN = mean), key = Sepal.Length.Cate, value = Sepal.Length)

print("Pivot Table:")
print(pivot_table)
