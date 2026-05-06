# Esteira F4 — Inteligência Competitiva

## Quando usar

- Antes de entrar em um novo mercado ou segmento
- Quando um concorrente está crescendo rápido e você quer entender por quê
- Revisão trimestral de posicionamento vs. concorrência
- Identificação de gaps de mercado para diferenciação

## Pré-requisitos

- **A1** (ICP & Persona) — para filtrar dados de concorrentes que atendem o mesmo ICP

## Entrada esperada

- Lista de 3-5 concorrentes diretos (URLs, redes sociais, nomes)
- Aspectos a monitorar: conteúdo, canais, ads ativos, precificação, posicionamento, reviews
- Perguntas específicas (ex: "qual canal eles mais investem?", "o que os clientes reclamam?")
- Frequência de atualização (pontual ou recorrente)

## Sequência de execução

### Passo 1 — /scraping
- **Input:** lista de concorrentes + aspectos a monitorar + perguntas específicas
- **Output:**
  - Análise de conteúdo de cada concorrente (temas, formatos, frequência, engajamento)
  - Canais ativos e nível de investimento estimado
  - Ads ativos (via Meta Ads Library, se solicitado)
  - Reviews e reclamações em sites públicos (Reclame Aqui, G2, Trustpilot)
  - Linguagem e mensagens usadas em headlines e CTAs
- **Como chamar:** `/scraping` — informe concorrentes, aspectos a monitorar e perguntas específicas

### Passo 2 — analytics-analyst
- **Input:** dados coletados no Passo 1 + posicionamento da sua marca
- **Output:** análise comparativa: onde você está à frente, onde está atrás, gaps não explorados por ninguém (oportunidades), ameaças que precisam de resposta rápida
- **Como chamar:** chame `analytics-analyst` com os dados do scraping; peça análise de gaps e ameaças

### Passo 3 — /diagrama
- **Input:** análise comparativa (Passo 2) + critérios de comparação
- **Output:** diagrama de quadrante (2×2) ou radar comparando sua marca vs. concorrentes nos critérios mais relevantes
- **Como chamar:** `/diagrama` — peça quadrant chart ou radar chart comparando [sua marca] vs. [concorrentes] em [critérios]

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `relatorio-concorrentes.md` | Análise detalhada de cada concorrente: canais, conteúdo, ads, mensagens, reviews |
| `analise-gaps.md` | Gaps de mercado, oportunidades não exploradas e ameaças mapeadas |
| `mapa-competitivo.md` | Diagrama visual de posicionamento comparativo |

## Ativa próximas esteiras

- **A2** (Posicionamento) → usar os gaps identificados para refinar o posicionamento
- **G1** (Inteligência de Mercado) → aprofundar a pesquisa com dados qualitativos de clientes
- **B1** (Estratégia Editorial) → pautar conteúdo nos gaps não cobertos pelos concorrentes
