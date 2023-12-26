# Confidence interval

# Question: You have a sample of 100 values from a population with mean u = 500
# and with standard deviation a = 80. Compute the interval that covers the
# middle 95% of the distribution of the sample mean; in other words, compute
# A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96. Note
# that z is the z-score.

# Set data
values = float(input())
mean = float(input())
std_dev = float(input())
percent_ci = float(input())
z_value = float(input())

# Formula CI
ci = z_value * (std_dev/(values ** 0.5))

# Gets the result and show it on the screen
print(round(mean - ci, 2))
print(round(mean + ci, 2))
