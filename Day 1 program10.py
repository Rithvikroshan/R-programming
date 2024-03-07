# Draw an empty plot
plot.new()
title(main = "Empty Plot", xlab = "X-axis", ylab = "Y-axis")

# Draw an empty plot with specified axes limits
plot.new()
title(main = "Empty Plot with Axes Limits", xlab = "X-axis", ylab = "Y-axis")

# Specify axes limits
x_limits <- c(0, 10)
y_limits <- c(0, 20)
axis(1, at = seq(x_limits[1], x_limits[2], by = 2))
axis(2, at = seq(y_limits[1], y_limits[2], by = 4))

# Add a rectangle to represent the specified axes limits
rect(x_limits[1], y_limits[1], x_limits[2], y_limits[2], border = "red", lwd
