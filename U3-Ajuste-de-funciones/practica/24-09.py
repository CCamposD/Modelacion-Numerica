# Ejercicios
import numpy as np
import matplotlib.pyplot as plt

# 1.- Primer ejercicio

# Definir la función
f = lambda x: (3/5) ** (15/7 * np.cos(3*x)) - 2*x

# Rango de valores de x (de -9 a 1 con paso 0.1)
x = np.arange(-9, 1, 0.1)

# Evaluar f(x)
y = f(x)

# Graficar
plt.plot(x, y, label="f(x)")
plt.axhline(0, color="black", linewidth=0.8)  # eje x
plt.axvline(0, color="black", linewidth=0.8)  # eje y
plt.legend()
plt.grid(True)
plt.show()

# 2.- Ejercicio

df = lambda x: -27/7**((15/7 * np.cos(3*x))) - np.sin(3*x)-2
y2 = df(x)
# Graficar
plt.plot(x, abs(y2), label="df(x)")
plt.axhline(0, color="black", linewidth=0.8)  # eje x
plt.axvline(0, color="black", linewidth=0.8)  # eje y
plt.legend()
plt.grid(True)
plt.show()
