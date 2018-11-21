import solvers
from mpmath import *
from sympy import *
import sympy as sp
import numpy as np

var = 'test'
in_file = open((var + '_in'), 'r')
out_file = open((var + '_out'), 'w')

f = sp.parse_expr(in_file.input().replace('\n',''))
