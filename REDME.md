# README – Generador de Datos Sintéticos de Deserción Estudiantil

## Descripción del proyecto
Este proyecto implementa un generador de datos sintéticos que simula información de estudiantes de pregrado con el fin de modelar el problema de la deserción estudiantil.

El dataset creado no proviene de estudiantes reales, sino que se construye aplicando un enfoque basado en reglas, donde variables académicas, demográficas y financieras se combinan siguiendo patrones realistas para producir un conjunto de datos que puede ser utilizado en pruebas de Machine Learning supervisado.

## Objetivo
El propósito es contar con un dataset de entrenamiento que represente escenarios plausibles de deserción, permitiendo:
- Desarrollar y entrenar modelos de clasificación binaria.
- Probar diferentes algoritmos (Árboles de Decisión, Regresión Logística, Random Forest).
- Analizar la influencia de factores académicos, socioeconómicos y financieros en la deserción.

## Tecnologías utilizadas
- Python 3.9+
- Librerías principales:
  - numpy – Generación de números aleatorios.
  - pandas – Manipulación y almacenamiento de datos.

## Variables generadas
El generador produce 500 registros con las siguientes variables:

### Demográficas
- Edad: valor entero entre 17 y 30 años, con algunos valores atípicos (50, 60, 70) para simular outliers.
- Género: categórica, Hombre/Mujer.
- Origen: categórica, Urbano/Rural.

### Académicas
- Promedio secundaria: número decimal entre 2.0 y 5.0.
- Resultado de admisión: puntaje simulado entre 0 y 100.
- Promedio primer semestre: número decimal entre 2.0 y 5.0.

### Financieras
- Nivel socioeconómico: Bajo / Medio / Alto.
- Beca: Sí / No.
- Préstamo educativo: Sí / No.

### Variable objetivo
- Deserta: Sí / No (variable binaria a predecir).

## Reglas de generación
El valor de la variable Deserta se determina aplicando reglas que combinan diferentes factores:

1. Si el promedio del primer semestre es menor a 3.0, aumenta el riesgo de deserción.
2. Los estudiantes de nivel socioeconómico bajo tienen mayor probabilidad de desertar.
3. Contar con beca reduce el riesgo de deserción.
4. Tener un préstamo educativo aumenta el riesgo moderado de deserción.

Además:
- Se introducen valores nulos (~5%) para simular datos incompletos.
- Se incluyen outliers en la edad para representar datos atípicos.

## Estructura de salida
El generador produce un archivo `dataset_desercion.csv` con 500 filas y 10 columnas.

Ejemplo (5 primeros registros):

## Uso
1. Clonar el repositorio.
2. Instalar dependencias:
   ```bash
   pip install pandas numpy
