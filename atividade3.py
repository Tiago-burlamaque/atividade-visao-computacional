import cv2

img = cv2.imread("image/gato.jpg")

edt = cv2.selectROI('Selecione a area de recorte', img, False) 

v1 = int(edt[0]) # selecionando o quadrado de recorte
v2 = int(edt[1]) # selecionando o quadrado de recorte
v3 = int(edt[2]) # selecionando o quadrado de recorte
v4 = int(edt[3]) # selecionando o quadrado de recorte

recorte = img[v2:v2+v4, v1:v1+v3] # aplicando o recorte

cv2.imshow("Recorte", recorte)
nome_recorte = input("Digite o nome do arquivo para salvar o recorte (sem extensão): ")
cv2.imwrite(f"recorte/{nome_recorte}.jpg", recorte)

cv2.waitKey(0)
cv2.destroyAllWindows()