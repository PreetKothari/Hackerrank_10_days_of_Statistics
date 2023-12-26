# Question: In a certain plant, the time taken to assemble a car is a random
# variable, X, having a normal distribution with a mean of 20 hours and a
# standard deviation of 2 hours. What is the probability that a car can be
# assembled at this plant in:
# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

# Import library
from math import erf

# Define functions
def cum_dist_func(mean, std_dev, x):
    return (0.5 * (1 + erf((x - mean)/(std_dev * (2 ** 0.5)))))

# Set data
values = list(map(float, input().split()))
mean = values[0]
std_dev = values[1]

less_period = float(input())
between_period = list(map(float, input().split()))

# Gets the result and show it on the screen
prob_less_period = cum_dist_func(mean, std_dev, less_period)
f_a = cum_dist_func(mean, std_dev, between_period[0])
f_b = cum_dist_func(mean, std_dev, between_period[1])
prob_between_period = (f_b - f_a)

print("{:.3f}".format(prob_less_period))
print("{:.3f}".format(prob_between_period))
