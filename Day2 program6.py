# Load the built-in dataset airquality
data(airquality)

# Check if it is a data frame
if (is.data.frame(airquality)) {
  cat("The 'airquality' dataset is a data frame.\n")

  # Order the entire data frame by the first and second column
  airquality_ordered <- airquality[order(airquality$Ozone, airquality$Solar.R), ]

  # Display the ordered data frame
  cat("\nOrdered Data Frame by the first and second column:\n")
  print(airquality_ordered)

  # Remove the variables 'Solar.R' and 'Wind'
  airquality_filtered <- airquality[, !(names(airquality) %in% c('Solar.R', 'Wind'))]

  # Display the data frame after removing variables
  cat("\nData Frame after removing 'Solar.R' and 'Wind' variables:\n")
  print(airquality_filtered)
} else {
  cat("The 'airquality' dataset is not a data frame.\n")
}
