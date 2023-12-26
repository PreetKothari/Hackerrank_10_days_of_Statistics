# Question: The number of tickets purchased by each student for the
# University X vs. University Y football game follows a distribution that has
# a mean of u = 2.4 and a standard deviation of 20.
# A few hours before the game starts, 100 eager students line up to purchase
# last-minute tickets. If there are only 250 tickets left, what is the
# probability that all 100 students will be able to purchase tickets?

# Import library
from math import erf

# Define functions
def cum_dist_func(mean, std_dev, x):
    return (0.5 * (1 + erf((x - mean)/(std_dev * (2 ** 0.5)))))

# Set data
tickets_left = float(input())
n = float(input())
mean = float(input())
std_dev = float(input())

mean_dash = n * mean
std_dev_dash = (n ** 0.5) * std_dev

# Gets the result and show it on the screen
print("{:.4f}".format(cum_dist_func(mean_dash, std_dev_dash, tickets_left)))
