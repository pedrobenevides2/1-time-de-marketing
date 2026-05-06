# Esteira E3 — Campanha TikTok Ads

## Quando usar

- Público jovem (18-35) ou produto com forte apelo visual/entretenimento
- Produto que pode ser demonstrado de forma rápida e autêntica
- Alcance de audiência que não está no Meta
- Custo por clique frequentemente menor que Meta em nichos competitivos

## Pré-requisitos

- **A1** (ICP & Persona) — para segmentação e linguagem dos criativos
- **A2** (Posicionamento) — para manter consistência de mensagem

## Entrada esperada

- Produto ou serviço a ser anunciado
- Objetivo: tráfego, conversão, geração de leads, awareness, instalação de app
- Budget mensal estimado
- Criativos disponíveis ou precisam ser produzidos
- Audiência-alvo
- Landing page de destino

## Sequência de execução

### Passo 1 — ads-strategist
- **Input:** produto + objetivo + budget + audiência + landing page
- **Output:** estrutura no TikTok Ads Manager: objetivo de campanha, tipo de anúncio (In-Feed, TopView, Spark Ads, Brand Takeover), segmentação (interesses, comportamentos, lookalike), estratégia de lances
- **Como chamar:** chame `ads-strategist` com todos os inputs acima

### Passo 2 — /tiktok-ads
- **Input:** produto + objetivo + audiência + estrutura (Passo 1) + tom
- **Output:**
  - 3-5 variações de criativo para teste (cada uma com hook diferente nos 3 primeiros segundos)
  - Copy de cada criativo: texto on-screen, narração, CTA
  - Recomendações técnicas: duração ideal, proporção, legendas, música
  - Configurações de segmentação detalhadas no TikTok Ads Manager
  - Estratégia de Spark Ads (impulsionar vídeos orgânicos que já performam)
- **Como chamar:** `/tiktok-ads` — forneça produto, objetivo, audiência e estrutura do Passo 1

### Passo 3 — short-video-creator (para produção de criativos nativos)
- **Input:** hooks definidos no Passo 2 + produto + tom
- **Output:** roteiros de vídeo nativos do TikTok (não parecem anúncio) para os 3-5 criativos
- **Como chamar:** chame `short-video-creator` pedindo roteiros de vídeo no estilo TikTok nativo para cada hook

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `estrutura-tiktok-ads.md` | Estrutura da campanha: objetivo, tipo, segmentação, lances |
| `criativos-tiktok.md` | 3-5 variações de criativo com hook, copy, narração e CTA |
| `roteiros-nativos.md` | Roteiros de vídeo estilo TikTok orgânico para os criativos |

## Ativa próximas esteiras

- **E5** (Performance) → auditoria das campanhas após período de veiculação
- **C2** (Short Video) → transformar os melhores criativos em conteúdo orgânico
- **E4** (Landing Page) → criar ou otimizar a página de destino
