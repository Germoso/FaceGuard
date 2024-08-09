from deepface import DeepFace
import cv2
import ctypes
import time
import os
import random

def lock_windows():
    ctypes.windll.user32.LockWorkStation()

def load_known_images(known_images_folder):
    known_images = []
    for file_name in os.listdir(known_images_folder):
        file_path = os.path.join(known_images_folder, file_name)
        if os.path.isfile(file_path):
            try:
                # Cargar la representación de la imagen conocida
                image_representation = DeepFace.represent(img_path=file_path, model_name='VGG-Face', enforce_detection=False)
                known_images.append((file_path, image_representation))
            except Exception as e:
                print(f"Error al cargar la imagen {file_name}: {e}")
    return known_images

def recognize_face(known_images_folder):
    known_images = load_known_images(known_images_folder)
    
    if not known_images:
        print("No se encontraron imágenes conocidas.")
        return

    # Captura de video desde la cámara
    video_capture = cv2.VideoCapture(0)

    # Captura un fotograma del video
    ret, frame = video_capture.read()
    if not ret:
        print("No se pudo acceder a la cámara.")
        video_capture.release()
        cv2.destroyAllWindows()
        return

    # Guardar el fotograma capturado en un archivo temporal
    temp_image_path = "temp_frame.jpg"
    cv2.imwrite(temp_image_path, frame)

    # Intentar reconocer la cara en el fotograma
    try:
        verified = False
        for known_image_path, known_image_representation in known_images:
            # Verificar contra cada representación de imagen conocida
            result = DeepFace.verify(img1_path=temp_image_path, img2_path=known_image_path, model_name='VGG-Face', enforce_detection=False)
            print(result)
            if result['verified']:
                print("¡Rostro reconocido!")
                verified = True
                break
        
        if not verified:
            lock_windows()
            print("Rostro no reconocido.")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

    # Liberar la captura de video y cerrar las ventanas
    video_capture.release()
    cv2.destroyAllWindows()

def main(min_interval, max_interval):
    known_images_folder = "known_images"

    # Crear carpeta para guardar imágenes si no existe
    if not os.path.exists(known_images_folder):
        os.makedirs(known_images_folder)

    while True:
        print("Iniciando reconocimiento facial...")
        recognize_face(known_images_folder)
        
        # Generar un intervalo aleatorio entre min_interval y max_interval
        interval = random.randint(min_interval, max_interval)
        print(f"Esperando {interval} segundos antes del próximo reconocimiento...")
        time.sleep(interval)

# Ejecutar la función principal con un intervalo en segundos
if __name__ == "__main__":
    main(min_interval=60, max_interval=120)
