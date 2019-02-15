import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([1, 2, 3, 4, 5, 6, 7])
x = np.zeros((7, 7))
# x = a + (b - 1) * 7
i = 0
while i < len(a):
    j = 0
    while j < len(b):
        x[i][j] = a[i] + (b[j] - 1) * 7
        j = j + 1
    i = i + 1
# generate from 1 to 49
print(x)

y = 1
k = []
while y <= 40:
    k.append((y - 1) % 10 + 1)
    y = y + 1
# generate from 1 to 10 with the same probability
print(k)
