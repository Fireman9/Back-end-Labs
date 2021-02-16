import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

# plot's dots coordinates
x = []
y = []


# Initialize X, Y for the plot
def init_xy(from_number, to_number, step):
    for i in np.arange(from_number, to_number, step):
        # add new dot to plot
        # new_x = i rounded to 4 digits
        new_x = round(i, 4)
        x.append(new_x)
        # new_y = func(new_x) rounded to 4 digits
        new_y = round(func(new_x), 4)
        y.append(new_y)


# Working function
def func(param):
    if param <= 0 or param == 1:
        return np.nan
    else:
        return (param * param) / np.log(param)


# Print table to the console
def print_table():
    table = PrettyTable()
    table.field_names = ["x", "y"]
    for i in range(len(x)):
        table.add_row([x[i], y[i]])
    print(table)


# Build plot
def build_plot():
    ax = plt.subplot()
    ax.plot(x, y, 'k')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    plt.show()


print("Функція x^2/ln(x)")
init_xy(float(input("Введіть початкове число: ")),
        float(input("Введіть кінцеве число: ")),
        float(input("Введіть крок: ")))
print_table()
build_plot()
