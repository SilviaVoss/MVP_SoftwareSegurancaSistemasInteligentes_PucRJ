"""Protótipo: separa os dígitos de uma etiqueta de preço."""
import cv2

CAMINHO_IMAGEM = "etiqueta_exemplo.png"

# 1) Carregar a imagem colorida (o OpenCV lê no formato BGR, não RGB)
imagem = cv2.imread(CAMINHO_IMAGEM)

# 2) Converter para tons de cinza: cada pixel vira um único número (0 = preto, 255 = branco)
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# 3) Binarizar: cada pixel vira 0 ou 255.
#    - THRESH_OTSU escolhe sozinho o melhor limite entre "fundo" e "texto"
#    - THRESH_BINARY_INV inverte: texto fica BRANCO e fundo PRETO
limite, binaria = cv2.threshold(cinza, 0, 255,
                                cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
print(f"Limite escolhido pelo Otsu: {limite}")

cv2.imwrite("etapa1_cinza.png", cinza)
cv2.imwrite("etapa2_binaria.png", binaria)

# 4) Encontrar os contornos: cada "mancha" branca conectada vira um contorno.
#    - RETR_EXTERNAL: só o contorno de fora (ignora o "buraco" dentro do 9, do 0...)
#    - CHAIN_APPROX_SIMPLE: guarda só os pontos essenciais do contorno (economiza memória)
contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
print(f"Contornos encontrados: {len(contornos)}")

# 5) Para cada contorno, calcular o retângulo que o envolve (x, y, largura, altura)
#    boundingRect devolve uma tupla; guardamos todas numa lista para filtrar depois
caixas = [cv2.boundingRect(contorno) for contorno in contornos]

# 6) FILTRO 1 - descartar texto pequeno (ex.: "ARROZ 1KG")
#    Regra: o preço é o texto MAIOR da etiqueta. Então mantemos só os contornos
#    com altura de pelo menos 50% da altura do maior contorno.
altura_maxima = max(altura for (x, y, largura, altura) in caixas)
LIMITE_ALTURA = 0.5  # 50% - podemos ajustar depois com fotos reais

mantidas = [c for c in caixas if c[3] >= LIMITE_ALTURA * altura_maxima]
print(f"Altura máxima: {altura_maxima} | mantidos: {len(mantidas)} de {len(caixas)}")

# 7) Visualização: verde = mantido, vermelho = descartado
visualizacao = imagem.copy()
for caixa in caixas:
    x, y, largura, altura = caixa
    cor = (0, 160, 0) if caixa in mantidas else (0, 0, 255)  # BGR
    cv2.rectangle(visualizacao, (x, y), (x + largura, y + altura), cor, 2)

cv2.imwrite("etapa3_contornos.png", visualizacao)
