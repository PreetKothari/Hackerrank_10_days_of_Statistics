# Question: The final grades for a Physics exam taken by a large group of
# students have a mean of mi = 70 and a standard deviation of sigma = 10.
# If we can approximate the distribution of these grades by a normal
# distribution, what percentage of the students:
# 1. Scored higher than 80 (i.e., have a grade > 80)?
# 2. Passed the test (i.e., have a grade >= 60)?
# 3. Failed the test (i.e., have a grade < 60)?

# Import library
from math import erf

# Define functions
def cum_dist_func(mean, std_dev, x):
    return (0.5 * (1 + erf((x - mean)/(std_dev * (2 ** 0.5)))))

# Set data
values = list(map(float, input().split()))
mean = values[0]
std_dev = values[1]
q1 = float(input())
q2 = float(input())

# Gets the result and show it on the screen
prob_q1 = 100 - (cum_dist_func(mean, std_dev, q1) * 100) # 100 - prob of less than equal to 80
prob_q2 = 100 - (cum_dist_func(mean, std_dev, q2) * 100) # 100 - prob of less than equal to 60
prob_q3 = cum_dist_func(mean, std_dev, q2) * 100 # prob of less than equal to 60

print("{:.2f}".format(prob_q1))
print("{:.2f}".format(prob_q2))
print("{:.2f}".format(prob_q3))
