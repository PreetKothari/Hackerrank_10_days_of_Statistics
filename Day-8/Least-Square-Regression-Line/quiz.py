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

def f_y(a, b, x):
    return a + (b * x)

# Set data
x = []
y = []
n = 5
for i in range(n):
    val = list(map(float,input().split()))
    x.append(val[0])
    y.append(val[1])

# Set the B and A
b = ((pearson_corr_coef(x, y, n) * std_dev(y, n)) / std_dev(x, n))
a = mean(y) - (b * mean(x))

# Gets the result and show it on the screen
print("{:3f}".format(f_y(a, b, 80)))
