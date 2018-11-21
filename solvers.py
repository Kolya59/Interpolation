import numpy as np
from mpmath import *
from scipy import interpolate
from sympy import *

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


# Анализ результатов интерполяции
def interpolation_analysis(x_points, start_x_points, f, inter_f):
    result_table = np.zeros((len(x_points), 5), dtype=float)
    for i in range(len(x_points)):
        result_table[i, 0] = x_points[i]
        result_table[i, 1] = f.subs(x, x_points[i])
        result_table[i, 2] = inter_f[i].subs(x, x_points[i])
        result_table[i, 3] = abs(result_table[i, 1] - result_table[i, 2])
        w = 1
        for k in range(i + 1):
            w *= x_points[i] - start_x_points[k]
        result_table[i, 4] = abs(diff(f, x, i).subs(x, x_points[i]) / factorial(i + 1) * w)
    return result_table


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
        output_matrix[i, 0] = y_points[i]
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
    # TODO: Доделать корректное типизирвоание для sympy_exr
    newton_polynomial_list = np.zeros(n, dtype=)
    for i in range(0, n):
        next_elem = split_difference_table[i, i]
        for j in range(0, i):
            next_elem *= (x - x_points[j])
        newton_polynomial += next_elem
        newton_polynomial_list[i] = (newton_polynomial)
    out_table = np.column_stack((x_points.transpose(), split_difference_table))
    return newton_polynomial_list, out_table


# Метод кубический сплайнов дефекта 1
def cube_splain(x_points, y_points):
    out_table_splain = []
    return interpolate.CubicSpline(x_points, y_points), out_table_splain

# Дискрентое среднеквадратичное приближение
# def discrete_rms_approximation(out):

# Интегральное среднеквадратичное отклонение
# def integral_rms_approximation(out):

# Метод обратного интерполирования
# def inverse_interpolation_method(out):
