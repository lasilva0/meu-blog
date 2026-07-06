# L-Stats Blog

Blog pessoal sobre estatística, ciência de dados e matemática. Os posts cobrem desde curiosidades matemáticas até tópicos mais técnicos como redes neurais, otimização e inferência estatística.

Construído com [Quarto](https://quarto.org) e publicado via GitHub Pages.

**Site:** [https://lasilva0.github.io/meu-blog](https://lasilva0.github.io/meu-blog)

## Estrutura

```
meu-blog/
├── posts/                  # um diretório por post
│   ├── AAAA-MM-DD-slug/
│   │   ├── index.qmd       # conteúdo do post
│   │   └── *.png / *.py    # figuras e scripts
├── docs/                   # saída do quarto render (GitHub Pages)
├── _quarto.yml             # configuração do site
├── styles.css              # customizações visuais
├── index.qmd               # página inicial (listing dos posts)
└── about.qmd               # página sobre
```

## Posts

| Data | Título | Categorias |
|------|--------|------------|
| 2026-07-06 | Alguns tópicos sobre redes neurais | redes neurais |
| 2026-07-06 | Otimização de funções via gradiente descendente | otimização, matemática |
| 2026-07-06 | Perceptron Simples | redes neurais, matemática |
| 2026-02-10 | Brincando um pouco com senos e cossenos | matemática |
| 2025-05-21 | Uma propriedade interessante envolvendo números transcendentais | matemática |

## Como rodar localmente

Requer [Quarto](https://quarto.org/docs/get-started/) instalado.

```bash
# visualizar com live reload
quarto preview

# gerar os arquivos estáticos em docs/
quarto render
```

As figuras geradas por scripts Python ficam na pasta de cada post. Para regenerá-las:

```bash
python posts/<slug>/gerar_figuras.py
```

## Deploy

O site é publicado automaticamente via GitHub Pages a partir da pasta `docs/`. Basta fazer push para a branch `main` após rodar `quarto render`.
