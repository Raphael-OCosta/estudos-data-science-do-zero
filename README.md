# 🧮 Estudos — *Data Science do Zero* (Joel Grus)

> **A melhor forma de estudar um livro técnico é ler e praticar ao mesmo tempo.**
> Leia uma seção, feche o livro e escreva o código com as próprias mãos. Só depois confira o gabarito.

Este repositório registra meu estudo de *Data Science do Zero*. A proposta do livro é implementar as ferramentas de ciência de dados **do zero**, em Python puro, para entender como funcionam por dentro.
Cada um dos 25 capítulos virou um caderno Jupyter. Cada seção aponta para a página do PDF e, quando cabe, traz um exercício original "do zero".

## 🔁 O método

| Passo | O que fazer | Onde |
|---|---|---|
| 1. Ler | Ler a seção indicada | PDF do livro (página no caderno) |
| 2. Praticar | Escrever a solução do 🧪 exercício **sem olhar a resposta** | `praticar/capXX_*.ipynb` |
| 3. Conferir | Comparar com o gabarito e entender a diferença | `resolvidos/capXX_*.ipynb` |
| 4. Resumir | Explicar com as próprias palavras nas células 📝 | `praticar/` |
| 5. Registrar | Commit + push | GitHub |

## 📚 Conteúdo (55 exercícios, só Python puro + matplotlib)

| Capítulos | O que se implementa do zero |
|---|---|
| 1–4 | rede de amigos e sugestões, compreensões, geradores, gráficos, vetores e matrizes com listas |
| 5–7 | estatística descritiva, correlação e outliers, Simpson, Bayes (doença rara), normal e sua inversa, limite central, testes de hipótese, p-hacking, teste A/B, priori Beta |
| 8–11 | gradiente numérico, gradiente descendente e SGD, CSV, extração de HTML, JSON, limpeza, padronização, PCA por gradiente, treino/teste, métricas |
| 12–18 | KNN com desempate, maldição da dimensionalidade, Naive Bayes de spam, regressão simples, bootstrap, ridge, logística, entropia e escolha de atributo, perceptron e rede neural para XOR com *backpropagation* |
| 19–24 | k-médias e cotovelo, bigramas, gramáticas, PageRank, recomendação por popularidade e por cosseno, SQL com `sqlite3`, MapReduce (contagem e multiplicação de matrizes) |

## 🛠️ Melhorias em relação ao livro

- A edição em português usa **Python 2.7**. Aqui tudo está em **Python 3.12**: f-strings, `math.dist`, `statistics`, `random.choices`, separador de milhar `1_000`.
- Bibliotecas que saíram de uso ou exigem conta (por exemplo, a API do Twitter) foram trocadas por equivalentes da biblioteca padrão: `html.parser`, `json`, `sqlite3`.
- Cada exercício **confere o próprio resultado** (contra o módulo `statistics`, a fórmula fechada ou o valor verdadeiro da simulação).
- O gabarito inteiro é executado por `ferramentas/testar_cadernos.py`.
- O código original do autor (licença MIT) está em [joelgrus/data-science-from-scratch](https://github.com/joelgrus/data-science-from-scratch). A pasta `first-edition/code-python3` corresponde à edição traduzida.

## ▶️ Como usar

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-estudos.txt
.venv\Scripts\python.exe ferramentas\testar_cadernos.py   # opcional: roda o gabarito
```

Abra `praticar/cap01_introducao.ipynb` no VS Code e escolha o kernel `.venv`.
O [Guia de Estudos (PDF)](Guia_de_Estudos.pdf) explica o passo a passo.

## ⚖️ Direitos autorais

O livro **não** está neste repositório. Para estudar, use a sua própria cópia.
Os exercícios, os cadernos, os scripts e o guia são autorais e estão sob licença [MIT](LICENSE).
