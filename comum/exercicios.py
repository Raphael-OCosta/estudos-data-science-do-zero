"""Exercícios práticos criados para estudar o livro, um ou mais por seção.

Formato: (capítulo, início do título da seção, nome, enunciado em Markdown, solução em Python).
No espírito do livro, tudo é feito "do zero": só Python puro (math, random, collections) e matplotlib.
Os exemplos são originais (não copiados do livro) e usam Python 3.12.
"""

EXERCICIOS = [
    # ---------------- 1. Introdução ----------------
    (1, "Motivação Hipotética", "Quem tem mais amigos?",
     "Com a lista de amizades `[(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]`, "
     "monte um dicionário `amigos[id] = [ids]`, calcule o número médio de amigos e mostre os 3 usuários mais conectados.",
     '''amizades = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
amigos = defaultdict(list)
for a, b in amizades:
    amigos[a].append(b); amigos[b].append(a)
print("média:", sum(len(v) for v in amigos.values()) / len(amigos))
print(sorted(amigos, key=lambda u: len(amigos[u]), reverse=True)[:3])'''),
    (1, "Motivação Hipotética", "Amigos de amigos",
     "Escreva `sugestoes(u)`: os amigos dos amigos de `u` que ainda não são amigos dele (nem ele mesmo), com quantos "
     "amigos em comum cada um tem (`Counter`). Teste com o usuário 3.",
     '''amizades = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
amigos = defaultdict(set)
for a, b in amizades:
    amigos[a].add(b); amigos[b].add(a)
def sugestoes(u):
    return Counter(ff for f in amigos[u] for ff in amigos[f] if ff != u and ff not in amigos[u])
print(sugestoes(3))'''),

    # ---------------- 2. Python ----------------
    (2, "O Básico", "Compreensões e funções",
     "Com uma *list comprehension*, gere os quadrados dos pares de 0 a 20. Com uma *dict comprehension*, mapeie cada "
     "palavra de `\"o rato roeu a roupa do rei de roma\"` para o seu tamanho. Escreva `dobra(f)` que devolve uma "
     "função que aplica `f` duas vezes.",
     '''print([x * x for x in range(21) if x % 2 == 0])
print({p: len(p) for p in "o rato roeu a roupa do rei de roma".split()})
def dobra(f):
    return lambda x: f(f(x))
print(dobra(lambda x: x + 3)(10))'''),
    (2, "Não Tão Básico", "Geradores, zip e *args",
     "Escreva um gerador `fib()` infinito e pegue os 10 primeiros valores com `itertools.islice`. Use `zip` para "
     "\"descompactar\" `[(\"a\", 1), (\"b\", 2), (\"c\", 3)]`. Escreva `soma_tudo(*args, **kwargs)` que soma todos "
     "os números recebidos.",
     '''from itertools import islice
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
print(list(islice(fib(), 10)))
letras, numeros = zip(*[("a", 1), ("b", 2), ("c", 3)])
print(letras, numeros)
def soma_tudo(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
print(soma_tudo(1, 2, 3, x=10, y=20))'''),

    # ---------------- 3. Visualizando dados ----------------
    (3, "Gráficos de Barra", "Histograma do zero",
     "Gere 500 notas com `random.gauss(70, 12)`, limitadas entre 0 e 100. Agrupe em faixas de 10 pontos com "
     "`Counter` (sem usar `plt.hist`) e desenhe com `plt.bar`.",
     '''notas = [min(100, max(0, random.gauss(70, 12))) for _ in range(500)]
faixas = Counter(min(int(n // 10) * 10, 90) for n in notas)
plt.bar(list(faixas), list(faixas.values()), width=8, edgecolor="black")
plt.xticks(range(0, 100, 10)); plt.xlabel("faixa de nota"); plt.ylabel("alunos"); plt.show()'''),
    (3, "Gráficos de Linhas", "Viés × variância em linhas",
     "Desenhe três curvas para complexidades de 1 a 10: viés² = 2⁻ᶜ·256 (cai), variância = 2ᶜ (sobe) e o erro total "
     "(a soma). Use legenda.",
     '''c = list(range(1, 11))
vies = [256 / 2**k for k in c]; var = [2**k for k in c]; total = [a + b for a, b in zip(vies, var)]
for y, rot in [(vies, "viés²"), (var, "variância"), (total, "erro total")]:
    plt.plot(c, y, marker="o", label=rot)
plt.legend(); plt.xlabel("complexidade"); plt.show()'''),
    (3, "Gráficos de Dispersão", "Dispersão com rótulos",
     "Gere 10 pessoas com minutos por dia no site e número de amigos (amigos ≈ minutos/10 + ruído) e faça um "
     "gráfico de dispersão escrevendo o nome de cada uma ao lado do ponto (`plt.annotate`).",
     '''nomes = list("ABCDEFGHIJ")
minutos = [random.randint(20, 200) for _ in nomes]
amigos = [m / 10 + random.gauss(0, 2) for m in minutos]
plt.scatter(minutos, amigos)
for n, x, y in zip(nomes, minutos, amigos):
    plt.annotate(n, (x, y), xytext=(5, -5), textcoords="offset points")
plt.xlabel("minutos por dia"); plt.ylabel("amigos"); plt.show()'''),

    # ---------------- 4. Álgebra linear ----------------
    (4, "Vetores", "Vetores com listas",
     "Sem NumPy, escreva `soma_vetores(v, w)`, `escalar(c, v)`, `produto_escalar(v, w)`, `norma(v)` e "
     "`distancia(v, w)`. Teste com `[1, 2, 3]` e `[4, 5, 6]`.",
     '''def soma_vetores(v, w): return [a + b for a, b in zip(v, w)]
def escalar(c, v): return [c * a for a in v]
def produto_escalar(v, w): return sum(a * b for a, b in zip(v, w))
def norma(v): return math.sqrt(produto_escalar(v, v))
def distancia(v, w): return norma(soma_vetores(v, escalar(-1, w)))
v, w = [1, 2, 3], [4, 5, 6]
print(soma_vetores(v, w), escalar(2, v), produto_escalar(v, w), round(norma(v), 3), round(distancia(v, w), 3))'''),
    (4, "Matrizes", "Matrizes como listas de listas",
     "Escreva `forma(A)`, `transposta(A)`, `multiplica(A, B)` e `identidade(n)` só com listas. Confira que "
     "`multiplica(A, identidade(3)) == A` para uma matriz 2×3.",
     '''def forma(A): return len(A), len(A[0]) if A else 0
def transposta(A): return [list(col) for col in zip(*A)]
def multiplica(A, B):
    Bt = transposta(B)
    return [[sum(a * b for a, b in zip(linha, col)) for col in Bt] for linha in A]
def identidade(n): return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
A = [[1, 2, 3], [4, 5, 6]]
print(forma(A), transposta(A), multiplica(A, identidade(3)) == A)'''),

    # ---------------- 5. Estatística ----------------
    (5, "Descrevendo um Conjunto", "Estatísticas descritivas do zero",
     "Escreva `media`, `mediana`, `quantil(xs, p)`, `moda`, `amplitude`, `variancia` (amostral) e `desvio_padrao`. "
     "Teste com `[1, 3, 3, 6, 7, 8, 9, 15, 3, 50]` e compare com o módulo `statistics`.",
     '''import statistics as st
def media(xs): return sum(xs) / len(xs)
def mediana(xs):
    s = sorted(xs); n = len(s); m = n // 2
    return s[m] if n % 2 else (s[m - 1] + s[m]) / 2
def quantil(xs, p): return sorted(xs)[int(p * len(xs))]
def moda(xs):
    c = Counter(xs); mx = max(c.values())
    return [x for x, k in c.items() if k == mx]
def amplitude(xs): return max(xs) - min(xs)
def variancia(xs):
    m = media(xs); return sum((x - m) ** 2 for x in xs) / (len(xs) - 1)
def desvio_padrao(xs): return math.sqrt(variancia(xs))
xs = [1, 3, 3, 6, 7, 8, 9, 15, 3, 50]
print(media(xs), mediana(xs), quantil(xs, 0.75), moda(xs), amplitude(xs), round(desvio_padrao(xs), 3))
print(st.mean(xs), st.median(xs), st.multimode(xs), round(st.stdev(xs), 3))'''),
    (5, "Correlação", "Correlação e um ponto fora da curva",
     "Escreva `covariancia(x, y)` e `correlacao(x, y)`. Gere 50 pares com y = 2x + ruído, calcule a correlação e "
     "depois acrescente um único ponto extremo (x = 0, y = 500). Quanto a correlação muda?",
     '''def media(xs): return sum(xs) / len(xs)
def covariancia(x, y):
    mx, my = media(x), media(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (len(x) - 1)
def correlacao(x, y):
    return covariancia(x, y) / math.sqrt(covariancia(x, x) * covariancia(y, y))
x = [random.uniform(0, 10) for _ in range(50)]; y = [2 * a + random.gauss(0, 2) for a in x]
print(round(correlacao(x, y), 3), round(correlacao(x + [0], y + [500]), 3))'''),
    (5, "Paradoxo de Simpson", "Paradoxo de Simpson com números",
     "Duas clínicas tratam casos leves e graves. Clínica A: leves 90/100 curados, graves 30/100. Clínica B: leves "
     "170/200, graves 3/20. Calcule a taxa de cura por gravidade e no total. Qual clínica parece melhor em cada caso?",
     '''dados = {"A": {"leve": (90, 100), "grave": (30, 100)}, "B": {"leve": (170, 200), "grave": (3, 20)}}
for clinica, g in dados.items():
    cur = sum(c for c, _ in g.values()); tot = sum(t for _, t in g.values())
    print(clinica, {k: round(c / t, 2) for k, (c, t) in g.items()}, "total:", round(cur / tot, 2))
# A ganha em cada gravidade, mas B ganha no total: B atende muito mais casos leves'''),

    # ---------------- 6. Probabilidade ----------------
    (6, "Probabilidade Condicional", "Duas crianças",
     "Simule 100.000 famílias com 2 filhos (menino/menina com 50%). Estime P(as duas são meninas | a mais velha é "
     "menina) e P(as duas são meninas | pelo menos uma é menina).",
     '''fam = [(random.choice("MF"), random.choice("MF")) for _ in range(100_000)]
ambas = sum(1 for v, n in fam if v == n == "F")
velha = sum(1 for v, _ in fam if v == "F")
alguma = sum(1 for v, n in fam if "F" in (v, n))
print(round(ambas / velha, 3), round(ambas / alguma, 3))  # ~1/2 e ~1/3'''),
    (6, "Teorema de Bayes", "Teste de doença rara",
     "Uma doença atinge 1 em 10.000 pessoas. O teste acerta 99% dos doentes e dá falso positivo em 1% dos saudáveis. "
     "Calcule P(doente | positivo) pela fórmula de Bayes e confira com uma simulação de 2 milhões de pessoas.",
     '''p_d, sens, fp = 1 / 10_000, 0.99, 0.01
bayes = sens * p_d / (sens * p_d + fp * (1 - p_d))
pos = doentes_pos = 0
for _ in range(2_000_000):
    d = random.random() < p_d
    if random.random() < (sens if d else fp):
        pos += 1; doentes_pos += d
print(round(bayes, 4), round(doentes_pos / pos, 4))'''),
    (6, "A Distribuição Normal", "Normal: densidade, acumulada e inversa",
     "Escreva `normal_pdf(x, mu, sigma)`, `normal_cdf` (use `math.erf`) e `inversa_normal_cdf(p)` por busca binária. "
     "Confira que `inversa_normal_cdf(0.975)` ≈ 1,96.",
     '''def normal_pdf(x, mu=0, sigma=1):
    return math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2
def inversa_normal_cdf(p, mu=0, sigma=1, tol=1e-6):
    lo, hi = -10.0, 10.0
    while hi - lo > tol:
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if normal_cdf(mid) < p else (lo, mid)
    return mu + sigma * (lo + hi) / 2
print(round(normal_pdf(0), 4), round(normal_cdf(1.96), 4), round(inversa_normal_cdf(0.975), 3))'''),
    (6, "O Teorema do Limite Central", "Limite central com dados viciados",
     "Some 30 lançamentos de um dado viciado (6 sai com 50%, os demais 10% cada) e repita 10.000 vezes. Desenhe o "
     "histograma das somas: parece normal?",
     '''pesos = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
somas = [sum(random.choices(range(1, 7), pesos, k=30)) for _ in range(10_000)]
plt.hist(somas, bins=40, edgecolor="black"); plt.title("Soma de 30 dados viciados"); plt.show()'''),

    # ---------------- 7. Hipótese e inferência ----------------
    (7, "Exemplo: Lançar Uma Moeda", "A moeda é honesta?",
     "Uma moeda deu 560 caras em 1.000 lançamentos. Use a aproximação normal (μ = np, σ = √(np(1−p))) para calcular "
     "o p-valor bicaudal de H₀: p = 0,5.",
     '''def normal_cdf(x, mu=0, sigma=1): return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2
n, caras, p = 1000, 560, 0.5
mu, sigma = n * p, math.sqrt(n * p * (1 - p))
p_valor = 2 * (1 - normal_cdf(caras - 0.5, mu, sigma))
print(round(p_valor, 5))  # bem menor que 0,05: rejeitamos H0'''),
    (7, "P-Hacking", "P-hacking por simulação",
     "Faça 1.000 \"experimentos\" com uma moeda honesta (1.000 lançamentos cada) e conte em quantos o p-valor ficou "
     "abaixo de 5%. O que isso mostra sobre testar muitas hipóteses?",
     '''def normal_cdf(x, mu=0, sigma=1): return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2
def p_valor(caras, n=1000):
    mu, s = n / 2, math.sqrt(n) / 2
    return 2 * (1 - normal_cdf(abs(caras - mu), 0, s))
falsos = sum(p_valor(sum(random.random() < 0.5 for _ in range(1000))) < 0.05 for _ in range(1000))
print(falsos)  # ~50: 5% de "descobertas" mesmo sem efeito nenhum'''),
    (7, "Exemplo: Executando um Teste A/B", "Teste A/B de anúncios",
     "O anúncio A teve 200 cliques em 1.000 visualizações; o B teve 150 em 1.000. Calcule a estatística z da "
     "diferença de proporções e o p-valor.",
     '''def normal_cdf(x): return (1 + math.erf(x / math.sqrt(2))) / 2
def params(n, k): p = k / n; return p, math.sqrt(p * (1 - p) / n)
pa, sa = params(1000, 200); pb, sb = params(1000, 150)
z = (pb - pa) / math.sqrt(sa ** 2 + sb ** 2)
print(round(z, 3), round(2 * (1 - normal_cdf(abs(z))), 4))'''),
    (7, "Inferência Bayesiana", "Priori Beta para a moeda",
     "Com priori Beta(α, β) e k caras em n lançamentos, a posteriori é Beta(α + k, β + n − k). Para 10 caras em 20 "
     "lançamentos, calcule a média da posteriori com as prioris Beta(1, 1), Beta(20, 20) e Beta(30, 10).",
     '''k, n = 10, 20
for a, b in [(1, 1), (20, 20), (30, 10)]:
    a2, b2 = a + k, b + n - k
    print(f"priori Beta({a},{b}) -> posteriori Beta({a2},{b2}), média = {a2 / (a2 + b2):.3f}")'''),

    # ---------------- 8. Gradiente descendente ----------------
    (8, "Estimando o Gradiente", "Gradiente numérico × exato",
     "Para f(x, y) = x² + 3y², calcule o gradiente por diferenças finitas (h = 1e-5) no ponto (2, −1) e compare "
     "com o exato (2x, 6y).",
     '''def f(v): x, y = v; return x ** 2 + 3 * y ** 2
def grad_estimado(f, v, h=1e-5):
    return [(f([vj + (h if j == i else 0) for j, vj in enumerate(v)]) - f(v)) / h for i in range(len(v))]
print([round(g, 3) for g in grad_estimado(f, [2, -1])], [2 * 2, 6 * -1])'''),
    (8, "Juntando Tudo", "Descendo até o mínimo",
     "Minimize f(x, y) = (x − 3)² + (y + 2)² com gradiente descendente a partir de um ponto aleatório, passo 0,1, "
     "até o passo ficar menor que 1e-8. Onde você chegou e em quantas iterações?",
     '''v = [random.uniform(-10, 10), random.uniform(-10, 10)]
for it in range(10_000):
    g = [2 * (v[0] - 3), 2 * (v[1] + 2)]
    novo = [vi - 0.1 * gi for vi, gi in zip(v, g)]
    if math.dist(novo, v) < 1e-8: break
    v = novo
print([round(x, 4) for x in v], it)'''),
    (8, "Gradiente Descendente Estocástico", "SGD para ajustar uma reta",
     "Gere 100 pontos com y = 4x − 7 + ruído (x de −5 a 5). Ajuste a reta y = ax + b com gradiente descendente "
     "estocástico (um ponto por vez, passo 0,001, 1.000 épocas, ordem embaralhada).",
     '''dados = [(x, 4 * x - 7 + random.gauss(0, 1)) for x in [random.uniform(-5, 5) for _ in range(100)]]
a, b = random.random(), random.random()
for epoca in range(1000):
    random.shuffle(dados)
    for x, y in dados:
        erro = (a * x + b) - y
        a -= 0.001 * 2 * erro * x
        b -= 0.001 * 2 * erro
print(round(a, 2), round(b, 2))'''),

    # ---------------- 9. Obtendo dados ----------------
    (9, "Lendo Arquivos", "CSV com o módulo csv",
     "Escreva um CSV temporário com preços de ações (data, ação, fechamento) e leia com `csv.DictReader`, guardando "
     "o maior fechamento de cada ação.",
     '''import csv, tempfile, os
linhas = [("2024-01-02", "AAA", 10.5), ("2024-01-02", "BBB", 22.0), ("2024-01-03", "AAA", 11.2), ("2024-01-03", "BBB", 21.1)]
with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="") as f:
    w = csv.writer(f); w.writerow(["data", "acao", "fechamento"]); w.writerows(linhas); nome = f.name
maior = defaultdict(float)
with open(nome, newline="") as f:
    for r in csv.DictReader(f):
        maior[r["acao"]] = max(maior[r["acao"]], float(r["fechamento"]))
os.remove(nome); print(dict(maior))'''),
    (9, "Extraindo Dados da Internet", "Extraindo dados de HTML",
     "Sem bibliotecas externas, use `html.parser.HTMLParser` para extrair todos os links (`href`) e o texto dos "
     "`<h2>` de um HTML de exemplo escrito por você.",
     '''from html.parser import HTMLParser
html = "<h2>Livros</h2><a href='/a'>A</a><p>texto</p><h2>Cursos</h2><a href='/b'>B</a>"
class Extrator(HTMLParser):
    def __init__(self):
        super().__init__(); self.links, self.titulos, self._em_h2 = [], [], False
    def handle_starttag(self, tag, attrs):
        if tag == "a": self.links.append(dict(attrs).get("href"))
        self._em_h2 = tag == "h2"
    def handle_data(self, data):
        if self._em_h2: self.titulos.append(data)
    def handle_endtag(self, tag):
        if tag == "h2": self._em_h2 = False
e = Extrator(); e.feed(html); print(e.links, e.titulos)'''),
    (9, "Usando APIs", "JSON de uma API",
     "Transforme o texto JSON `'{\"repos\": [{\"nome\": \"a\", \"estrelas\": 5}, {\"nome\": \"b\", \"estrelas\": 12}]}'` "
     "em objeto Python com `json.loads` e mostre o repositório com mais estrelas.",
     '''import json
resp = json.loads('{"repos": [{"nome": "a", "estrelas": 5}, {"nome": "b", "estrelas": 12}]}')
print(max(resp["repos"], key=lambda r: r["estrelas"])["nome"])'''),

    # ---------------- 10. Trabalhando com dados ----------------
    (10, "Explorando Seus Dados", "Explorar uma e duas dimensões",
     "Gere 1.000 alturas (normal 170, 10) e pesos (peso = 0,9·altura − 90 + ruído). Mostre o histograma das alturas e "
     "a dispersão altura × peso.",
     '''alt = [random.gauss(170, 10) for _ in range(1000)]
peso = [0.9 * a - 90 + random.gauss(0, 5) for a in alt]
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].hist(alt, bins=30); ax[0].set_title("altura")
ax[1].scatter(alt, peso, s=5); ax[1].set_title("altura × peso"); plt.show()'''),
    (10, "Limpando e Transformando", "Limpar linhas sujas",
     "Converta `[[\"2024-01-02\", \"AAA\", \"10.5\"], [\"2024-01-03\", \"BBB\", \"n/a\"], [\"data\", \"AAA\", \"9\"]]` "
     "para (datetime.date, str, float), descartando as linhas que não puderem ser convertidas.",
     '''from datetime import date
def converte(linha):
    try:
        return date.fromisoformat(linha[0]), linha[1], float(linha[2])
    except ValueError:
        return None
brutas = [["2024-01-02", "AAA", "10.5"], ["2024-01-03", "BBB", "n/a"], ["data", "AAA", "9"]]
print([r for r in map(converte, brutas) if r])'''),
    (10, "Manipulando Dados", "Agrupar e resumir sem pandas",
     "Com uma lista de dicionários de vendas `{\"loja\", \"mes\", \"valor\"}` (gere 50 aleatórias), calcule o total por "
     "loja e a maior venda de cada mês usando `defaultdict`.",
     '''vendas = [{"loja": random.choice("XYZ"), "mes": random.randint(1, 3), "valor": round(random.uniform(10, 500), 2)} for _ in range(50)]
total = defaultdict(float); maior = defaultdict(float)
for v in vendas:
    total[v["loja"]] += v["valor"]
    maior[v["mes"]] = max(maior[v["mes"]], v["valor"])
print({k: round(t, 2) for k, t in total.items()}, dict(maior))'''),
    (10, "Redimensionando", "Padronização (z-score)",
     "Distâncias dependem da unidade. Com 3 pessoas (altura em cm, peso em kg), calcule as distâncias entre pares "
     "antes e depois de padronizar cada coluna (média 0, desvio 1).",
     '''pessoas = [[160, 60], [170, 85], [175, 62]]
def padroniza(dados):
    cols = list(zip(*dados))
    m = [sum(c) / len(c) for c in cols]
    s = [math.sqrt(sum((x - mi) ** 2 for x in c) / (len(c) - 1)) for c, mi in zip(cols, m)]
    return [[(x - mi) / si for x, mi, si in zip(p, m, s)] for p in dados]
for dados in (pessoas, padroniza(pessoas)):
    print([round(math.dist(dados[i], dados[j]), 2) for i, j in [(0, 1), (0, 2), (1, 2)]])'''),
    (10, "Redução da Dimensionalidade", "Primeiro componente principal por gradiente",
     "Gere 200 pontos 2D alongados na direção (1, 1). Centralize e encontre a direção de maior variância "
     "maximizando a variância projetada com subida de gradiente (normalizando o vetor a cada passo).",
     '''pts = [[t + random.gauss(0, 0.3), t + random.gauss(0, 0.3)] for t in [random.gauss(0, 2) for _ in range(200)]]
m = [sum(c) / len(c) for c in zip(*pts)]
X = [[x - m[0], y - m[1]] for x, y in pts]
w = [random.random(), random.random()]
for _ in range(500):
    g = [sum(2 * (x[0] * w[0] + x[1] * w[1]) * x[i] for x in X) / len(X) for i in range(2)]
    w = [wi + 0.01 * gi for wi, gi in zip(w, g)]
    n = math.hypot(*w); w = [wi / n for wi in w]
print([round(x, 3) for x in w])  # ~(0,707; 0,707)'''),

    # ---------------- 11. Aprendizado de máquina ----------------
    (11, "Sobreajuste e Sub-Ajuste", "Separar treino e teste",
     "Escreva `separa(dados, prob)` que divide uma lista em treino/teste com proporção `prob` (embaralhando uma cópia). "
     "Teste com 1.000 itens e prob = 0,75.",
     '''def separa(dados, prob):
    d = dados[:]; random.shuffle(d); corte = int(len(d) * prob)
    return d[:corte], d[corte:]
tr, te = separa(list(range(1000)), 0.75)
print(len(tr), len(te), len(set(tr) & set(te)))'''),
    (11, "Precisão", "Acurácia, precisão, revocação e F1",
     "Escreva funções para acurácia, precisão, revocação e F1 a partir de VP, FP, FN e VN. Teste com VP = 70, FP = 4.930, "
     "FN = 13.930, VN = 981.070 e explique por que a acurácia engana aqui.",
     '''def acuracia(vp, fp, fn, vn): return (vp + vn) / (vp + fp + fn + vn)
def precisao(vp, fp, fn, vn): return vp / (vp + fp)
def revocacao(vp, fp, fn, vn): return vp / (vp + fn)
def f1(*c):
    p, r = precisao(*c), revocacao(*c); return 2 * p * r / (p + r)
c = (70, 4930, 13930, 981070)
print([round(f(*c), 4) for f in (acuracia, precisao, revocacao, f1)])
# acurácia 98% porque quase todos são negativos; precisão e revocação mostram que o modelo é ruim'''),

    # ---------------- 12. KNN ----------------
    (12, "O Modelo", "KNN do zero com voto",
     "Escreva `knn(k, pontos_rotulados, novo)` que devolve o rótulo mais votado entre os k vizinhos mais próximos "
     "(em caso de empate, reduza k até desempatar). Teste com 2 nuvens de pontos simuladas.",
     '''def voto(rotulos):
    c = Counter(rotulos); venc, n = c.most_common(1)[0]
    if sum(1 for v in c.values() if v == n) == 1: return venc
    return voto(rotulos[:-1])
def knn(k, rotulados, novo):
    viz = sorted(rotulados, key=lambda p: math.dist(p[0], novo))[:k]
    return voto([r for _, r in viz])
dados = [((random.gauss(0, 1), random.gauss(0, 1)), "azul") for _ in range(50)] + \\
        [((random.gauss(3, 1), random.gauss(3, 1)), "vermelho") for _ in range(50)]
print(knn(5, dados, (0.2, 0.1)), knn(5, dados, (2.8, 3.3)))'''),
    (12, "A Maldição da Dimensionalidade", "Distâncias em muitas dimensões",
     "Para d = 1, 10, 100 e 1.000, gere 500 pontos em [0, 1]ᵈ e calcule a razão entre a menor e a média das "
     "distâncias até um ponto. O que acontece quando d cresce?",
     '''for d in [1, 10, 100, 1000]:
    pts = [[random.random() for _ in range(d)] for _ in range(500)]
    dist = [math.dist(pts[0], p) for p in pts[1:]]
    print(d, round(min(dist) / (sum(dist) / len(dist)), 3))  # tende a 1: todos ficam "igualmente longe"'''),

    # ---------------- 13. Naive Bayes ----------------
    (13, "Implementação", "Filtro de spam Naive Bayes",
     "Treine um Naive Bayes de palavras (suavização k = 0,5) com 8 mensagens rotuladas inventadas por você e "
     "classifique duas mensagens novas, uma com cara de spam e outra normal.",
     '''def tokens(t): return set(re.findall(r"[a-zà-ú0-9']+", t.lower()))
treino = [("ganhe dinheiro rápido agora", True), ("promoção grátis clique aqui", True), ("dinheiro grátis prêmio", True),
          ("clique e ganhe prêmio", True), ("reunião amanhã cedo", False), ("segue o relatório do mês", False),
          ("almoço amanhã com o time", False), ("relatório da reunião", False)]
n_spam = sum(s for _, s in treino); n_ok = len(treino) - n_spam
cont = defaultdict(lambda: [0, 0])
for txt, spam in treino:
    for p in tokens(txt): cont[p][0 if spam else 1] += 1
def p_spam(txt, k=0.5):
    lp_s = lp_o = 0.0
    tk = tokens(txt)
    for p, (s, o) in cont.items():
        ps, po = (s + k) / (n_spam + 2 * k), (o + k) / (n_ok + 2 * k)
        lp_s += math.log(ps if p in tk else 1 - ps); lp_o += math.log(po if p in tk else 1 - po)
    a, b = math.exp(lp_s) * n_spam, math.exp(lp_o) * n_ok
    return a / (a + b)
print(round(p_spam("ganhe um prêmio grátis"), 3), round(p_spam("relatório da reunião de amanhã"), 3))'''),

    # ---------------- 14. Regressão linear simples ----------------
    (14, "O Modelo", "Mínimos quadrados com fórmula fechada",
     "Escreva `ajuste(x, y)` que devolve (alfa, beta) por β = cor·sy/sx e α = ȳ − βx̄, e `r_quadrado`. Teste com "
     "y = 3 + 2x + ruído.",
     '''def media(v): return sum(v) / len(v)
def dp(v): m = media(v); return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1))
def cor(x, y):
    mx, my = media(x), media(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (len(x) - 1) / (dp(x) * dp(y))
def ajuste(x, y):
    beta = cor(x, y) * dp(y) / dp(x); return media(y) - beta * media(x), beta
def r_quadrado(a, b, x, y):
    my = media(y); sse = sum((yi - (a + b * xi)) ** 2 for xi, yi in zip(x, y))
    return 1 - sse / sum((yi - my) ** 2 for yi in y)
x = [random.uniform(0, 10) for _ in range(100)]; y = [3 + 2 * xi + random.gauss(0, 1) for xi in x]
a, b = ajuste(x, y); print(round(a, 3), round(b, 3), round(r_quadrado(a, b, x, y), 3))'''),

    # ---------------- 15. Regressão múltipla ----------------
    (15, "Digressão: A Inicialização", "Bootstrap para o erro de uma estatística",
     "Com 101 valores simulados, estime o desvio-padrão da mediana por *bootstrap* (1.000 reamostragens com "
     "reposição).",
     '''dados = [random.gauss(50, 10) for _ in range(101)]
def mediana(v): s = sorted(v); return s[len(s) // 2]
meds = [mediana(random.choices(dados, k=len(dados))) for _ in range(1000)]
m = sum(meds) / len(meds)
print(round(math.sqrt(sum((x - m) ** 2 for x in meds) / (len(meds) - 1)), 3))'''),
    (15, "Regularização", "Regressão ridge por gradiente",
     "Ajuste y = 1 + 2x₁ − 3x₂ por gradiente descendente com penalização ridge (α·Σβ², sem penalizar o intercepto) "
     "para α = 0 e α = 10. Como os coeficientes mudam?",
     '''X = [[1, random.gauss(0, 1), random.gauss(0, 1)] for _ in range(200)]
y = [1 + 2 * x1 - 3 * x2 + random.gauss(0, 0.5) for _, x1, x2 in X]
def ridge(alfa, passos=2000, lr=0.01):
    b = [0.0, 0.0, 0.0]
    for _ in range(passos):
        g = [0.0, 0.0, 0.0]
        for xi, yi in zip(X, y):
            e = sum(bj * xj for bj, xj in zip(b, xi)) - yi
            for j in range(3): g[j] += 2 * e * xi[j] / len(X)
        for j in range(1, 3): g[j] += 2 * alfa * b[j] / len(X)
        b = [bj - lr * gj for bj, gj in zip(b, g)]
    return [round(v, 3) for v in b]
print(ridge(0), ridge(10))'''),

    # ---------------- 16. Regressão logística ----------------
    (16, "A Função Logística", "Logística por gradiente",
     "Gere 300 pontos com P(y = 1) = logística(−2 + 1,5x). Ajuste os coeficientes maximizando a log-verossimilhança "
     "por subida de gradiente e compare com os valores verdadeiros.",
     '''def logistica(t): return 1 / (1 + math.exp(-t))
xs = [random.uniform(-3, 5) for _ in range(300)]
ys = [1 if random.random() < logistica(-2 + 1.5 * x) else 0 for x in xs]
a = b = 0.0
for _ in range(3000):
    ga = sum(y - logistica(a + b * x) for x, y in zip(xs, ys)) / len(xs)
    gb = sum((y - logistica(a + b * x)) * x for x, y in zip(xs, ys)) / len(xs)
    a += 0.1 * ga; b += 0.1 * gb
print(round(a, 2), round(b, 2))'''),

    # ---------------- 17. Árvores de decisão ----------------
    (17, "Entropia", "Entropia de uma lista de rótulos",
     "Escreva `entropia(rotulos)` (em bits). Calcule para `['s']*10`, `['s']*5 + ['n']*5` e `['a', 'b', 'c', 'd']`.",
     '''def entropia(rotulos):
    n = len(rotulos)
    return -sum(c / n * math.log2(c / n) for c in Counter(rotulos).values())
print(entropia(["s"] * 10), entropia(["s"] * 5 + ["n"] * 5), entropia(list("abcd")))'''),
    (17, "Criando uma Árvore", "Qual atributo divide melhor?",
     "Com candidatos inventados `{nivel, linguagem, tem_github, bom}`, calcule a entropia da partição por cada "
     "atributo e diga qual deveria ser a raiz da árvore.",
     '''def entropia(r):
    n = len(r); return -sum(c / n * math.log2(c / n) for c in Counter(r).values())
cands = [("senior", "java", False, False), ("senior", "java", True, False), ("pleno", "python", False, True),
         ("junior", "python", False, True), ("junior", "r", True, True), ("junior", "r", False, False),
         ("pleno", "r", True, True), ("senior", "python", False, False), ("senior", "r", True, True), ("junior", "python", True, True)]
nomes = ["nivel", "linguagem", "tem_github"]
for i, nome in enumerate(nomes):
    grupos = defaultdict(list)
    for c in cands: grupos[c[i]].append(c[3])
    print(nome, round(sum(len(g) / len(cands) * entropia(g) for g in grupos.values()), 3))'''),

    # ---------------- 18. Redes neurais ----------------
    (18, "Perceptrons", "Portas lógicas com perceptron",
     "Escreva `perceptron(pesos, vies, x)` com função degrau e escolha pesos que implementem AND e OR. Mostre a "
     "tabela-verdade. Por que nenhum perceptron sozinho faz XOR?",
     '''def perceptron(w, b, x): return 1 if sum(wi * xi for wi, xi in zip(w, x)) + b >= 0 else 0
for x in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(x, "AND:", perceptron([2, 2], -3, x), "OR:", perceptron([2, 2], -1, x))
# XOR não é linearmente separável: nenhuma reta separa (0,1),(1,0) de (0,0),(1,1)'''),
    (18, "Backpropagation", "XOR com uma rede de 2 camadas",
     "Treine por *backpropagation* uma rede 2-2-1 com sigmoide para aprender XOR (10.000 épocas, taxa 1,0). "
     "Mostre a saída para as 4 entradas.",
     '''def sig(t): return 1 / (1 + math.exp(-t))
random.seed(1)
oculta = [[random.random() for _ in range(3)] for _ in range(2)]
saida = [random.random() for _ in range(3)]
dados = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)]
for _ in range(10_000):
    for x, y in dados:
        xb = list(x) + [1]
        h = [sig(sum(w * v for w, v in zip(n, xb))) for n in oculta]; hb = h + [1]
        o = sig(sum(w * v for w, v in zip(saida, hb)))
        d_o = o * (1 - o) * (o - y)
        d_h = [h[i] * (1 - h[i]) * d_o * saida[i] for i in range(2)]
        saida = [w - 1.0 * d_o * v for w, v in zip(saida, hb)]
        oculta = [[w - 1.0 * d_h[i] * v for w, v in zip(oculta[i], xb)] for i in range(2)]
for x, _ in dados:
    xb = list(x) + [1]; hb = [sig(sum(w * v for w, v in zip(n, xb))) for n in oculta] + [1]
    print(x, round(sig(sum(w * v for w, v in zip(saida, hb))), 3))'''),

    # ---------------- 19. Agrupamento ----------------
    (19, "O Modelo", "k-médias do zero",
     "Implemente k-médias (atribui ao centro mais próximo, recalcula os centros, para quando nada muda) e aplique "
     "a 3 nuvens de pontos simuladas.",
     '''def kmeans(pontos, k):
    centros = random.sample(pontos, k); atrib = None
    while True:
        nova = [min(range(k), key=lambda i: math.dist(p, centros[i])) for p in pontos]
        if nova == atrib: return centros, atrib
        atrib = nova
        for i in range(k):
            membros = [p for p, a in zip(pontos, atrib) if a == i]
            if membros: centros[i] = [sum(c) / len(membros) for c in zip(*membros)]
pts = [[random.gauss(cx, 0.7), random.gauss(cy, 0.7)] for cx, cy in [(0, 0), (5, 5), (0, 6)] for _ in range(60)]
centros, atrib = kmeans(pts, 3)
print([[round(c, 2) for c in ct] for ct in centros])
plt.scatter(*zip(*pts), c=atrib); plt.scatter(*zip(*centros), marker="x", s=200, c="red"); plt.show()'''),
    (19, "Escolhendo k", "Cotovelo",
     "Para k de 1 a 8, calcule a soma dos quadrados das distâncias de cada ponto ao seu centro, com o k-médias "
     "do exercício anterior, e desenhe a curva.",
     '''def kmeans(pontos, k):
    centros = random.sample(pontos, k); atrib = None
    while True:
        nova = [min(range(k), key=lambda i: math.dist(p, centros[i])) for p in pontos]
        if nova == atrib: return centros, atrib
        atrib = nova
        for i in range(k):
            m = [p for p, a in zip(pontos, atrib) if a == i]
            if m: centros[i] = [sum(c) / len(m) for c in zip(*m)]
pts = [[random.gauss(cx, 0.7), random.gauss(cy, 0.7)] for cx, cy in [(0, 0), (5, 5), (0, 6)] for _ in range(60)]
erros = []
for k in range(1, 9):
    c, a = kmeans(pts, k); erros.append(sum(math.dist(p, c[i]) ** 2 for p, i in zip(pts, a)))
plt.plot(range(1, 9), erros, marker="o"); plt.xlabel("k"); plt.show()'''),

    # ---------------- 20. NLP ----------------
    (20, "Modelos n-gramas", "Gerador de texto com bigramas",
     "Monte um modelo de bigramas (palavra → lista de próximas palavras) a partir de um parágrafo seu e gere uma "
     "frase de até 15 palavras sorteando a próxima palavra.",
     '''texto = ("os dados contam uma história . os dados precisam de cuidado . uma boa análise começa com dados limpos . "
         "a história dos dados começa com uma pergunta .")
palavras = texto.split()
transicoes = defaultdict(list)
for a, b in zip(palavras, palavras[1:]):
    transicoes[a].append(b)
atual, frase = "os", ["os"]
while atual != "." and len(frase) < 15:
    atual = random.choice(transicoes[atual]); frase.append(atual)
print(" ".join(frase))'''),
    (20, "Gramáticas", "Frases a partir de uma gramática",
     "Defina uma gramática pequena (`_F -> _SN _V`, `_SN -> _D _S | _D _S _A` ...) num dicionário e escreva uma "
     "função recursiva que gera frases aleatórias expandindo os símbolos que começam com `_`.",
     '''gramatica = {"_F": ["_SN _V _SN"], "_SN": ["_D _S", "_D _S _A"], "_D": ["o", "um"],
             "_S": ["cientista", "modelo", "gráfico"], "_A": ["curioso", "preciso", "lento"], "_V": ["analisa", "treina", "explica"]}
def expande(simbolo):
    if not simbolo.startswith("_"): return simbolo
    return " ".join(expande(s) for s in random.choice(gramatica[simbolo]).split())
for _ in range(3): print(expande("_F"))'''),

    # ---------------- 21. Análise de rede ----------------
    (21, "Gráficos Direcionados e PageRank", "PageRank iterativo",
     "Com o grafo dirigido `{0: [1, 2], 1: [2], 2: [0], 3: [2]}`, implemente o PageRank com amortecimento 0,85 "
     "(100 iterações, começando de 1/n) e mostre o ranking.",
     '''links = {0: [1, 2], 1: [2], 2: [0], 3: [2]}
n = len(links); pr = {u: 1 / n for u in links}
for _ in range(100):
    novo = {u: 0.15 / n for u in links}
    for u, destinos in links.items():
        for v in destinos: novo[v] += 0.85 * pr[u] / len(destinos)
    pr = novo
print({u: round(p, 3) for u, p in sorted(pr.items(), key=lambda kv: -kv[1])})'''),

    # ---------------- 22. Recomendadores ----------------
    (22, "Recomendando O Que é Popular", "Os mais populares que você não tem",
     "Com interesses de 6 usuários (listas de tópicos inventadas), conte a popularidade de cada tópico e recomende "
     "ao usuário 0 os 3 tópicos mais populares que ele ainda não tem.",
     '''interesses = [["python", "estatística"], ["python", "sql", "ml"], ["ml", "estatística", "r"],
              ["sql", "python", "ml"], ["r", "estatística"], ["ml", "deep learning", "python"]]
pop = Counter(t for u in interesses for t in u)
print([t for t, _ in pop.most_common() if t not in interesses[0]][:3])'''),
    (22, "Filtragem Colaborativa Baseada no Usuário", "Usuários parecidos (cosseno)",
     "Transforme os interesses em vetores 0/1, calcule a similaridade de cosseno entre o usuário 0 e os outros e "
     "recomende os tópicos dos usuários parecidos, pesados pela similaridade.",
     '''interesses = [["python", "estatística"], ["python", "sql", "ml"], ["ml", "estatística", "r"],
              ["sql", "python", "ml"], ["r", "estatística"], ["ml", "deep learning", "python"]]
topicos = sorted({t for u in interesses for t in u})
vet = [[1 if t in u else 0 for t in topicos] for u in interesses]
def cos(a, b): return sum(x * y for x, y in zip(a, b)) / math.sqrt(sum(a) * sum(b))
score = defaultdict(float)
for j in range(1, len(vet)):
    s = cos(vet[0], vet[j])
    for t in interesses[j]:
        if t not in interesses[0]: score[t] += s
print(sorted(score.items(), key=lambda kv: -kv[1]))'''),

    # ---------------- 23. SQL ----------------
    (23, "CREATE TABLE e INSERT", "SQL de verdade com sqlite3",
     "Crie em memória (`sqlite3.connect(\":memory:\")`) a tabela `usuarios(id, nome, amigos)`, insira 5 linhas e "
     "consulte os usuários com mais de 2 amigos, ordenados por nome.",
     '''import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, amigos INTEGER)")
con.executemany("INSERT INTO usuarios VALUES (?, ?, ?)", [(0, "Hero", 2), (1, "Dunn", 3), (2, "Sue", 3), (3, "Chi", 3), (4, "Thor", 1)])
print(con.execute("SELECT nome, amigos FROM usuarios WHERE amigos > 2 ORDER BY nome").fetchall())'''),
    (23, "JOIN", "JOIN e GROUP BY",
     "Acrescente a tabela `interesses(usuario_id, interesse)` e responda em SQL: quantos interesses cada usuário tem "
     "(incluindo quem tem zero, com `LEFT JOIN`) e quem se interessa por SQL.",
     '''import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
con.execute("CREATE TABLE interesses (usuario_id INTEGER, interesse TEXT)")
con.executemany("INSERT INTO usuarios VALUES (?, ?)", [(0, "Hero"), (1, "Dunn"), (2, "Sue")])
con.executemany("INSERT INTO interesses VALUES (?, ?)", [(0, "SQL"), (0, "NoSQL"), (2, "MySQL"), (2, "SQL")])
print(con.execute("SELECT u.nome, COUNT(i.interesse) FROM usuarios u LEFT JOIN interesses i ON u.id = i.usuario_id GROUP BY u.id").fetchall())
print(con.execute("SELECT u.nome FROM usuarios u JOIN interesses i ON u.id = i.usuario_id WHERE i.interesse = 'SQL'").fetchall())'''),

    # ---------------- 24. MapReduce ----------------
    (24, "Exemplo: Contagem de Palavras", "MapReduce do zero",
     "Escreva `map_reduce(entradas, mapper, reducer)` genérica (mapper gera pares chave-valor; agrupe por chave; "
     "reducer resume cada grupo) e use para contar palavras em 4 frases.",
     '''def map_reduce(entradas, mapper, reducer):
    grupos = defaultdict(list)
    for e in entradas:
        for k, v in mapper(e): grupos[k].append(v)
    return [saida for k, vs in grupos.items() for saida in reducer(k, vs)]
def mapper(doc):
    for p in doc.lower().split(): yield p, 1
def reducer(palavra, contagens):
    yield palavra, sum(contagens)
docs = ["dados são legais", "dados grandes", "dados e mais dados", "python é legal"]
print(sorted(map_reduce(docs, mapper, reducer), key=lambda kv: -kv[1])[:3])'''),
    (24, "Exemplo: Multiplicação de Matriz", "Multiplicação de matrizes com MapReduce",
     "Represente A (2×3) e B (3×2) como listas esparsas `(matriz, linha, coluna, valor)` e calcule C = A·B com "
     "MapReduce, conferindo com a multiplicação comum.",
     '''A = [[1, 2, 0], [0, 3, 4]]; B = [[5, 0], [1, 2], [0, 6]]
esparsa = [("A", i, j, v) for i, l in enumerate(A) for j, v in enumerate(l) if v] + \\
          [("B", i, j, v) for i, l in enumerate(B) for j, v in enumerate(l) if v]
linhas_A, colunas_B = 2, 2
def mapper(e):
    m, i, j, v = e
    if m == "A":
        for col in range(colunas_B): yield (i, col), (m, j, v)
    else:
        for lin in range(linhas_A): yield (lin, j), (m, i, v)
def reducer(chave, vals):
    a = {k: v for m, k, v in vals if m == "A"}; b = {k: v for m, k, v in vals if m == "B"}
    yield chave, sum(a[k] * b[k] for k in a if k in b)
grupos = defaultdict(list)
for e in esparsa:
    for k, v in mapper(e): grupos[k].append(v)
C = dict(kv for k, vs in grupos.items() for kv in reducer(k, vs))
print([[C[(i, j)] for j in range(2)] for i in range(2)])
print([[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(2)] for i in range(2)])'''),
]
