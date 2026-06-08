# Pruebas realizadas al componente desarrollado

## Objetivo de las pruebas

Verificar si el modelo de aprendizaje supervisado puede clasificar correctamente el nivel de congestion de una ruta de transporte masivo.

## Prueba 1: carga del dataset

Se cargo el archivo `dataset_transporte_masivo.csv` con la libreria pandas. El archivo contiene 180 registros y 15 columnas.

Resultado: la carga fue exitosa y no se presentaron errores de lectura.

## Prueba 2: division de datos

Los datos se dividieron en dos partes:

- 75% para entrenamiento.
- 25% para prueba.

Resultado: el proceso permitio evaluar el modelo con datos que no fueron usados durante el entrenamiento.

## Prueba 3: entrenamiento del arbol de decision

Se entreno un modelo `DecisionTreeClassifier` con profundidad maxima de 5. Antes del entrenamiento se transformaron las variables categoricas con `OneHotEncoder`.

Resultado: el modelo aprendio reglas relacionadas con pasajeros, buses disponibles, lluvia, incidentes y franja horaria.

## Prueba 4: evaluacion del modelo

Exactitud obtenida: 75.56%

Reporte de clasificacion:

```
              precision    recall  f1-score   support

        Alta       0.62      0.56      0.59         9
        Baja       0.95      0.86      0.90        22
       Media       0.59      0.71      0.65        14

    accuracy                           0.76        45
   macro avg       0.72      0.71      0.71        45
weighted avg       0.77      0.76      0.76        45

```

Matriz de confusion, usando el orden Baja, Media y Alta:

```
[[19  3  0]
 [ 1 10  3]
 [ 0  4  5]]
```

## Prueba 5: caso nuevo

Se ingreso un caso de prueba con las siguientes condiciones:

- Viernes en franja de tarde pico.
- Linea Norte.
- Origen Portal Norte y destino Calle 76.
- 980 pasajeros estimados.
- 7 buses disponibles.
- Lluvia activa.
- Incidente reportado.

Resultado esperado: congestion alta, porque combina alta demanda, pocos buses, lluvia e incidente.

Resultado del modelo: Alta.

## Conclusion de las pruebas

El componente funciona correctamente como prototipo academico. El modelo logra clasificar el nivel de congestion y permite generar una recomendacion operativa para apoyar la toma de decisiones en un sistema de transporte masivo.
