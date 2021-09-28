import numpy as np

t = x2 = input("enter the number of Rows and columns(IN A FORM OD M*M): ").split()
t[0] = int(t[0])
t[1] = int(t[1])
n = t[0]
m = t[1]

list1 = []
for i in range(0, n):
    x1 = list(map(float, input("Enter heights as a matrix: ").split(' ')[:m]))
    list1.append(x1)


h1 = []
h1.append(list1[0][0])
h1.append(list1[0][m - 1])
h1.append(list1[n - 1][0])
h1.append(list1[n - 1][m -1])


h2 = []
for i in range(1, (m - 1)):
    c = list1[0][i]
    h2.append(c)

for i in range(1, (m - 1)):
    c = list1[n - 1][i]
    h2.append(c)

for i in range(1, (n - 1)):
    c = list1[i][0]
    h2.append(c)

for i in range(1, (n - 1)):
    c = list1[i][m - 1]
    h2.append(c)


h4 = []

for i in range(1, (n -1)):
    for j in range(1, (m - 1)):
        d = list1[i][j]
        h4.append(d)

h = float(input("enter the maximum heights: ")) + 5
a = float(input("Enter the area of each square: "))


r = np.absolute((np.sum(h1) - (len(h1) * h)))
yy = 2 * np.absolute((np.sum(h2) - (len(h2) * h)))
yyy = 4 * np.absolute((np.sum(h4) - (len(h4) * h)))
p = np.absolute(r) + np.absolute(yy) + np.absolute(yyy)

v = (a / 4) * p

print(v)