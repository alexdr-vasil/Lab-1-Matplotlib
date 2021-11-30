import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# Ввод данных из файла
with open("large.txt", 'r') as f:
    data = list(filter(lambda x: x, f.read().split('\n')))

# Выделим размерность N, матрицу A, столбец b
N = int(data[0])
A = np.array([[float(j) for j in i.split()] for i in data[1:N + 1]], dtype=np.float64)
b = np.array([[float(i) for i in data[-1].split()]], dtype=np.float64).transpose()

# Решим систему уравнений
x = linalg.solve(A, b).transpose()
bars = np.arange(1, x[0].size + 1)

# График
fig, axes = plt.subplots(1, 1)
axes.bar(bars, x[0])
axes.grid()
fig.savefig("large.png")
plt.show()
