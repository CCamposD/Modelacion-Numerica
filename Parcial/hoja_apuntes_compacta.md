# 📘 Hoja de Apuntes – Modelación Numérica (Versión Compacta)

---

## 🧮 Unidad 1: Errores

### Errores
- **Error absoluto:**  `Ea = |x_real - x_aprox|`
- **Error relativo:**  `Er = Ea / |x_real|`
- **Porcentaje error:** `Er% = Er * 100`
- **Error de redondeo:** Por límite de representación numérica
- **Error de truncamiento:** Por aproximar una expresión matemática

### Propagación de errores
- Suma/resta:  `Ea(f) = Ea(a) + Ea(b)`
- Multiplicación/división:  `Er(f) = Er(a) + Er(b)`

---

## 🧠 Unidad 2: Ecuaciones No Lineales

### Método de Bisección
- Fórmula:  `xr = (a + b) / 2`
- Criterio:  `f(a)*f(xr) < 0 → b = xr`, sino `a = xr`
- Error: `Ea = |xr - xr-1|`

### Método de Regula Falsi
- `xr = (a*f(b) - b*f(a)) / (f(b) - f(a))`

### Método de Punto Fijo
- Transformar `f(x)=0` en `x = g(x)`
- Iteración: `x_{i+1} = g(x_i)`
- Convergencia: `|g'(x)| < 1`

### Newton-Raphson
- `x_{i+1} = x_i - f(x_i)/f'(x_i)`
- Error estimado: `Ea = |x_{i+1} - x_i|`

### Método de la Secante
- `x_{i+1} = x_i - f(x_i)(x_i - x_{i-1}) / (f(x_i) - f(x_{i-1}))`

### Orden de Convergencia
- `p = log(|e_{n+1}/e_n|) / log(|e_n/e_{n-1}|)`

---

## 📈 Unidad 3: Ajuste de Curvas e Interpolación

### Cuadrados mínimos (lineal)
- `y = a + b x`
- `b = [nΣxy - ΣxΣy] / [nΣx² - (Σx)²]`
- `a = (Σy - bΣx)/n`

### Polinomio de Lagrange
- `P(x) = Σ [y_i * L_i(x)]`
- `L_i(x) = Π_{j≠i} (x - x_j)/(x_i - x_j)`

### Polinomio de Newton
- `P(x) = f[x0] + f[x0,x1](x - x0) + f[x0,x1,x2](x - x0)(x - x1) + ...`

### Error de Interpolación
- `E(x) = f⁽ⁿ⁺¹⁾(ξ)/(n+1)! * Π(x - x_i)`

### Nodos de Chebyshev
- `x_i = cos((2i - 1)π / 2n)`

---

## 🔧 Unidad 5: Diferenciación e Integración Numérica

### Derivación Numérica
- **Hacia adelante:** `f'(x) ≈ [f(x+h) - f(x)] / h`
- **Hacia atrás:** `f'(x) ≈ [f(x) - f(x-h)] / h`
- **Centrada:** `f'(x) ≈ [f(x+h) - f(x-h)] / (2h)`
- **Segunda derivada:** `f''(x) ≈ [f(x+h) - 2f(x) + f(x-h)] / h²`

---

### Integración Numérica

#### Método del Trapecio
- `I ≈ (b - a) * [f(a) + f(b)] / 2`
- Compuesto: `I ≈ h/2 [f(x0) + 2Σf(xi) + f(xn)]`
- `h = (b - a)/n`

#### Método de Simpson 1/3
- `I ≈ h/3 [f(x0) + 4Σf(x_odd) + 2Σf(x_even) + f(xn)]`

#### Método de Simpson 3/8
- `I ≈ 3h/8 [f(x0) + 3Σf(x_1,2 mod3≠0) + 2Σf(x_3 múltiplos) + f(xn)]`

---

### Extrapolación de Richardson
- `I ≈ I(h/2) + [I(h/2) - I(h)] / (r^p - 1)`
  - `r`: relación entre pasos (ej. 2)
  - `p`: orden del método

---

📘 **Fin de la Hoja Compacta**
