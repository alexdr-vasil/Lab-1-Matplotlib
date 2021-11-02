import matplotlib.pyplot as plt

names_of_files = ["001.dat", "002.dat", "003.dat", "004.dat", "005.dat"]

totalX = []
totalY = []
totalN = []

for file_name in names_of_files:
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            data.append(line.split())

    N = int(data[0][0])
    X = []
    Y = []

    for i in data[1:N + 1]:
        X.append(float(i[0]))
        Y.append(float(i[1]))

    totalX.append(X)
    totalY.append(Y)
    totalN.append(N)

for i in range(0, 5):
    plt.figure(i+1)
    if i == 3:
        plt.scatter(totalX[i], totalY[i], s=3)
    else:
        if i == 4:
            plt.scatter(totalX[i], totalY[i], s=1)
        else:
            plt.scatter(totalX[i], totalY[i])
    plt.title("Number of points: " + str(totalN[i]))
    plt.savefig("Frame " + str(i+1) + ".png")
plt.show()



