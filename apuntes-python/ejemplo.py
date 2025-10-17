# ================================
# Ejemplo con NumPy y Matplotlib
# ================================

# Importamos las librerías
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Parte 1: Uso de NumPy
# ----------------------------

# Creamos un array de valores en el rango [-5, 5] con paso 0.1
x = np.arange(-5, 5, 0.1)

# Aplicamos funciones matemáticas a todo el array
y1 = np.sin(x)     # seno de cada valor
y2 = np.cos(x)     # coseno de cada valor

# ----------------------------
# Parte 2: Uso de Matplotlib
# ----------------------------

# Dibujamos la primera función
plt.plot(x, y1, label="sin(x)", color="blue")

# Dibujamos la segunda función
plt.plot(x, y2, label="cos(x)", color="red")

# Personalizamos el gráfico
plt.title("Ejemplo: Gráfico con NumPy + Matplotlib")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()        # muestra qué línea corresponde a cada función
plt.grid(True)      # agrega grilla para facilitar la lectura

# Dibujamos los ejes de referencia
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# Mostramos el gráfico en pantalla
plt.show()
