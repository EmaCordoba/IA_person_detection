from picamera2 import Picamera2
import cv2


# Inicializa la cámara y configura el video para una resolución de 640x480
config = picam2.create_video_configuration(main={"size": (640, 480)})
picam2.configure(config)
picam2.start()

while True:
    # Captura un frame
    frame = picam2.capture_array()

    # Muestra el frame
    cv2.imshow("Cámara", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Detener la cámara
picam2.stop()
cv2.destroyAllWindows()
