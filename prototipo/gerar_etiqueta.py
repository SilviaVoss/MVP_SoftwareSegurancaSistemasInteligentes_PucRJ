"""
Gera uma etiqueta de preço ARTIFICIAL para testar a segmentação de dígitos.

Por que artificial? Para começar com um caso "perfeito" (sem sombra, sem foto
torta). Se a segmentação não funcionar nem aqui, não vai funcionar em foto real.
"""

# Pillow (PIL) é a biblioteca de imagens do Python.
#   Image     -> representa a imagem em si (a "tela")
#   ImageDraw -> o "pincel" que desenha sobre a imagem
#   ImageFont -> carrega fontes de computador (Arial, etc.)
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# CONSTANTES (configurações em MAIÚSCULAS, no topo do arquivo)
# Boa prática: quem lê entende o significado de cada número, e se precisar
# mudar algo, muda em um lugar só.
# ---------------------------------------------------------------------------

# Tamanho da etiqueta em pixels (largura x altura)
LARGURA, ALTURA = 400, 200

# Cores no formato RGB: (vermelho, verde, azul), cada um de 0 a 255
COR_FUNDO = (255, 220, 60)      # amarelo, típico de etiqueta de mercado
COR_TEXTO = (20, 20, 20)        # quase preto

# Lista de fontes para tentar, em ordem.
#   "arialbd.ttf" -> Arial Bold, existe no Windows (o Pillow acha pelo nome)
#   o caminho longo -> fonte DejaVu Bold, existe no Linux
FONTES_POSSIVEIS = ["arialbd.ttf",
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]


def carregar_fonte(tamanho):
    """Devolve a primeira fonte disponível no sistema, no tamanho pedido."""
    # Percorre a lista de fontes, uma por uma
    for caminho in FONTES_POSSIVEIS:
        try:
            # Tenta carregar a fonte. Se existir, já devolve e a função termina.
            return ImageFont.truetype(caminho, tamanho)
        except OSError:
            # OSError = a fonte não existe neste computador.
            # "continue" pula para a próxima fonte da lista.
            continue
    # Se chegou aqui, nenhuma fonte da lista foi encontrada: avisa com um erro claro.
    raise RuntimeError("Nenhuma fonte encontrada. Ajuste FONTES_POSSIVEIS.")


# ---------------------------------------------------------------------------
# CRIAÇÃO DA ETIQUETA
# ---------------------------------------------------------------------------

# Cria uma imagem nova, colorida ("RGB"), do tamanho definido, toda pintada
# com a cor de fundo
imagem = Image.new("RGB", (LARGURA, ALTURA), COR_FUNDO)

# Cria o "pincel" ligado a essa imagem: tudo que ele desenhar vai para ela
desenho = ImageDraw.Draw(imagem)

# Escreve o texto pequeno (descrição do produto).
#   (20, 15) = posição (x, y) do canto superior esquerdo do texto.
#   Atenção: em imagens, a origem (0, 0) é o canto SUPERIOR esquerdo,
#   e o eixo y cresce PARA BAIXO.
# Colocamos esse texto de propósito: etiquetas reais têm outras coisas escritas,
# e a segmentação precisa saber ignorá-las.
desenho.text((20, 15), "ARROZ 1KG", fill=COR_TEXTO,
             font=carregar_fonte(22))

# Escreve o preço, em fonte grande.
# Usamos vírgula no centavo (padrão brasileiro) para depois tratarmos
# o separador decimal.
desenho.text((40, 70), "$ 12,99", fill=COR_TEXTO,
             font=carregar_fonte(80))

# Salva a imagem como arquivo PNG na pasta atual
imagem.save("etiqueta_exemplo.png")
print("Etiqueta salva em etiqueta_exemplo.png")
