import math
import numpy as np
import matplotlib.pyplot as plt   # alias correcto

# Parámetros
a = 0.25
b = 0.75
c = -2.e18
d = (-a + b - a - a)  # * c
print(d)

# Definiciones de funciones
f = lambda x: x - 2.0123411
g = lambda x: np.power(x, 2) - 2.043

# Rango de valores
x = np.arange(-5, 6)           # enteros de -5 a 5
# x = np.arange(-5, 5.1, 0.2)  # con paso 0.2

# Evaluaciones
y = f(x)
y2 = g(x)

# Gráfico con ambas funciones
plt.plot(x, y, 'r', label='f(x) = x - 2.0123411')
plt.plot(x, y2, 'b', label='g(x) = x^2 - 2.043')
plt.grid(True)
plt.legend()
plt.show()
