# Question: A large elevator can transport a maximum of 9800 pounds. Suppose a
# load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean
# of u = 205 pounds and a standard deviation of a = 15 pounds. Based on this
# information, what is the probability that all 49 boxes can be safely loaded
# into the freight elevator and transported?

# Import library
from math import erf

# Define functions
def cum_dist_func(mean, std_dev, x):
    return (0.5 * (1 + erf((x - mean)/(std_dev * (2 ** 0.5)))))

# Set data
max_weight = float(input())
n = float(input())
mean = float(input())
std_dev = float(input())

mean_dash = n * mean
std_dev_dash = (n ** 0.5) * std_dev

# Gets the result and show it on the screen
print("{:.4f}".format(cum_dist_func(mean_dash, std_dev_dash, max_weight)))
