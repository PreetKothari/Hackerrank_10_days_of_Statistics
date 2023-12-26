# Define functions
def median(values,size):
    if size%2 == 0:
        median = (values[(size//2)-1]+values[size//2])/2
    else:
        median = (values[size//2])
    return int(median)

# Set the data
n = int(input())
values = list(map(int,input().split()))
freqs = list(map(int,input().split()))

m = []
for i in range(n):
    m+= [values[i]]*freqs[i]
m.sort()
n = len(m)

# Verify that the total data is even or odd and calculate the quartiles
if n%2 == 0:
    q1 = median(m[:(n//2)],(n//2))
    q3 = median(m[(n//2):],(n//2))
else:
    q1 = median(m[:(n//2)],(n//2))
    q3 = median(m[(n//2)+1:],(n//2))

# Get the final result and print it on the screen
print("{:.1f}".format(q3-q1))
