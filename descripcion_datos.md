# Descripcion de los datos

El dataset se construyo como una muestra de datos operativos para un sistema de transporte masivo colombiano tipo TransMilenio. La idea es continuar el proyecto anterior, en el que se buscaba la mejor ruta entre estaciones usando una base de conocimiento y el algoritmo de Dijkstra.

Para esta actividad se usa aprendizaje supervisado. La variable que se desea predecir es `nivel_congestion`, con tres posibles clases: Baja, Media y Alta.

## Fuente de datos

Como no se cuenta con una base real entregada por la empresa de transporte, se desarrollo un dataset de muestra llamado `dataset_transporte_masivo.csv`. Este archivo simula registros historicos de operacion por ruta, horario y condiciones externas.

## Variables principales

- `dia_semana`: dia del viaje.
- `franja_horaria`: momento del dia, por ejemplo manana pico o tarde pico.
- `linea`: linea o zona principal de operacion.
- `estacion_origen`: estacion inicial del trayecto.
- `estacion_destino`: estacion final del trayecto.
- `pasajeros_estimados`: cantidad aproximada de pasajeros para la ruta.
- `buses_disponibles`: buses disponibles para atender la demanda.
- `lluvia`: indica si habia lluvia, 1 si habia y 0 si no.
- `evento_cercano`: indica si habia evento cercano que pudiera aumentar la demanda.
- `incidente_reportado`: indica si se reporto un incidente en la operacion.
- `tiempo_base_min`: tiempo normal estimado del recorrido.
- `retraso_estimado_min`: retraso aproximado observado o calculado.
- `nivel_congestion`: variable objetivo que el modelo aprende a clasificar.
- `recomendacion_operativa`: recomendacion asociada al nivel de congestion.

## Uso dentro del modelo

El modelo usa como entradas las variables relacionadas con horario, estacion, pasajeros, buses, clima, eventos e incidentes. La salida es el nivel de congestion. Esta prediccion puede ayudar a tomar decisiones como mantener la ruta normal, aumentar buses o activar una ruta alterna.
