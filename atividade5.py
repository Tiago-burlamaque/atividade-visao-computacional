import cv2

video = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        print("Vídeo finalizado.")
        break

    cv2.imshow("Reproduzindo Vídeo", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()