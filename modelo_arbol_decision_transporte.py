# Modelo supervisado para transporte masivo
# Proyecto: prediccion del nivel de congestion en rutas tipo TransMilenio

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# 1. Cargar fuente de datos
# El archivo debe estar en la misma carpeta que este script.
datos = pd.read_csv("dataset_transporte_masivo.csv")

# 2. Separar variables de entrada y variable objetivo
# Se elimina retraso_estimado_min porque nivel_congestion se construyo con base en esa medida
# y se deja el modelo trabajando con variables operativas: pasajeros, buses, clima, incidentes, horario, etc.
X = datos.drop(columns=["id_registro", "nivel_congestion", "recomendacion_operativa", "retraso_estimado_min"])
y = datos["nivel_congestion"]

# 3. Definir columnas categoricas y numericas
columnas_categoricas = ["dia_semana", "franja_horaria", "linea", "estacion_origen", "estacion_destino"]
columnas_numericas = ["pasajeros_estimados", "buses_disponibles", "lluvia", "evento_cercano", "incidente_reportado", "tiempo_base_min"]

# 4. Transformar datos categoricos a variables numericas
preprocesamiento = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), columnas_categoricas),
        ("num", "passthrough", columnas_numericas)
    ]
)

# 5. Crear modelo de arbol de decision
modelo = DecisionTreeClassifier(max_depth=5, random_state=42, criterion="gini")

# 6. Crear pipeline completo
pipeline = Pipeline(steps=[
    ("preprocesamiento", preprocesamiento),
    ("modelo", modelo)
])

# 7. Dividir datos para entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 8. Entrenar el modelo
pipeline.fit(X_entrenamiento, y_entrenamiento)

# 9. Realizar predicciones
predicciones = pipeline.predict(X_prueba)

# 10. Evaluar el modelo
exactitud = accuracy_score(y_prueba, predicciones)
print("Exactitud del modelo:", round(exactitud, 3))
print("\nReporte de clasificacion:")
print(classification_report(y_prueba, predicciones, zero_division=0))
print("\nMatriz de confusion:")
print(confusion_matrix(y_prueba, predicciones, labels=["Baja", "Media", "Alta"]))

# 11. Probar con un caso nuevo
nuevo_caso = pd.DataFrame([{
    "dia_semana": "Viernes",
    "franja_horaria": "Tarde_pico",
    "linea": "Norte",
    "estacion_origen": "Portal Norte",
    "estacion_destino": "Calle 76",
    "pasajeros_estimados": 980,
    "buses_disponibles": 7,
    "lluvia": 1,
    "evento_cercano": 0,
    "incidente_reportado": 1,
    "tiempo_base_min": 44
}])

resultado = pipeline.predict(nuevo_caso)[0]
print("\nPrediccion para caso nuevo:", resultado)

if resultado == "Baja":
    print("Recomendacion: mantener ruta normal.")
elif resultado == "Media":
    print("Recomendacion: aumentar buses y avisar a usuarios.")
else:
    print("Recomendacion: activar ruta alterna y control operativo.")

# 12. Guardar grafica del arbol de decision
nombres_variables = pipeline.named_steps["preprocesamiento"].get_feature_names_out()
plt.figure(figsize=(16, 8))
plot_tree(
    pipeline.named_steps["modelo"],
    feature_names=nombres_variables,
    class_names=pipeline.named_steps["modelo"].classes_,
    rounded=True,
    fontsize=7
)
plt.title("Arbol de decision - Nivel de congestion")
plt.savefig("arbol_decision.png", dpi=150, bbox_inches="tight")
plt.close()
