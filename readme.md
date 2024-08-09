# Reconocimiento Facial y Captura de Fotos

Este proyecto incluye dos componentes principales:

1. **Reconocimiento Facial**: Un script que utiliza la librería `DeepFace` para reconocer caras en tiempo real desde la cámara. Compara las caras detectadas con un conjunto de imágenes conocidas y bloquea la computadora si no se reconoce la cara.

2. **Captura de Fotos**: Un script que captura una serie de fotos desde la cámara y las guarda en una carpeta con un nombre único basado en la marca de tiempo.

## Requisitos

Para ejecutar este proyecto, necesitarás instalar las siguientes dependencias. Puedes hacerlo usando el archivo `requirements.txt`.

### Dependencias

- `deepface`
- `opencv-python`
- `tensorflow`
- `numpy`

## Captura de Fotos - Registro de usuarios

El script para captura de fotos (`registrar_usuario.py`) toma una serie de fotos desde la cámara y las guarda en la carpeta `known_images`.

**Ejecuta el script de captura de fotos:**

```sh
python registrar_usuario.py
```

## Uso

### Reconocimiento Facial

El script para reconocimiento facial (`main.py`) compara la imagen capturada con las imágenes almacenadas en la carpeta `known_images`. Si la cara no se reconoce, la computadora se bloquea.

Asegúrate de tener imágenes conocidas en la carpeta `known_images`.

Ejecuta el script de reconocimiento facial:

```sh
python main.py
```

## Configuración del Intervalo de Tiempo

En el script main.py, puedes configurar el intervalo de tiempo entre cada reconocimiento facial ajustando los valores min_interval y max_interval en la función main.

Ejemplo para configurar el intervalo:

```python
if __name__ == "__main__":
    main(min_interval=10, max_interval=60)
```
