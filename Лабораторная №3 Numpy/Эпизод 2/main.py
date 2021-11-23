import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 4):

    # Запись из файла
    with open("signal0" + str(i) + ".dat") as f:
        raw_signal = filter(lambda x: x, f.read().split('\n'))
        raw_signal = np.array([float(i) for i in raw_signal])

    # Обработка
    N = 10
    filtered_signal = np.cumsum(raw_signal, dtype=float)
    filtered_signal[N:] = filtered_signal[N:] - filtered_signal[:-N]
    for j in range(N):
        filtered_signal[j] /= (j + 1)
    filtered_signal[N:] /= N

    # Вывод в виде 2 графиков
    fig, axs = plt.subplots(1, 2)
    t = [i for i in range(raw_signal.size)]  # необработанный сигнал
    axs[0].plot(t, raw_signal)
    axs[0].minorticks_on()
    axs[0].grid(which='major', color='k', linewidth=1)
    axs[0].grid(which='minor', color='grey', linestyle=':')
    axs[0].set_title('Необработанный сигнал')

    t = [i for i in range(filtered_signal.size)]  # обработанный сигнал
    axs[1].plot(t, filtered_signal)
    axs[1].minorticks_on()
    axs[1].grid(which='major', color='k', linewidth=1)
    axs[1].grid(which='minor', color='grey', linestyle=':')
    axs[1].set_title('Обработанный сигнал')

    # Сохранение и вывод на экран
    plt.savefig("signal0" + str(i) + "_filtered.png")
    plt.show()
