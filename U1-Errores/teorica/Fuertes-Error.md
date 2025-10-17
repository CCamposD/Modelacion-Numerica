# Errores en el cálculo numérico

## Fuentes de error y su propagación

![Ejemplo de Montaña](/U1-Errores/imgs/ejemplo-mountain.png)


**Problema:** Deseamos calcular la altura de una montaña d(B,C)
**Datos:** Distancia d(A,B), ángulo α en grados sexagesimales

**Instrumentos de cáculo:** Calculadora sin funciones matemáticas, lápiz y papel.

Podemos definir nuestro **Problema Matemático** de las siguiente forma:

```
d(B,C) = d(A,B)tan(α*π/180)
```

### Error de truncamiento

Son los que se producen al pasar el problema.

Problema Matemático -> Problema Νumérico

---

> Ahora debemos elegir un algortimo para resolver el problema numérico

---
### Errores Inherentes

Son los errores que afectan a los datos de entrada del problema numérico

d(A,B) α: Valores exactos ----------> d(A,B): es el valor medido

π ----------> π: algunos decimales de π

### Εrrores de redondeo 

Se producen por la limitación en la representación de los valores

Las operaciones se realizan utilizando solo una cantidad finita de dígitos (uso de la calculadora)

## Propagación de errores

| Caso | Error Inherente | Error de Redondeo | Error de Discretización | Error Final |
|:----:|:----------------:|:-----------------:|:------------------------:|:-------------|
| I   | Nulo      | Nulo      | Nulo      | Nulo |
| II  | No Nulo   | Nulo      | Nulo      | Depende solo del P.N |
| III | Nulo      | No Nulo   | Nulo      | Depende del P.N y del algoritmo |
| IV  | Nulo      | Nulo      | No Nulo   | Error de discretización (P.M ≠ P.N) |

## Reglas para expresar los resultados numéricos

### Error absoluto y relativo

- Error absoluto de x
```
e<sub>x</sub> = x - X<sup>-</sup> 
```

El valor verdadero - el valor medido 
Puede ser negativo o positivo

El error absoluto / el valor medido

Esto nos da una ídea de la calidad de la medición

![Errores](/U1-Errores/imgs/error.png)


### Cota del error absoluto y relativo

Siempre es positivo, por lo general conocemos o deberiamos conocer

![Cotas](/U1-Errores/imgs/cota.png)

### Dos maneras de expresar el resultado numérico

![Formas de expresar](/U1-Errores/imgs/formas-expresar.png)


1) Valor medido +- la cota 

Ejemplos para escribir el resultado.

![Ejemplo para escribir el resultado](/U1-Errores/imgs/ejemplo-escribir-resultado.png)



