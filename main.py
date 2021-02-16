import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable


# plot's dots coordinates
x = []
y = []


# Initialize X, Y for the plot
def init_xy(from_number, to_number, step):
    precision = 7
    for i in np.arange(from_number, to_number, step):
        # add new dot to plot
        # new_x = i rounded to {precision} digits
        new_x = round(i, precision)
        x.append(new_x)
        # new_y = func(new_x) rounded to {precision} digits
        new_y = round(func(new_x), precision)
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


# Find and print x coordinates where func intersect X axis
def print_x_axis_intersection_coordinates():
    x_axis_intersection_coordinates = []
    for i in range(len(y)):
        if y[i] == 0:
            x_axis_intersection_coordinates.append(x[i])
    if len(x_axis_intersection_coordinates) > 0:
        print("Функція перетинає вісь Х у точках:", x_axis_intersection_coordinates)
    else:
        print("Функція не перетинає вісь Х")


# Find and print coordinates where func does not exists
def print_non_existence_coordinates():
    non_existence_coordinates = []
    for i in range(len(y)):
        if np.isnan(y[i]):
            non_existence_coordinates.append(x[i])
    if len(non_existence_coordinates) > 0:
        print("Функція не існує у точках:", non_existence_coordinates)
    else:
        print("Функція існує в усіх точках")


print("Функція x^2/ln(x)")
init_xy(float(input("Введіть початкове число: ")),
        float(input("Введіть кінцеве число: ")),
        float(input("Введіть крок: ")))
print_table()
print_x_axis_intersection_coordinates()
print_non_existence_coordinates()
build_plot()
