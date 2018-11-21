from sympy.parsing.sympy_parser import parse_expr
import solvers as solv
import numpy as np

n = 5

var = 'var1'
in_file = open((var + '_in'), 'r')
out_file = open((var + '_out'), 'w')

# Ввод функции
f = parse_expr(in_file.read().replace('\n',''))
# Вычисление значений функции в точках
(points_vector, values_vector) = solv.table_creating(f, 1.0, 2.0, n)
# Вычисление полинома Ньютона
newton_polynomial = solv.newton_method(points_vector, values_vector, n)
# Вычисление полинома кубическими сплайнами
splain_polynomial = solv.cube_splain(points_vector, values_vector)

# Вывод точек, в которых значение функции известно
out_file.write((points_vector.__repr__() + '\n' + values_vector.__repr__() + '\n'))
# Вывод значений, с помощью метода Ньютона
out_file.write(('Полином Ньютона: ' + newton_polynomial.__repr__() + '\n'))
# Вывод значений, с помощью метода кубических сплайнов
out_file.write(('Полином методом кубических сплайнов: ' + splain_polynomial.__repr__() + '\n'))

in_file.close()
out_file.close()
quit()
