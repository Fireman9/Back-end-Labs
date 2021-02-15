import matplotlib.pyplot as plt
import numpy as np

x = []
y = []


def initXY(fromNumber, toNumber, step):
    for i in np.arange(fromNumber, toNumber, step):
        x.append(round(i, 4))
        y.append(round(f(round(i, 4)), 4))


def f(x1):
    if x1 <= 0 or x1 == 1:
        return np.nan
    else:
        return (x1 * x1) / np.log(x1)


def printTable(x, y):
    print("x y")
    for i in range(len(x)):
        print(x[i], y[i])


print("Функція x^2/ln(x)")
initXY(float(input("Введіть початкове число: ")),
       float(input("Введіть кінцеве число: ")),
       float(input("Введіть крок: ")))
printTable(x, y)
plt.plot(x, y, 'k')
plt.show()
