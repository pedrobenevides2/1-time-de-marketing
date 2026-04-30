# Esteira C2 — Short Video (Reels / TikTok / Shorts)

## Quando usar

- Produção de vídeos curtos para TikTok, Instagram Reels ou YouTube Shorts
- Repurposing de vídeo longo existente (cortes estratégicos)
- Campanha de topo de funil via vídeo curto
- Publicação diária/frequente de conteúdo nativo

## Pré-requisitos

- **A1** (ICP & Persona) — para gancho e linguagem
- **C1** (YouTube Longo) — se for repurposing de vídeo existente (opcional)

## Entrada esperada

- Tópico OU vídeo longo existente (para cortes)
- Plataformas alvo (TikTok, Reels, Shorts — pode ser todas)
- Objetivo (crescimento de audiência, leads, vendas, autoridade)
- Frequência desejada (posts/semana)
- Recursos disponíveis (câmera, teleprompter, CapCut, etc.)

## Sequência de execução

### Passo 1 — short-video-creator
- **Input:** tópico (ou vídeo longo) + plataformas + objetivo + ICP
- **Output:** 5 ângulos de hook para o tópico + estrutura narrativa para vídeo de 30-60 segundos + estratégia de frequência e temas por plataforma
- **Como chamar:** chame o agente `short-video-creator` com todos os inputs

### Passo 2 — /video-script
- **Input:** hook selecionado do Passo 1 + formato (15s / 30s / 60s) + CTA
- **Output:** roteiro curto e denso com:
  - Hook (primeiros 3 segundos)
  - Desenvolvimento (problema → solução ou insight)
  - CTA final (call to action específico)
  - Legendas automáticas sugeridas
  - Instruções de edição no CapCut
- **Como chamar:** `/video-script` — informe hook, duração e CTA

### Passo 3 — skill de plataforma (escolha conforme canal principal)

**Se TikTok:**
- **Como chamar:** `/tiktok-strategy` — peça hashtags, legenda adaptada e horário ideal de postagem para o tópico

**Se Instagram Reels:**
- **Como chamar:** `/instagram-publisher` — peça legenda, hashtags e configuração de Reels para o roteiro

**Se YouTube Shorts:**
- **Como chamar:** `/youtube-seo` — peça título (até 100 chars), descrição curta e hashtags para o Short

### Passo 4 — short-video-creator
- **Input:** vídeo aprovado + plataformas alvo
- **Output:** plano de repurposing sem marca d'água:
  - TikTok → Reels (ajuste de proporção e legenda)
  - Reels → Shorts (ajuste de título e descrição)
  - Sequência de postagem (qual plataforma primeiro, intervalo entre posts)
- **Como chamar:** chame o agente `short-video-creator` pedindo o plano de repurposing

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `roteiros-curtos.md` | 3-5 roteiros de vídeos curtos prontos |
| `legendas-hashtags.md` | Legendas e hashtags por plataforma |
| `calendario-postagem.md` | Plano de publicação com datas e plataformas |
| `plano-repurposing.md` | Sequência de repurposing cross-platform |

## Ativa próximas esteiras

- **D1** (Social Completo) → integrar vídeos curtos no calendário social
- **E3** (TikTok Ads) → transformar melhor short em Spark Ad
- **F1** (Relatório) → medir performance dos shorts após 30 dias
