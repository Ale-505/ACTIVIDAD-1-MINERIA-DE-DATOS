import pandas as pd
import numpy as np

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Número de registros
n = 500

# ------------------------------
# 1. Variables demográficas
# ------------------------------
edades = np.random.randint(16, 25, n)
generos = np.random.choice(['Masculino', 'Femenino'], n)
origen = np.random.choice(['Urbano', 'Rural'], n, p=[0.7, 0.3])

# ------------------------------
# 2. Variables académicas
# ------------------------------
# Promedio secundaria (ligeramente mayor con la edad)
promedio_secundaria = np.round(
    np.clip(np.random.normal(3.5 + (edades - 18) * 0.02, 0.4, n), 1.0, 5.0), 2
)

# Resultado admisión (correlación con promedio secundaria)
resultado_admision = np.round(
    np.clip(np.random.normal(250 + promedio_secundaria * 30, 20, n), 150, 400), 0
)

# Promedio primer semestre (depende de secundaria + admisión)
promedio_primer_semestre = np.round(
    np.clip(np.random.normal((promedio_secundaria + (resultado_admision/100))/2, 0.5, n), 0.0, 5.0), 2
)

# ------------------------------
# 3. Variables financieras
# ------------------------------
nivel_socioeco = np.random.choice(['Bajo', 'Medio', 'Alto'], n, p=[0.4, 0.4, 0.2])

# Beca (más probable si es de nivel bajo con buenas notas)
beca = []
for i in range(n):
    if nivel_socioeco[i] == 'Bajo' and promedio_secundaria[i] > 3.8:
        beca.append(np.random.choice(['Sí', 'No'], p=[0.7, 0.3]))
    else:
        beca.append(np.random.choice(['Sí', 'No'], p=[0.3, 0.7]))

# Préstamo (más probable en niveles bajo y medio)
prestamo = []
for i in range(n):
    if nivel_socioeco[i] == 'Bajo':
        prestamo.append(np.random.choice(['Sí', 'No'], p=[0.6, 0.4]))
    elif nivel_socioeco[i] == 'Medio':
        prestamo.append(np.random.choice(['Sí', 'No'], p=[0.4, 0.6]))
    else:
        prestamo.append(np.random.choice(['Sí', 'No'], p=[0.2, 0.8]))

# ------------------------------
# 4. Variable objetivo: Deserción
# ------------------------------
deserta = []
for i in range(n):
    prob = 0.2  # base
    if promedio_primer_semestre[i] < 3.0:
        prob += 0.4
    if nivel_socioeco[i] == 'Bajo':
        prob += 0.2
    if beca[i] == 'No':
        prob += 0.1
    if prestamo[i] == 'Sí':
        prob += 0.1

    deserta.append(np.random.choice(['Sí', 'No'], p=[min(prob, 0.9), 1 - min(prob, 0.9)]))

# ------------------------------
# 5. Construcción del DataFrame
# ------------------------------
df = pd.DataFrame({
    'Edad': edades,
    'Género': generos,
    'Origen': origen,
    'Promedio_Secundaria': promedio_secundaria,
    'Resultado_Admision': resultado_admision,
    'Promedio_Primer_Semestre': promedio_primer_semestre,
    'Nivel_Socioeconómico': nivel_socioeco,
    'Beca': beca,
    'Préstamo': prestamo,
    'Deserta': deserta
})

# ------------------------------
# 6. Introducir nulos y outliers
# ------------------------------
# Nulos en algunas columnas
for col in ['Promedio_Secundaria', 'Resultado_Admision', 'Promedio_Primer_Semestre']:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

# Outliers de edad
df.loc[np.random.choice(df.index, 3, replace=False), 'Edad'] = [50, 60, 70]

# ------------------------------
# 7. Vista previa
# ------------------------------
print(df.head())
print(df.describe(include='all'))


# Guardar en CSV
df.to_csv("dataset_desercion.csv", index=False)

print("Archivo CSV generado: dataset_desercion.csv")
