#Importando as Bibliotecas
from PIL import Image
import PIL

#adquirindo a imagem no diretório
Imagem_original = Image.open("/content/pasta_exemplo/exemplo.png")

#resolução da imagem
print(Imagem_original.size)

#rotação das imagens
imagem_invertida = Imagem_original.rotate(180)

imagem_esquerda = Imagem_original.transpose(Image.ROTATE_90)

imagem_direita = Imagem_original.transpose(Image.ROTATE_270)

#salvando-as em um Diretório específico
Imagem_original.save("/content/pasta_exemplo2/imagem_rotacionada_or.png")
imagem_invertida.save("/content/pasta_exemplo2/imagem_rotacionada_inv.png") 
imagem_esquerda.save("/content/pasta_exemplo2/imagem_rotacionada_esq.png") 
imagem_direita.save("/content/pasta_exemplo2/imagem_rotacionada_dir.png") 