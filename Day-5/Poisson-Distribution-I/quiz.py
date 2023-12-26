# Question: A random variable, X, follows Poisson distribution with a mean of 2.5
# Find the probability with which the random variable X is equal to 5.

# Define functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Set data
mean = float(input())
k = float(input())

from math import exp
# e = 2.71828

# Gets the result and show it on the screen
prob = ((mean ** k) * (exp(-mean)) /  factorial(k)
print("{:.3f}".format(prob))
