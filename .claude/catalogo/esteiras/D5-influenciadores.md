# Esteira D5 — Outreach de Influenciadores

## Quando usar

- Lançamento de produto que precisa de amplificação rápida
- Construção de prova social via criadores de conteúdo
- Estratégia de brand awareness com budget limitado (micro/nano)
- Parceria de longo prazo com embaixadores da marca

## Pré-requisitos

- **A1** (ICP & Persona) — para identificar quem a persona segue e em quem confia
- **A2** (Posicionamento) — para garantir alinhamento de valores na escolha dos influenciadores

## Entrada esperada

- Nicho / categoria de influenciadores buscados
- Plataformas (Instagram, TikTok, YouTube)
- Tier desejado: nano (1k-10k), micro (10k-100k), médio (100k-500k)
- Tipo de parceria: permuta, comissão, cachê, embaixador
- Objetivo: awareness, vendas (com cupom), UGC, lançamento
- Budget estimado (mesmo que zero — para permuta)

## Sequência de execução

### Passo 1 — /scraping
- **Input:** nicho + plataformas + concorrentes da marca
- **Output:** lista de influenciadores que já falam do nicho ou dos concorrentes, dados de engajamento aproximado, hashtags usadas, linguagem da audiência
- **Como chamar:** `/scraping` — peça pesquisa de influenciadores do nicho em [plataformas]

### Passo 2 — /influencer-outreach
- **Input:** lista do Passo 1 + tier + tipo de parceria + objetivo + posicionamento da marca
- **Output:**
  - Lista priorizada de influenciadores com tier, engajamento estimado e fit com a marca
  - Template de DM/e-mail de primeiro contato (personalizado por tier)
  - Modelo de proposta formal com escopo, entregáveis, prazo e contrapartida
  - Checklist de qualificação pré-contato
- **Como chamar:** `/influencer-outreach` — forneça a lista, o tier, o tipo de parceria e o objetivo

### Passo 3 — social-media-manager (para gestão do relacionamento)
- **Input:** influenciadores confirmados + briefing da campanha
- **Output:** briefing criativo para o influenciador (do's and don'ts, mensagens obrigatórias, formatos e datas de entrega), processo de aprovação de conteúdo antes da publicação
- **Como chamar:** chame `social-media-manager` pedindo briefing criativo para influenciadores

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `lista-influenciadores.md` | Lista priorizada com tier, plataforma, engajamento e fit |
| `template-contato.md` | DM/e-mail de primeiro contato por tier |
| `proposta-parceria.md` | Modelo de proposta com escopo, entregáveis e contrapartida |
| `briefing-criativo.md` | Diretrizes criativas para o influenciador (do's/don'ts, mensagens) |

## Ativa próximas esteiras

- **D6** (Engajamento) → monitorar e responder ao conteúdo gerado pelos influenciadores
- **F1** (Relatório) → medir o resultado das parcerias no relatório mensal
- **E1** (Meta Ads) → usar conteúdo de influenciadores como creative nos Spark Ads
