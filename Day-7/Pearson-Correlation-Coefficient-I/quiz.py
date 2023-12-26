# Question: Given two n-element data sets, X and Y, calculate the value of
# the Pearson correlation coefficient.

# import libraries
import statistics as st

# Define functions
def mean(x):
    return (sum(x)/len(x))

def std_dev(x, n):
    sum = 0
    x_mean = mean(x)
    for i in range(n):
        sum += ((x[i] - x_mean) ** 2)
    return ((sum/n) ** 0.5)

def pearson_corr_coef(x, y, n):
    sum = 0
    x_mean = mean(x)
    y_mean = mean(y)
    std_x = std_dev(x, n)
    std_y = std_dev(y, n)
    for i in range(n):
        sum += ((x[I] - x_mean) * (y[I] - y_mean))
    return (sum/(n* std_x * stdy))

# Set data
n = int(float(input()))
x = list(map(float, input().split()))
y = list(map(float, input().split()))

# Gets the result and show it on the screen
print("{:3f}".format(pearson_corr_coef(x, y, n)))
