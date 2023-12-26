n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

s = 0
for i in range(n):
    s += x[i]*w[i]

w_mean = s/sum(w)

print("{:.1f}".format(w_mean))
