# 📈 Calculadora de Ahorro Programado

Proyecto académico desarrollado bajo principios de **código limpio**, validaciones robustas y pruebas unitarias.

Esta aplicación permite calcular cuánto se debe ahorrar mensualmente para alcanzar una meta financiera en un plazo determinado, considerando una tasa de interés mensual fija y un posible abono extra en un mes específico.

---

## 🎯 Objetivo

Calcular la **cuota mensual de ahorro** necesaria para alcanzar una meta financiera usando el modelo de valor futuro de una anualidad con interés compuesto.

---

## 📥 Entradas del sistema

El programa solicita los siguientes datos:

| Entrada | Tipo | Descripción |
|----------|--------|--------------|
| `meta` | float | Monto total que se desea alcanzar. |
| `plazo` | int | Número de meses para alcanzar la meta. |
| `extra` | float | Abono adicional realizado en un mes específico (puede ser 0). |
| `mes_extra` | int | Mes en el que se realiza el abono extra. |

### 🔎 Validaciones implementadas

El sistema valida que:

- La meta sea mayor que 0.
- El plazo sea mayor que 0.
- El abono extra no sea negativo.
- El abono extra no supere la meta.
- El mes del abono esté dentro del rango del plazo.

Si alguna condición falla, se lanzan **excepciones personalizadas**.

---

## ⚙️ Proceso

El cálculo se basa en:

- 📌 Interés compuesto mensual fijo: `0.75%`
- 📌 Fórmula de valor futuro de anualidad:

\[
![Fórmula Valor Futuro](assets/images//formula2.svg)
\]

Donde:

- `C` = cuota mensual
- `i` = tasa de interés mensual
- `n` = número de meses

Si existe un abono extra, se calcula su valor futuro:

\[
![Fórmula Valor Futuro](assets/images//fvextra.svg)
\]

Luego se despeja la cuota mensual necesaria:

\[
![Fórmula Valor Futuro](assets/images//cuotamensual.svg)
\]

El resultado se redondea a 2 decimales.

---

## 📤 Salida

El sistema muestra:
