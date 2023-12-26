# Question: A manufacturer of metal pistons finds that, on average, 12% of the
# pistons they manufacture are rejected because they are incorrectly sized.
# What is the probability that a batch of 10 pistons will contain:

# Define functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def binomial(x, n, p):
    f = factorial(n) / (factorial(n - x) * factorial(x))
    return (f * p**x * (1.0 - p)**(n-x))

# Set data
values = list(map(float, input().split()))
prob_fail = (values[0] / 100)
batch_size = int(values[1])

# First rule: No more than 2 rejects
no_more_than_2_rejects = 0
# Second rule: At least 2 rejects
at_least_2_rejects =

for i in range(3):
    if i == 2:
        at_least_2_rejects = 1 - no_more_than_2_rejects 
    no_more_than_2_rejects += binomial(i, n, prob_fail)

print('{:.3f}'.format(no_more_than_2_rejects))
print('{:.3f}'.format(at_least_2_rejects))
