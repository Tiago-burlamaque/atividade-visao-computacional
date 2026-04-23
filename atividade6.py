import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Webcam Ao Vivo", frame)

    tecla = cv2.waitKey(1)

    if tecla == ord('q'):
        break

    if tecla == ord('s'):
        cv2.imwrite("frame_salvo.jpg", frame)
        print("Frame salvo!")

camera.release()
cv2.destroyAllWindows()