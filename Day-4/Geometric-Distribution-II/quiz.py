# Question: The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the
# first 5 inspections?

# Set data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution, g(n,p) = (q**(n-1))*p
g = 0
for i in range(1, n + 1):
    g += (q**(i - 1)) * p

# Show the final result
print("{:.3f}".format(g))
