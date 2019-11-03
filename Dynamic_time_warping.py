import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import isinf


# plt.plot(x,'r', label='x')
# plt.plot(y, 'g', label='y')
# plt.legend();

# def DTWDistance(n, m, dist, warp=1, w=np.inf, s=1.0):
def DTWDistance(n, m):
    DTW = np.zeros((len(n), len(m)))
    for i in range(len(m)):
        for j in range(len(n)):
            DTW[i, j] = DTWDynamic(np.fabs(n[i][j] - m[i][j]), DTW, i, j)

    return DTW, DTW[19][19]


def DTWDynamic(cost, DTW, i, j):
    if j != len(DTW) - 1:
        var = (cost + np.amin([DTW[i, j],
                               DTW[i, j - 1],
                               DTW[i, j + 1]
                               ]))
    else:
        var = (cost + np.amin([DTW[i, j],
                               DTW[i, j - 1],

                               ]))

    # DTW[i, j]]))
    # [DTW[i - 1, j],
    #  DTW[i, j - 1],
    #  DTW[i - 1, j - 1]]
    return var


def plotG(n, m, c):
    z = n.ravel()
    k = m.ravel()
    B = c.ravel()

    B = B.astype(int)
    print("z", z)
    print("k", k)
    print("B", B)
    size = []

    for i in range(0, z.size):
        size = np.append(size, i)

    plt.plot(z, size, 'r', 'x')
    plt.plot(k, size, 'g', 'y')
    size = []
    for i in range(0, B.size):
        size = np.append(size, i)
    plt.plot(B, size, 'b', 'L')
    plt.show()


def averagePointDifference(arr):
    cost = 0
    # for i in range(arr.shape[1]-1):
    #     for j in range(arr.shape[0]-1):
    for i in range(len(arr)):
        for j in range(len(arr[0])):

            if i != 20 & j != 20:
                cost += arr[i][j]

    size = np.multiply(arr.size, arr[0].size)
    return np.divide(cost, size)
    return 21
