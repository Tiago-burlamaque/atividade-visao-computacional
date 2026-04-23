import cv2

img = cv2.imread("image/gato.jpg")

caminho = "saida"
nome_arquivo = input("Digite o nome do arquivo para salvar a imagem (sem extensão): ")
cv2.imwrite(f"{caminho}/{nome_arquivo}.jpg", img)

print("Imagem salva com sucesso!")