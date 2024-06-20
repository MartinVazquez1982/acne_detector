
# Detección de Acné

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un sistema automatizado para la detección de acné en imágenes faciales utilizando técnicas de procesamiento digital de imágenes. Emplea Python junto con la biblioteca OpenCV para implementar un flujo de trabajo que abarca desde la captura y preprocesamiento de imágenes hasta la segmentación, medición de características y clasificación de lesiones de acné.

## Contenido del Repositorio

- **Código fuente**: Contiene los scripts en Python para cada etapa del procesamiento de imágenes.
- **Dataset**: Se utilizaron datasets preexistentes de imágenes faciales con anotaciones de acné para entrenar y evaluar el modelo.
- **Informes y Documentación**: Incluye el informe completo del proyecto, describiendo los métodos y resultados obtenidos.

## Requisitos

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/MartinVazquez1982/acne_detector
   cd acne_detector
   ```
   
## Uso

Para ejecutar el sistema de detección de acné, utiliza el siguiente comando:
```bash
python acne_detector.py --input <ruta_a_la_imagen>
```

## Flujo de Trabajo

1. **Captura de Imágenes**: Utilización de un dataset preexistente de imágenes faciales.
2. **Preprocesamiento**: Conversión a escala de grises, aplicación del detector de bordes de Canny y dilatación de bordes.
3. **Segmentación**: Detección de contornos en la imagen preprocesada.
4. **Medición de Características**: Cálculo del tamaño y color de las regiones de interés.
5. **Clasificación**: Identificación de regiones con acné basado en reglas predefinidas.
6. **Postprocesamiento**: Mejora y refinamiento de los resultados.

## Resultados

Los resultados del sistema se evaluaron con un conjunto de pruebas de 39 imágenes, obteniendo las siguientes métricas:

- **Precisión**: 60.4%
- **Sensibilidad**: 77.5%
- **F1-Score**: 67.92%

Estos resultados indican un rendimiento aceptable del modelo, con margen para mejorar en la reducción de falsos positivos.

## Contribuciones

Las contribuciones son bienvenidas. Para contribuir, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature-nueva-caracteristica`).
5. Abre un Pull Request.


## Contacto

Para más información, puedes contactar a los autores:

- Ignacio Ezequiel Gorriti: [igorriti@alumnos.exa.unicen.edu.ar](mailto:igorriti@alumnos.exa.unicen.edu.ar)
- Martin Vazquez Arispe: [martin.vazquez.arispe@gmail.com](mailto:martin.vazquez.arispe@gmail.com)
