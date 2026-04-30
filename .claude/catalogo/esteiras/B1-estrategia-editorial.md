# Esteira B1 — Estratégia Editorial

## Quando usar

- Início de presença digital (canal, blog ou redes do zero)
- Revisão semestral da estratégia de conteúdo
- Entrada em novo canal
- Quando o conteúdo está sem direção ou coerência

## Pré-requisitos

- **A1** (ICP & Persona)
- **A2** (Posicionamento de Marca)

## Entrada esperada

- ICP e personas (output A1)
- Posicionamento e pilares de mensagem (output A2)
- Canais ativos (Instagram, YouTube, LinkedIn, TikTok, blog...)
- Frequência de publicação disponível (posts/semana por canal)
- Objetivo principal de conteúdo (awareness, leads, vendas, autoridade)

## Sequência de execução

### Passo 1 — content-strategist
- **Input:** ICP + posicionamento + canais + frequência + objetivo
- **Output:** 3-5 pilares editoriais com descrição, tipos de conteúdo por pilar, guia de voz e tom por canal, e regras de repurposing
- **Como chamar:** chame o agente `content-strategist` com todos os inputs

### Passo 2 — /content-calendar
- **Input:** pilares editoriais (Passo 1) + canais + frequência
- **Output:** calendário editorial de 30 dias em tabela markdown com data, canal, formato, pilar, título sugerido, CTA e status
- **Como chamar:** `/content-calendar` — informe pilares, canais e frequência por canal

### Passo 3 — /diagrama
- **Input:** pilares editoriais + fluxo de repurposing
- **Output:** dois diagramas Mermaid:
  1. Mindmap dos pilares de conteúdo
  2. Fluxo de repurposing (conteúdo-raiz → derivações por canal)
- **Como chamar:** `/diagrama` — peça mindmap de pilares e fluxo de repurposing

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `pilares-editoriais.md` | 3-5 pilares com descrição, tipos de conteúdo e guia de voz |
| `calendario-30d.md` | Calendário mensal pronto para Notion/Sheets |
| `fluxo-repurposing.md` | Diagramas visuais de pilares e repurposing |

## Ativa próximas esteiras

- **B2** (Blog+SEO) → primeiro artigo de cada pilar
- **B4** (Podcast/Webinar) → episódio baseado em pilar
- **C1** (YouTube Longo) → vídeo do pilar principal
- **C2** (Short Video) → derivações dos vídeos longos
- **D1** (Social Completo) → usa calendário como base do planejamento mensal
