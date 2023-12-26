n = int(input())
m = list(map(int,input().split()))
m.sort()

mean = (sum(m)/n)
if n%2 == 0:
    median = ((m[(n//2)-1] + m[(n//2)])/2)
else:
    median = m[n//2]

count = 0
max = 0
num = 0

for i in m:
    if i == num:
        count +=1
    else:
        num = i
        count = 1
    if count > max:
        max = count
        mode = num

if max < 2:
    mode = m[0]

print('{:.1f}'.format(mean))
print('{:.1f}'.format(median))
print(mode)
