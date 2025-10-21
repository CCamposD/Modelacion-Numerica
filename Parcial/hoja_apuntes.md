# 🧮 Hoja de Apuntes - Modelación Numérica (2025 - 2C)

## Unidad 1: Errores

### 🔹 Tipos de Errores
- **Error absoluto:** \( e_a = |x - x_{real}| \)
- **Error relativo:** \( e_r = \frac{e_a}{|x_{real}|} \)
- **Error porcentual:** \( e_p = e_r \times 100 \)

### 🔹 Propagación de errores
| Caso | Error inherente | Error redondeo | Error discretización | Error final |
|------|------------------|----------------|-------------------------|--------------|
| I | Nulo | Nulo | Nulo | Nulo |
| II | No nulo | Nulo | Nulo | Depende del problema numérico |
| III | Nulo | No nulo | Nulo | Depende del algoritmo |
| IV | Nulo | Nulo | No nulo | Error de discretización |

### 🔹 Cifras significativas
- Son los números que expresan la precisión de una medición.
- Ejemplo: 0,020 → 2 cifras significativas.

---

## Unidad 2: Ecuaciones no lineales

### 🔸 Método de Bisección
**Objetivo:** Encontrar una raíz de \( f(x) = 0 \) en [a, b].

**Condición:** \( f(a) \times f(b) < 0 \)

**Fórmula:**
\[
 x_r = \frac{a + b}{2}
\]

**Procedimiento:**
1. Calcular \( x_r \)
2. Evaluar \( f(x_r) \)
3. Si \( f(a)f(x_r) < 0 \Rightarrow b = x_r \), si no \( a = x_r \)
4. Repetir hasta que \( |b - a| < tol \)

**Orden de convergencia:** lineal.

---

### 🔸 Método de Regula-Falsi (Falsa Posición)
**Fórmula:**
\[
 x_r = b - f(b) \frac{(a - b)}{f(a) - f(b)}
\]

**Igual proceso** que bisección pero reemplaza el punto medio por esta fórmula. Converge más rápido, pero sigue siendo lineal.

---

### 🔸 Método del Punto Fijo
**Reescritura:** \( x = g(x) \)

**Iteración:** \( x_{k+1} = g(x_k) \)

**Condición de convergencia:** \( |g'(x)| < 1 \) cerca de la raíz.

**Orden de convergencia:** lineal.

---

### 🔸 Método de Newton-Raphson
**Fórmula:**
\[
 x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
\]

**Condiciones:**
- f y f' deben ser continuas.
- \( f'(x) \neq 0 \).

**Orden de convergencia:** cuadrática.

**Variables:**
- \( x_k \): aproximación actual
- \( f(x_k) \): valor de la función
- \( f'(x_k) \): derivada de la función

---

### 🔸 Método de la Secante
**Fórmula:**
\[
 x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}
\]

**No requiere derivada.**
**Orden de convergencia:** \( \approx 1.618 \) (superlineal).

---

### 🔸 Newton-Raphson para raíces múltiples
**Fórmula:**
\[
 x_{k+1} = x_k - \frac{f(x_k) f'(x_k)}{[f'(x_k)]^2 - f(x_k)f''(x_k)}
\]

**Orden de convergencia:** cuadrática si la raíz es simple, lineal si es múltiple.

---

### 🔸 Orden de convergencia
\[
\lim_{k \to \infty} \frac{|x_{k+1} - r|}{|x_k - r|^p} = C
\]

Donde:
- \( p \): orden de convergencia (1 = lineal, 2 = cuadrática)
- \( C \): constante de convergencia

---

## Unidad 3: Ajuste de Curvas

### 🔸 Ajuste por cuadrados mínimos (lineal)
Queremos ajustar una recta: \( y = a + bx \)

**Fórmulas:**
\[
 b = \frac{n\sum xy - (\sum x)(\sum y)}{n\sum x^2 - (\sum x)^2}
\]
\[
 a = \bar{y} - b\bar{x}
\]

**Error cuadrático medio (ECM):**
\[
 ECM = \frac{1}{n}\sum (y_i - (a + bx_i))^2
\]

---

### 🔸 Ajuste cuadrático y cúbico
- Cuadrático: \( y = a + bt + ct^2 \)
- Cúbico: \( y = a + bt + ct^2 + dt^3 \)

Coeficientes se obtienen con matrices normales (\( A^T A x = A^T y \)) o `np.polyfit(x, y, grado)`.

---

### 🔸 Ajuste exponencial
\[
 y = e^{a - bt}
\]
Tomando logaritmos:
\[
 \ln(y) = a - bt
\]
Aplicar regresión lineal entre \( t \) y \( \ln(y) \).

---

### 🔸 Interpolación polinómica
Usa los puntos exactos para que el polinomio pase por ellos.

#### Polinomio de Lagrange:
\[
 P(x) = \sum_{i=0}^{n} y_i L_i(x), \quad L_i(x) = \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}
\]

#### Polinomio de Newton:
Usa diferencias divididas.
\[
 P(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + \ldots
\]

**Error de interpolación:**
\[
E(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)
\]

#### Nodos de Chebyshev:
Distribuyen los puntos para minimizar el error de oscilación (fenómeno de Runge).
\[
 x_i = \cos\left(\frac{2i+1}{2n+2}\pi\right), \quad i = 0,1,...,n
\]

#### Polinomio de Hermite:
Interpola usando valores y derivadas conocidas.

---

## Unidad 5: Diferenciación e Integración Numérica

### 🔸 Diferenciación numérica
#### Aproximaciones:
\[
 f'(x) \approx \frac{f(x+h) - f(x)}{h} \quad \text{(diferencia hacia adelante)}
\]
\[
 f'(x) \approx \frac{f(x) - f(x-h)}{h} \quad \text{(diferencia hacia atrás)}
\]
\[
 f'(x) \approx \frac{f(x+h) - f(x-h)}{2h} \quad \text{(centrada)}
\]

**Error de truncamiento:** \( O(h) \) o \( O(h^2) \) según el método.

---

### 🔸 Integración numérica

#### Regla del trapecio:
\[
 I = \frac{h}{2} [f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n)]
\]
**Error:** \( E_t = -\frac{(b-a)h^2}{12}f''(\xi) \)

#### Regla de Simpson 1/3:
\[
 I = \frac{h}{3} [f(x_0) + 4f(x_1) + 2f(x_2) + \ldots + 4f(x_{n-1}) + f(x_n)]
\]
**Error:** \( E_t = -\frac{(b-a)h^4}{180}f^{(4)}(\xi) \)

#### Regla de Simpson 3/8:
\[
 I = \frac{3h}{8}[f(x_0) + 3f(x_1) + 3f(x_2) + 2f(x_3) + ... + f(x_n)]
\]

#### Richardson (mejora de estimación):
\[
 R = T(h_2) + \frac{T(h_2) - T(h_1)}{(h_1/h_2)^p - 1}
\]
Donde \( p \) es el orden del método.

---

✅ **Consejos generales:**
- Verificar siempre continuidad de f(x) y derivadas antes de aplicar Newton.
- Normalizar variables antes de ajustar.
- Revisar tolerancia y error relativo en iteraciones.
- Usar Chebyshev cuando se interpola con muchos puntos.

---
**Fin de la hoja de apuntes** ✨

