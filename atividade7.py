import cv2
import os

camera = cv2.VideoCapture(0)

os.makedirs("saida", exist_ok=True)

contador = 1

while True:
    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Tirar Foto", frame)

    tecla = cv2.waitKey(1)

    if tecla == ord('s'):
        nome = f"saida/foto_{contador}.jpg"
        cv2.imwrite(nome, frame)
        print(f"{nome} salva!")
        contador += 1

    if tecla == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()