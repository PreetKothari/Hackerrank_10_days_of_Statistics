# Import library
from sklearn import linear_model

# Set data
value = list(map(int,input().split()))
m = value[0]
n = value[1]
X = []
Y = []

# Get the parameters X and Y for discovering variables a and b
for i in range(n):
    x = [0]
    elements = list(map(float,input().split()))
    for j in range(m):
        x.append(elements[j])
    X.append(x)
    Y.append(elements[m])

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# Get the parameters X for discovering the Y
q = int(input())
new_X = []
for i in range(q):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(m):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show it on the screen
result = model.predict(new_X)
for i in range(len(result)):
    print(round(result[i],2))
