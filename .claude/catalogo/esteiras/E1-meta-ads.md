# Esteira E1 — Campanha Meta Ads (Facebook + Instagram)

## Quando usar

- Lançamento de campanha no Meta Ads Manager
- Escalar campanha orgânica que já demonstra demanda
- Campanha de remarketing para base existente
- Tráfego pago para landing page ou evento

## Pré-requisitos

- **A1** (ICP & Persona) — segmentação de públicos
- **A2** (Posicionamento) — mensagem central da campanha
- **E4** (Landing Page) — destino do tráfego (muito recomendado)

## Entrada esperada

- Objetivo da campanha (awareness, tráfego, leads, conversão, catálogo)
- Público-alvo principal com dados demográficos e interesses
- Budget mensal estimado (pode ser R$300/mês para começar)
- Landing page ou destino do anúncio (URL)
- Prazo da campanha

## Sequência de execução

### Passo 1 — ads-strategist
- **Input:** objetivo + ICP + budget + prazo
- **Output:** estrutura completa de campanha:
  - Arquitetura (campanhas > conjuntos de anúncios > anúncios)
  - 3 públicos: topo (interesse), meio (engajamento), fundo (remarketing/lookalike)
  - Distribuição de budget por público
  - Pixels e eventos de conversão a configurar
- **Como chamar:** chame o agente `ads-strategist` com todos os inputs

### Passo 2 — /facebook-ads
- **Input:** estrutura do Passo 1 + produto + público + landing page
- **Output:** copy completo de anúncios por público:
  - Headline principal + headline secundário
  - Texto do anúncio (primary text)
  - CTA recomendado
  - Descrição do link
  - Brief do criativo (imagem ou vídeo)
- **Como chamar:** `/facebook-ads` — forneça estrutura, produto, público e landing page

### Passo 3 — /copy-anatomy
- **Input:** copy principal do anúncio (Passo 2)
- **Output:** variações para A/B test:
  - 3 headlines alternativas
  - 2 variações de primary text (uma emocional, uma racional)
  - 2 CTAs alternativos
- **Como chamar:** `/copy-anatomy` — peça variações de copy para A/B test

### Passo 4 — growth-hacker
- **Input:** estrutura completa da campanha + métricas-alvo
- **Output:** plano de A/B test estruturado:
  - Hipóteses com ICE score (impacto, confiança, esforço)
  - Cronograma de testes (o que testar primeiro, quando)
  - Gatilhos de decisão (quando pausar, escalar ou duplicar)
  - KPIs por fase: ROAS, CPM, CTR, CPC, CPL, CPA
- **Como chamar:** chame o agente `growth-hacker` com a estrutura e métricas-alvo

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `estrutura-campanha.md` | Arquitetura completa com públicos e budget |
| `copy-ads.md` | Copy por público com headlines, textos e CTAs |
| `variacoes-abteste.md` | Variações para teste com hipóteses ICE |
| `plano-otimizacao.md` | Cronograma de testes e gatilhos de decisão |

## Ativa próximas esteiras

- **E5** (Performance) → auditoria após primeiros 30 dias
- **F3** (Experimento) → hipóteses de otimização baseadas em dados reais
- **E4** (Landing Page) → otimizar landing com base no CRO dos anúncios
