# Conversor de Preços por Foto — MVP

Ferramenta para viajantes: fotografa a etiqueta de preço, reconhece o valor
com um modelo de machine learning e converte para outra moeda.

> MVP da pós-graduação em Engenharia de Software — PUC-Rio.

## Estrutura

| Pasta        | Conteúdo |
|--------------|----------|
| `data/`      | Dataset TMNIST (dígitos impressos) usado no notebook |
| `notebook/`  | Notebook Colab: treino, avaliação e exportação do modelo |
| `database/`  | `schema.sql` com a criação das tabelas SQLite |
| `api/`       | Back-end Flask (API REST) + modelo embarcado + testes |
| `frontend/`  | Interface web (HTML, CSS, JavaScript) |

## Como executar

```bash
# 1. Criar e ativar o ambiente virtual (Windows)
python -m venv .venv
.venv\Scripts\activate

# 2. Instalar as dependências
pip install -r api/requirements.txt

# 3. Configurar variáveis de ambiente
copy .env.example .env

# 4. Rodar a aplicação
# (instruções serão completadas durante o desenvolvimento)
```

## Como rodar os testes

```bash
pytest api/tests
```

## Como regenerar o modelo

_(a completar: executar o notebook no Colab, baixar `modelo.pkl` e a amostra
de teste, e copiá-los para `api/ml_model/` e `api/tests/dados/`)_
