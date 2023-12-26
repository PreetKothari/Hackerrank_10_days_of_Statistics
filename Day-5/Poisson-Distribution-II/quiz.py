# Question: The manager of an industrial plant is planning to buy a machine of
# either type A or type B. For each day’s operation:
# The number of repairs, X, that machine A needs is a Poisson random variable
# with a mean of 0.88. The daily cost of operating A is C = 160 + 40X².
# The number of repairs, Y, that machine B needs is a Poisson random variable
# with a mean of 1.55. The daily cost of operating B is C = 128 + 40Y².

# Define functions
def exp_val(lmda):
    return (lmda + (lmda**2))

# Set data
mean = list(map(float,input().split()))

# Gets the result and show it on the screen
cost_a = 160 + (40*exp_val(mean[0]))
cost_b = 128 + (40*exp_val(mean[1]))

print("{:.3f}".format(cost_a))
print("{:.3f}".format(cost_b))
