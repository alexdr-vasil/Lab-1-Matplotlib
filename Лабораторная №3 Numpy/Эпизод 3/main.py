import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Функции для анимации
def init():
    global line
    line.set_data([], [])
    return line,


def animate(i):
    global x, all_U, line
    y = all_U[i][0]
    line.set_data(x, y)
    return line,


# Ввод данных из файла
with open('start.dat', 'r') as f:
    u = filter(lambda x: x, f.read().split('\n'))

u = np.array([[float(i) for i in u]])

# График для вывода
fig = plt.figure()
x = [i for i in range(u[0].size)]
ax = plt.axes(xlim=(min(x), max(x)), ylim=(min(u[0]), max(u[0])))
line, = ax.plot([], [], lw=3)

# Создание матрицы A
A = np.eye(u[0].size)
B = -np.roll(A, -1, axis=1)
A = A + B

# Значения по 255 шагам
all_U = []
for _ in range(256):
    all_U.append(u)
    u = u - 0.5 * np.dot(A, u.transpose()).transpose()

# Анимация
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)
ax.minorticks_on()
ax.grid(which='major', color='k', linewidth=1)
ax.grid(which='minor', color='grey', linestyle=':')

# Сохраниние и вывод на экран
anim.save('func_animation.gif', writer='pillow', fps=30)
plt.show()
