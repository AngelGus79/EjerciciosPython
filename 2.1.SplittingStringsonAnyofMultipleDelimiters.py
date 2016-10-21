"""
Procesamiento de cadenas. Una funcion mas flexible que el metodo split para la division
de cadenas, es el split del modulo re para realizar divisiones con multiples delimitadores
"""

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

print(re.split(r'[;,\s]\s*', line))
#acepta punto y coma (;) coma (,) espacios en blanco (\s) seguidos por cualquier cantidad
#de espacios en blanco \s*
