# Quiz: Given two n-element data sets, X and Y, calculate the value of
# Spearman's rank correlation coefficient.

# Define functions
def rank(x):
    x_sorted = sorted(x)
    rx = dict()
    for i in range(n):
        for j in range(n):
            if x[i] == x_sorted[j]:
                rx[x[i]] = j + 1
    return rx

def spearmans_rank_corr_coef(x, y, n):
    diff_rank = 0
    rx = rank(x)
    ry = rank(y)
    for i in range(n):
        diff_rank += ((rx[x[i]] - ry[y[i]]) ** 2)
    return (1 - ((6 * diff_rank)/((n ** 3) - n)))

# Set data
n = int(float(input()))
x = list(map(float, input().split()))
y = list(map(float, input().split()))

# Gets the result and show it on the screen
print("{:.3f}".format(spearmans_rank_corr_coef(x, y, n)))
