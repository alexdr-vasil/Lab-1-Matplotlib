import matplotlib.pyplot as plt

data = []
totalX = []
totalY = []

with open("frames.dat") as f:
    for line in f:
        data.append([float(i) for i in line.split()])

for i in range(0, len(data), 2):
    totalX.append(data[i])
    totalY.append(data[i + 1])

tabN = [[1, 2], [3, 4], [5, 6]]
tabX = [[0, 0], [0, 0], [0, 0]]
tabY = [[0, 0], [0, 0], [0, 0]]

for i in range(0, 3):
    for j in range(0, 2):
        tabX[i][j], tabY[i][j] = totalX[tabN[i][j] - 1], totalY[tabN[i][j] - 1]

fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))

for i in range(0, 3):
    for j in range(0, 2):
        axs[i][j].plot(tabX[i][j], tabY[i][j])
        axs[i][j].set_title('Frame ' + str(tabN[i][j]))
        axs[i][j].minorticks_on()
        axs[i][j].grid(which='major', color='grey', linewidth=1)
        axs[i][j].grid(which='minor', color='grey', linestyle='dashed')
        axs[i][j].set_ylim([-12, 12])
plt.savefig("Frames.png")
plt.show()
