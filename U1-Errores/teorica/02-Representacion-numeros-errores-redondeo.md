# Representación de números y errores de redondeo

- Sistemas de numeración posicional: Fijo y flotante
- Número de máquina y rango de máquina
- Redondeo simétrico y corte.
- Unidad de redondeo
- Errores de redondeo en operaciones aritméticas en punto flotante
- Representación de números en la computadora en sistema flotante

## Sistemas de numeración

### Sistema posicional  

El valor depende de la posición absoluta de cada uno de los símbolos que lo contienen
Los caracteriza una base B (por ejemplo 2,10, 16, etc)
Conjunto elementos de la base: 0, 1, ..., B-1

![Sistema posicional](/U1-Errores/imgs/modulo02/sistema-posicional.png)

Ejemplo de representación

- En base **10**

![Ejemplo de Representación en decimal](/U1-Errores/imgs/modulo02/repre-b10.png)

- En base **2**

![Ejemplo de Representación en binario](/U1-Errores/imgs/modulo02/repre-b2.png)

### Punto fijo

![Ejemplo de Representación en sist. Punto Fijo](/U1-Errores/imgs/modulo02/punto-fijo.png)


### Punto flotante

![Ejemplo de Representación en sist. Punto Flotanta](/U1-Errores/imgs/modulo02/punto-flotante.png)


- Punto Flotante Normalizada

n = números para guardar el número
t = para la mantisa 
e = para la parte decimal

![Ejemplo de Representación en sist. Punto Flotanta Normalizada](/U1-Errores/imgs/modulo02/punto-flotante-normalizado.png)

## Número de máqina y rango de máquina

**Números de máquina:** Es el conjunto de números que se pueden representar exactamente.
Esto quedará determinado por los números t y e, junto a la base B.

**Rango de la máquina:** Es el conjunto de números que podamos representar aproximadamente en nuestra máquina

```
Rango = { |x| E R / x E [10<sub>-10<sub>e</sub></sub>,10<sub>10<sub>e</sub>-1</sub> ] }
```

e = la cantidad de lugares 

## Rendondeo simétrico y corte 

![Redondeo Simétrico y corte](/U1-Errores/imgs/modulo02/punto-flotante-normalizado.png)

## Error relativo máximo de representación | Unidad de redondeo

