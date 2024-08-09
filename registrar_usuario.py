import cv2
import os
import time

def capture_photos(output_folder, num_photos=5):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Inicializar la captura de video
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("No se pudo acceder a la cámara.")
        return

    print(f"Iniciando la captura de {num_photos} fotos...")

    for i in range(num_photos):
        # Captura un fotograma del video
        ret, frame = video_capture.read()
        if not ret:
            print("No se pudo acceder al fotograma.")
            break

        # Crear un ID único basado en la marca de tiempo actual
        timestamp = int(time.time())
        photo_path = os.path.join(output_folder, f"photo_{timestamp}.jpg")

        # Guardar el fotograma en un archivo
        cv2.imwrite(photo_path, frame)
        print(f"Foto {i+1} guardada como {photo_path}")

        # Mostrar el fotograma en una ventana
        cv2.imshow('Captura de foto', frame)
        # Esperar 5 segundo entre capturas para facilitar la captura
        cv2.waitKey(5000)

    # Liberar la captura de video y cerrar las ventanas
    video_capture.release()
    cv2.destroyAllWindows()
    print("Captura de fotos completada.")

if __name__ == "__main__":
    output_folder = "known_images"  # Carpeta para guardar las fotos
    capture_photos(output_folder, num_photos=5)
