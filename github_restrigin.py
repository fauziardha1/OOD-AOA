from matplotlib import cm
import math
import matplotlib.pyplot as plt
import numpy as np

def rastrigin(*X, **kwargs):
    A = kwargs.get('A', 10)
    return A + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])
    # X adalah [1,2,3,4,5,...]
    # x adalah 1 atau 2 dst

if __name__ == '__main__':
    X = np.linspace(-4, 4, 200)    
    Y = np.linspace(-4, 4, 200)    

    X, Y = np.meshgrid(X, Y)

    Z = rastrigin(X, Y, A=10)
    # exit()
    # print(f"len X: {X},len y: {Y}, len Z: {Z}")
    # exit()

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap= cm.plasma, linewidth=0, antialiased=False)    
    plt.show()