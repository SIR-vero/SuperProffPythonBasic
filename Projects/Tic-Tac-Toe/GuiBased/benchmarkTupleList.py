from datetime import datetime

x = tuple(range(10000000))
X = list(range(10000000))

sum = 0
n = datetime.now()
for i in range(10000000):
	sum = sum + x[i]
nn = datetime.now()
print(nn-n)

sum = 0
n = datetime.now()
for i in range(10000000):
	sum = sum + X[i]
nn = datetime.now()
print(nn-n)
