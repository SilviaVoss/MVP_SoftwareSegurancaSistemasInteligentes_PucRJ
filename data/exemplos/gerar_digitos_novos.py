"""
Gera o arquivo digitos_novos.csv: dígitos "nunca vistos" pelo modelo, já no
formato do TMNIST, usados na seção "Simulando a aplicação do modelo em dados
não vistos" do notebook.

Os dígitos são desenhados com a fonte DejaVu Sans, que NÃO faz parte do TMNIST
(o TMNIST usa apenas fontes do Google Fonts).

O notebook não executa este script: ele apenas lê o CSV pronto pela URL do GitHub.
Este arquivo fica no repositório para documentar como os dados foram gerados.
"""
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager

# Dígitos de três etiquetas de preço: 12,99 / 47,50 / 30,86 (cobrem os dígitos de 0 a 9)
PRECOS = ['1299', '4750', '3086']


def criar_imagem_digito(digito, fonte):
    """Desenha um dígito e o converte para o formato do TMNIST (28x28)."""
    # Desenha o dígito em branco sobre fundo preto, em tamanho grande
    imagem = Image.new('L', (150, 150), 0)
    ImageDraw.Draw(imagem).text((20, 0), digito, fill=255, font=fonte)

    # Recorta só a área do dígito e reduz para caber em 20x20 (mantendo a proporção)
    imagem = imagem.crop(imagem.getbbox())
    imagem.thumbnail((20, 20))

    # Centro de massa: o "centro de gravidade" dos pixels claros
    pixels = np.array(imagem, dtype=float)
    linhas, colunas = np.indices(pixels.shape)
    centro_y = (linhas * pixels).sum() / pixels.sum()
    centro_x = (colunas * pixels).sum() / pixels.sum()

    # Cola o dígito numa imagem 28x28 com o centro de massa no meio (14, 14),
    # do mesmo jeito que o TMNIST (e o MNIST) foram construídos
    final = Image.new('L', (28, 28), 0)
    final.paste(imagem, (round(14 - centro_x), round(14 - centro_y)))
    return np.array(final)


fonte = ImageFont.truetype(font_manager.findfont('DejaVu Sans'), 100)
imagens = [criar_imagem_digito(d, fonte) for preco in PRECOS for d in preco]

# Mesmo formato das colunas de pixels do TMNIST: "1" a "784", sem a classe
colunas = [str(i) for i in range(1, 785)]
pd.DataFrame([im.reshape(784) for im in imagens], columns=colunas) \
  .to_csv('digitos_novos.csv', index=False)
print(f"{len(imagens)} dígitos salvos em digitos_novos.csv")
