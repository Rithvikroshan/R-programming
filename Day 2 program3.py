# Set the seed for reproducibility
set.seed(123)

# Generate a list of random numbers from normal distribution
random_numbers <- rnorm(100, mean = 0, sd = 1)  # Adjust the parameters as needed

# Count occurrences of each value
occurrences <- table(random_numbers)

# Print the list of random numbers and their occurrences
print("List of random numbers:")
print(random_numbers)

print("\nOccurrences of each value:")
print(occurrences)
