import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from tabulate import *

import solvers as solv

n = 5

var = 'var1'
in_file = open((var + '_in'), 'r')
out_file = open((var + '_out'), 'w')

# Ввод функции
f = parse_expr(in_file.read().replace('\n', ''))
# Вычисление значений функции в точках
(points_vector, values_vector) = solv.table_creating(f, 1.0, 2.0, n)
# Вычисление полинома Ньютона
newton_polynomial, out_table_newton = solv.newton_method(points_vector, values_vector, n)
# Вычисление полинома кубическими сплайнами
splain_polynomial, out_table_splain = solv.cube_splain(points_vector, values_vector)

# Вывод точек, в которых значение функции известно
out_file.write(
    tabulate(np.column_stack((points_vector.transpose(), values_vector.transpose())), headers=['x', 'f(x)']) + '\n\n')
# Вывод значений, с помощью метода Ньютона
out_file.write(('Полином Ньютона:\n' + tabulate(out_table_newton) + '\n\n' +
                tabulate(solv.interpolation_analysis([1.1, ..., 1.9], [1.0, ..., 2.0], f, newton_polynomial),
                         headers=['x', 'f(x)', 'Pn(x)', 'Delta', 'Оценка'])))
# Вывод значений, с помощью метода кубических сплайнов
out_file.write(('Полином методом кубических сплайнов: ' + splain_polynomial.__repr__() + '\n'))

in_file.close()
out_file.close()
quit()
