# 🧮 Hoja de Apuntes - Modelación Numérica (Versión Extendida)

## 🧩 Unidad 1: Errores

### 🔹 Tipos de errores
- **Error absoluto:** \( e_a = |x - x_{real}| \) → Diferencia entre el valor verdadero y el medido.
- **Error relativo:** \( e_r = \frac{e_a}{|x_{real}|} \) → Proporción del error respecto al valor real.
- **Error porcentual:** \( e_p = e_r \times 100 \) → Error expresado en porcentaje.

### 🔹 Propagación de errores
| Caso | Error Inherente | Error Redondeo | Error Discretización | Error Final |
|:----:|:----------------:|:---------------:|:---------------------:|:-------------:|
| I | Nulo | Nulo | Nulo | Nulo |
| II | No nulo | Nulo | Nulo | Depende solo del problema numérico |
| III | Nulo | No nulo | Nulo | Depende del algoritmo |
| IV | Nulo | Nulo | No nulo | Error de discretización (cuando P.M ≠ P.N) |

### 🔹 Cifras significativas
- Indican el nivel de precisión del número medido.
- Ejemplo: 0,020 → 2 cifras significativas.

---

## ⚙️ Unidad 2: Ecuaciones no lineales

### 🔸 Método de Bisección
**Objetivo:** Encontrar una raíz de \( f(x) = 0 \) en un intervalo [a, b].  
**Condición:** \( f(a) \times f(b) < 0 \)

**Fórmula:**
\[ x_r = \frac{a + b}{2} \]

**Pasos:**
1. Calcular \( x_r \)
2. Evaluar \( f(x_r) \)
3. Si \( f(a)f(x_r) < 0 \Rightarrow b = x_r \), si no \( a = x_r \)
4. Repetir hasta que \( |b - a| < tol \)

**Convergencia:** lineal.

---

### 🔸 Método de Regula-Falsi (Falsa posición)
**Fórmula:**
\[ x_r = b - f(b) \frac{(a - b)}{f(a) - f(b)} \]

Usa el mismo criterio que Bisección pero mejora el punto medio con una interpolación lineal.  
**Convergencia:** lineal (más rápida que bisección).

---

### 🔸 Método de Punto Fijo
**Reescritura:** \( x = g(x) \)

**Iteración:** \( x_{k+1} = g(x_k) \)

**Condición de convergencia:** \( |g'(x)| < 1 \)

**Convergencia:** lineal.

---

### 🔸 Método de Newton-Raphson
**Fórmula:**
\[ x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)} \]

**Condiciones:**
- f y f' deben ser continuas.
- \( f'(x) \neq 0 \).

**Convergencia:** cuadrática.

**Significado de símbolos:**
- \( x_k \): aproximación actual.
- \( f(x_k) \): valor de la función.
- \( f'(x_k) \): derivada de la función.

---

### 🔸 Método de la Secante
**Fórmula:**
\[ x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})} \]

**Ventajas:**
- No requiere derivada.
- **Orden de convergencia:** ≈ 1.618 (superlineal).

---

### 🔸 Newton-Raphson para raíces múltiples
**Fórmula:**
\[ x_{k+1} = x_k - \frac{f(x_k) f'(x_k)}{[f'(x_k)]^2 - f(x_k)f''(x_k)} \]

**Convergencia:** cuadrática para raíces simples, lineal para múltiples.

---

### 🔸 Orden de convergencia
\[ \lim_{k→∞} \frac{|x_{k+1} - r|}{|x_k - r|^p} = C \]
- \( p \): orden de convergencia (1 = lineal, 2 = cuadrática)
- \( C \): constante de convergencia.

---

## 📈 Unidad 3: Ajuste de Curvas e Interpolación

### 🔸 Ajuste lineal por cuadrados mínimos
Queremos ajustar una recta: \( y = a + bx \)

**Fórmulas:**
\[ b = \frac{nΣxy - (Σx)(Σy)}{nΣx^2 - (Σx)^2} \]
\[ a = \bar{y} - b\bar{x} \]

**Error cuadrático medio:**
\[ ECM = \frac{1}{n} Σ (y_i - (a + bx_i))^2 \]

**Interpretación:** mide qué tan bien el modelo ajusta los datos.

---

### 🔸 Ajustes cuadrático y cúbico
- Cuadrático: \( y = a + bt + ct^2 \)
- Cúbico: \( y = a + bt + ct^2 + dt^3 \)

Coeficientes: \( (A^TA)x = A^Ty \)  o con `np.polyfit(x, y, grado)`.

---

### 🔸 Ajuste exponencial
\[ y = e^{a - bt} \]
Transformación logarítmica:
\[ \ln(y) = a - bt \]
Se aplica regresión lineal entre t y ln(y).

---

### 🔸 Interpolación Polinómica
Interpola todos los puntos exactos (pasa por cada uno).

#### Polinomio de Lagrange
\[ P(x) = Σ y_i L_i(x), \quad L_i(x) = Π_{j≠i} \frac{x - x_j}{x_i - x_j} \]

#### Polinomio de Newton (diferencias divididas)
\[ P(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + ... \]

**Error:**
\[ E(x) = \frac{f^{(n+1)}(ξ)}{(n+1)!} Π(x - x_i) \]

#### Nodos de Chebyshev
Minimizan oscilaciones (fenómeno de Runge).
\[ x_i = \cos\left(\frac{2i+1}{2n+2}π\right) \]

#### Polinomio de Hermite
Usa valores y derivadas conocidas para interpolar.

---

## 🧮 Unidad 5: Diferenciación e Integración Numérica

### 🔸 Diferenciación Numérica
#### Fórmulas
- Hacia adelante: \( f'(x) ≈ \frac{f(x+h) - f(x)}{h} \)
- Hacia atrás: \( f'(x) ≈ \frac{f(x) - f(x-h)}{h} \)
- Centrada: \( f'(x) ≈ \frac{f(x+h) - f(x-h)}{2h} \)

**Error de truncamiento:** O(h) o O(h²).

---

### 🔸 Integración Numérica
#### Regla del trapecio
\[ I = \frac{h}{2} [f(x_0) + 2Σf(x_i) + f(x_n)] \]
**Error:** \( E_t = -\frac{(b-a)h^2}{12}f''(ξ) \)

#### Simpson 1/3
\[ I = \frac{h}{3} [f(x_0) + 4f(x_1) + 2f(x_2) + ... + 4f(x_{n-1}) + f(x_n)] \]
**Error:** \( E_t = -\frac{(b-a)h^4}{180}f^{(4)}(ξ) \)

#### Simpson 3/8
\[ I = \frac{3h}{8}[f(x_0) + 3f(x_1) + 3f(x_2) + 2f(x_3) + ... + f(x_n)] \]

#### Extrapolación de Richardson
\[ R = T(h_2) + \frac{T(h_2) - T(h_1)}{(h_1/h_2)^p - 1} \]
Donde \( p \) es el orden del método.

---

✅ **Consejos finales**
- Revisar continuidad de f(x) y f'(x) antes de Newton.
- Normalizar variables para estabilidad numérica.
- Usar tolerancia y error relativo como criterio de parada.
- Preferir nodos de Chebyshev al interpolar con muchos puntos.

---
📘 **Fin de la versión extendida**

