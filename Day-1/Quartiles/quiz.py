# Define functions
def median(values,size):
    if size%2 == 0:
        median = (values[(size//2)-1]+values[size//2])/2
    else:
        median = (values[size//2])
    return int(median)

# Set the data
n = int(input())
m = list(map(int,input().split()))
m.sort()

# Verify that the total data is even or odd
if n%2 == 0:
    q1 = median(m[:(n//2)],(n//2))
    q2 = median(m,n)
    q3 = median(m[(n//2):],(n//2))
else:
    q1 = median(m[:(n//2)],(n//2))
    q2 = median(m,n)
    q3 = median(m[(n//2)+1:],(n//2))

# Get the final result and print it on the screen
print(q1)
print(q2)
print(q3)
