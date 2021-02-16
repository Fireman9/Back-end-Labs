import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

x = []
y = []


# Initialize X, Y for the plot
def initXY(fromNumber, toNumber, step):
    for i in np.arange(fromNumber, toNumber, step):
        x.append(round(i, 4))
        y.append(round(func(round(i, 4)), 4))


# Working function
def func(x1):
    if x1 <= 0 or x1 == 1:
        return np.nan
    else:
        return (x1 * x1) / np.log(x1)


# Print table to the console
def printTable(x, y):
    table = PrettyTable()
    table.field_names = ["x", "y"]
    for i in range(len(x)):
        table.add_row([x[i], y[i]])
    print(table)


# Build plot
def buildPlot(x, y):
    ax = plt.subplot()
    ax.plot(x, y, 'k')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    plt.show()


print("Функція x^2/ln(x)")
initXY(float(input("Введіть початкове число: ")),
       float(input("Введіть кінцеве число: ")),
       float(input("Введіть крок: ")))
printTable(x, y)
buildPlot(x, y)
