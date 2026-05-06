# Esteira B3 — Conteúdo Rico

## Quando usar

- Geração de leads qualificados com isca de alto valor percebido
- Autoridade aprofundada em um tema do nicho
- Nurturing de leads que já conhecem a marca mas não converteram
- Suporte ao time de vendas (case study, white paper técnico)

## Pré-requisitos

- **A1** (ICP & Persona) — para calibrar profundidade e linguagem do conteúdo
- **A2** (Posicionamento) — para garantir que o conteúdo reforça o posicionamento da marca

## Entrada esperada

- Tema central do conteúdo rico
- Formato: ebook, white paper, case study (escolher um)
- Objetivo: captura de leads, nurturing, suporte a vendas, autoridade
- Dados ou história disponíveis (para case study: nome do cliente, resultados reais)
- Nível técnico do público: leigo, intermediário, especialista

## Sequência de execução

### Passo 1 — seo-specialist
- **Input:** tema + formato + nível técnico do público
- **Output:** palavras-chave de cauda longa para título e subtítulos, análise de conteúdos similares já existentes (gaps a explorar), sugestão de título com alto potencial de busca
- **Como chamar:** chame `seo-specialist` com o tema e o formato; peça análise de keywords e gaps

### Passo 2a — /ebook-outline (se formato = ebook)
- **Input:** tema + objetivo + persona + keywords (Passo 1)
- **Output:** sumário completo com capítulos, subseções, introdução e conclusão; sugestões de design e call-to-actions internos
- **Como chamar:** `/ebook-outline` — forneça tema, objetivo e persona

### Passo 2b — /white-paper (se formato = white paper)
- **Input:** tema + nível técnico + empresa + dados disponíveis + keywords (Passo 1)
- **Output:** white paper completo (8-20 páginas): executive summary, problema, solução, dados/evidências, conclusão, próximos passos e referências
- **Como chamar:** `/white-paper` — forneça tema, nível técnico e dados disponíveis

### Passo 2c — /case-study (se formato = case study)
- **Input:** nome do cliente, situação antes, intervenção realizada, resultados mensuráveis
- **Output:** case study no formato problema-solução-resultado com depoimento, métricas e CTA para contato
- **Como chamar:** `/case-study` — forneça todos os dados do cliente e resultados

### Passo 3 — /landing-page
- **Input:** título e benefícios do conteúdo rico (Passo 2) + persona + CTA de captação
- **Output:** copy completo da landing page de captura: hero, o que você vai aprender, para quem é, formulário e prova social
- **Como chamar:** `/landing-page` — forneça o título, benefícios e persona do conteúdo rico

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `conteudo-rico.md` | Ebook (outline) ou white paper completo ou case study |
| `landing-captura.md` | Copy completo da landing page de captura de leads |

## Ativa próximas esteiras

- **E1-E3** (Ads) → promover o conteúdo rico como isca via tráfego pago
- **B4** (Podcast/Webinar) → gravar um episódio ou live sobre o tema do conteúdo rico
- **D3** (LinkedIn) → artigo sobre o tema do white paper para gerar leads orgânicos
- **B2** (Blog & SEO) → série de artigos baseados nos capítulos do ebook
