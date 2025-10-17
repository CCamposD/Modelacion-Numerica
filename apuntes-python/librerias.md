# 📌 Apunte de librerías en Python

## 👉 Resumen:
- numpy → cálculos y arrays.
- matplotlib.pyplot → gráficos.

## 1. NumPy (`import numpy as np`)
- Librería principal para **cálculo numérico** en Python.  
- Permite trabajar con **arrays (vectores y matrices)** de manera eficiente.  
- Incluye funciones matemáticas optimizadas.

### Ejemplos:
```python
import numpy as np

# Crear arrays
x = np.arange(-9, 1, 0.1)     # array de -9 a 1 con paso 0.1
y = np.linspace(0, 1, 5)      # 5 puntos equidistantes entre 0 y 1

# Funciones matemáticas vectorizadas
z = np.cos(x)                 # coseno de cada valor en x
r = np.sqrt(np.array([1,4,9])) # raíz cuadrada de cada elemento

# Propiedades
print(x.shape)   # dimensiones del array
print(x.size)    # cantidad de elementos
```

## 2. Matplotlib (Pyplot) (`import matplotlib.pyplot as plt`)
- Librería estándar para gráficos en Python.
- Muy usada en matemáticas, ciencia de datos e ingeniería.

### Ejemplos:

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(-5, 5, 100)
y = np.sin(x)

# Graficar
plt.plot(x, y, label="sin(x)")

# Personalizar
plt.title("Ejemplo de gráfico")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

# Ejes de referencia
plt.axhline(0, color="black")
plt.axvline(0, color="black")

# Mostrar
plt.show()
```
