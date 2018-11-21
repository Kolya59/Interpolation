from mpmath import *
from sympy import *
from scipy import interpolate
import numpy as np

x = Symbol('x')


# Построение таблицы
def table_creating(f, start, finish, n):
    point_matrix = np.zeros(n + 1)
    value_matrix = np.zeros(n + 1)
    xi = start
    df = diff(f, x)
    h = (finish - start) / n
    for i in range(0, n + 1):
        point_matrix[i] = xi
        value_matrix[i] = df.subs(x, xi)
        xi += h
    return point_matrix, value_matrix


# Вычисление разделенной разности
def split_difference(yi, yj, xi, xj):
    return (yj - yi) / (xj / xi)


# Создание таблицы разделенных разностей
def split_difference_table_creating(x_points, y_points):
    # Создание таблицы
    n = len(x_points)
    output_matrix = np.zeros([n, n], dtype=float)
    # Заполнение первых 2 столбцов таблицы данными из исхдной таблицы
    for i in range(0, n):
        output_matrix[i,0] = y_points[i]
    # Заполнение остальных столбцов
    for j in range(1, n):
        for i in range(j, n):
            output_matrix[i, j] = float(output_matrix[i, j - 1] - output_matrix[i - 1, j - 1]) \
                                  / float(x_points[i] - x_points[i - j])
    return output_matrix


# Метод Ньютона
def newton_method(x_points, y_points, n):
    # Построение таблицы разделенных разностей
    split_difference_table = split_difference_table_creating(x_points, y_points)
    # Вычисление Полинома
    newton_polynomial = 0
    for i in range(0, n):
        next_elem = split_difference_table[i, i]
        for j in range(0, i):
            next_elem *= (x - x_points[j])
        newton_polynomial += next_elem

    return newton_polynomial

# Метод кубический сплайнов дефекта 1
def cube_splain(x_points, y_points):
    return interpolate.CubicSpline(x_points, y_points)

# Дискрентое среднеквадратичное приближение
# def discrete_rms_approximation(out):

# Интегральное среднеквадратичное отклонение
# def integral_rms_approximation(out):

# Метод обратного интерполирования
# def inverse_interpolation_method(out):
