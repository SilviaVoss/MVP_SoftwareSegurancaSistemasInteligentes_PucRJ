# CLAUDE.md — Contexto do projeto para o Claude Code

## Sobre o projeto
MVP da pós-graduação em Engenharia de Software (PUC-Rio), disciplina de
Engenharia de Sistemas de Software Inteligentes.

**Conversor de preços por foto:** o viajante fotografa a etiqueta de preço,
o sistema reconhece o valor com um modelo de ML e converte para outra moeda.
Inclui um carrinho de compras com total convertido.

## Forma de trabalho (IMPORTANTE)
- Responder sempre em **português**.
- A aluna está aprendendo: construir em **passos pequenos**, explicando cada
  trecho de código antes de seguir. Nada de blocos grandes prontos e herméticos.
- Comentar o código de forma didática.
- Perguntar antes de decisões de arquitetura.

## Stack (decidida)
- Back-end: **Flask** (API REST), que também serve o front-end
- Banco: **SQLite**, com **SQL puro** (a aluna quer exercitar queries: JOIN, SUM, GROUP BY)
- ML: **scikit-learn**, modelo exportado como `api/ml_model/modelo.pkl` (joblib)
- Front-end: HTML, CSS e JavaScript puro
- Testes: **PyTest**
- Ambiente: **venv** + `api/requirements.txt` (sem Docker)
- Sistema da aluna: Windows

## Pipeline de leitura do preço
foto → recorte → segmentação dos dígitos (OpenCV: tons de cinza, binarização
Otsu invertida, contornos) → classificação de cada dígito (modelo ML, 10 classes)
→ montagem do número → conversão de moeda.

O ML é o classificador de dígitos. A segmentação é pré-processamento clássico.

## Requisitos da disciplina (resumo)
- Notebook Colab: carga do dataset **por URL**, holdout, normalização/padronização,
  KNN, Árvore, Naive Bayes e SVM, otimização de hiperparâmetros, cross-validation,
  pipelines, comparação e exportação do modelo. Deve rodar sem erros no Colab.
- App full stack: carrega o modelo no back-end, recebe dados no front, exibe a predição.
- Teste PyTest de desempenho do modelo com métricas e thresholds definidos,
  impedindo a troca por um modelo pior.
- Reflexão sobre Software Seguro (anonimização, não armazenar fotos, .env etc.).
- Vídeo de até 3 minutos.

## Dataset
**TMNIST (Typeface MNIST)**: dígitos impressos 28×28 em ~2.990 fontes,
`TMNIST_Data.csv` (Kaggle). Vai em `data/` e o Colab lê pela URL raw do GitHub.
Descartados: MNIST (manuscrito) e "Printed Digits Dataset" (feito para Sudoku, "0" em branco).

## Escopo do MVP
- Foto pela webcam do PC (simulando celular); upload como plano B.
- Valor reconhecido aparece em campo fixo na tela, **editável** pelo usuário.
- Fora do escopo (só citar): HTTPS no celular, sobreposição em tempo real,
  detecção automática do preço, GraphQL, Docker, MySQL.

## Estrutura
- `data/` dataset · `notebook/` Colab · `database/schema.sql`
- `api/`: `app.py`, `routes/`, `services/` (segmentacao, classificador, cambio),
  `db/` (conexao, consultas), `ml_model/`, `tests/` (dados de holdout, test_modelo, test_rotas)
- `frontend/`: `index.html`, `css/`, `js/` (camera, api, carrinho)
- `prototipo/`: rascunhos de teste (segmentação). Não é código final.

## Repositório
https://github.com/SilviaVoss/conversor-precos-mvp

## Status atual
- Estrutura criada, venv ok, primeiro commit feito.
- Protótipo de segmentação (`prototipo/segmentar.py`): binarização e contornos ok
  numa etiqueta artificial. Próximo passo: **filtrar os contornos** (descartar texto
  pequeno e "$", identificar a vírgula como separador decimal). Decisão pendente:
  descartar o "$" por regra no código ou orientar o usuário a enquadrar só os números.
- Pendências: baixar o TMNIST para `data/`, escolher a API de cotação,
  testar a segmentação com fotos reais.
