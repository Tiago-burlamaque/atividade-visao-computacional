import cv2
import os

camera = cv2.VideoCapture(0)

os.makedirs("saida", exist_ok=True)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    altura, largura, _ = frame.shape

    x = largura // 4
    y = altura // 4
    w = largura // 2
    h = altura // 2

    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Recorte Webcam", frame)

    tecla = cv2.waitKey(1)

    if tecla == ord('s'):
        original = frame.copy()

        recorte = original[y:y+h, x:x+w]

        cv2.imwrite("saida/original.jpg", original)
        cv2.imwrite("saida/recorte.jpg", recorte)

        print("Imagem e recorte salvos!")

    if tecla == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()