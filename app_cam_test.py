from picamera2 import Picamera2
import cv2

# Inicializa la cámara
picam2 = Picamera2()
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
