# Define functions
def mean(arr):
    return sum(arr)/len(arr)

def std_dev(arr, size):
    sum = 0
    for i in range(size):
        sum = sum + (arr[i] - mean(arr)) ** 2
    return ((sum/size)**0.5)

# Set data
n = int(input())
arr = list(map(int,input().split()))

# Get standard deviation
print("{:.1f}".format(std_dev(arr, n)))
