import numpy as np
import matplotlib.pyplot as plt

def polaczenie(kropki):
    pozycja_x = np.random.rand(kropki)
    pozycja_y = np.random.rand(kropki)

    plt.scatter(pozycja_x, pozycja_y)

    for i in range(kropki):
        for j in range(i + 1, kropki):
            plt.plot([pozycja_x[i], pozycja_x[j]], [pozycja_y[i], pozycja_y[j]], 'k-', lw=0.1)

    plt.show()

kropki = int(input("Podaj liczbę: "))
polaczenie(kropki)
