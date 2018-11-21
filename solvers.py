from mpmath import *
from sympy import *
import sympy as sp
import numpy as np
x = Symbol('x')

# Построение таблицы
def table_creating(f, start, finish, n, out):
    value_matrix = np.matrix(dtype=float)
    xi = f.subs(x, start)
    df = diff(f, x)
    h = (finish - start) / n
    for i in range(0, n):
        value_matrix[i,0] = xi
        value_matrix[i,1] = df.subs(x, xi)
        xi = start + i * h
    return value_matrix

# Вычисление разделенной разности
def split_difference(yi,yj,xi,xj):
    return (yj - yi) / (xj / xi)

# Создание таблицы разделенных разностей
def split_difference_table_creating(f, input_matrix):
    # Создание таблицы
    matrix_range = input_matrix.shape()[0]
    output_matrix = np.matrix(shape=(matrix_range + 2, matrix_range))
    # Заполнение первых 2 столбцов таблицы данными из исхдной таблицы
    for i in range(0, matrix_range):
        output_matrix[0,i] = input_matrix[0,i]
        output_matrix[1,i] = input_matrix[1,i]
    # Заполнение остальных столбцов
    for i in range(2, matrix_range):
        for j in range(0, matrix_range - i + 1):
            output_matrix[i,j] = split_difference(output_matrix[1,i],
                                                  output_matrix[1,j],
                                                  output_matrix[0,i],
                                                  output_matrix[0,j])
    return output_matrix



# Метод Ньютона
def newton_method(f, input_matrix, out):
    split_difference_table = split_difference_table_creating(f, input_matrix)


# Метод кубический сплайнов дефекта 1
def cube_splain(f, start, finish, step, out):


# Дискрентое среднеквадратичное приближение
def discrete_rms_approximation(out):

# Интегральное среднеквадратичное отклонение
def integral_rms_approximation(out):

# Метод обратного интерполирования
def inverse_interpolation_method(out):
