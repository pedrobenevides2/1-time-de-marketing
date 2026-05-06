# Esteira E2 — Campanha YouTube Ads

## Quando usar

- Produto com potencial de demonstração em vídeo (funciona melhor que imagem estática)
- Alcance de audiência que não está nas redes sociais mas usa YouTube
- Remarketing de quem visitou o site via Google Ads
- Campanhas de awareness com budget menor que Meta Ads

## Pré-requisitos

- **A1** (ICP & Persona) — para segmentação de audiência
- **A2** (Posicionamento) — para garantir consistência de mensagem nos scripts

## Entrada esperada

- Produto ou serviço a ser anunciado
- Objetivo: awareness, consideração, conversão, remarketing
- Budget mensal estimado
- Vídeo disponível ou precisa de roteiro para gravar
- Audiência-alvo (idade, interesses, intenção de compra)
- Landing page de destino (se E4 não estiver pronto, crie antes)

## Sequência de execução

### Passo 1 — ads-strategist
- **Input:** produto + objetivo + budget + audiência + landing page
- **Output:** estrutura da campanha no Google Ads Manager: tipo de anúncio (In-Feed, TrueView In-Stream, Bumper), segmentação por interesse e intenção, lances e estratégia de bidding, configurações de frequência
- **Como chamar:** chame `ads-strategist` com todos os inputs acima

### Passo 2 — /youtube-ads
- **Input:** produto + objetivo + audiência + estrutura (Passo 1) + tom de comunicação
- **Output:**
  - Script do "gancho dos 5 segundos" (antes do botão Pular) — 3 variações
  - Script completo do anúncio (15s, 30s ou 60s conforme o formato)
  - Headline e descrição de acompanhamento (aparece ao lado do vídeo)
  - CTA e URL de destino otimizados
  - Configurações técnicas recomendadas no Google Ads
- **Como chamar:** `/youtube-ads` — forneça produto, objetivo, audiência e estrutura do Passo 1

### Passo 3 — analytics-analyst (após 7-14 dias de campanha no ar)
- **Input:** métricas da campanha (view rate, CTR, CPV, conversões)
- **Output:** análise de performance, variações de script para teste A/B, recomendações de ajuste de segmentação
- **Como chamar:** chame `analytics-analyst` com os dados de performance para otimização

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `estrutura-youtube-ads.md` | Estrutura da campanha no Google Ads: tipo, segmentação, lances |
| `scripts-youtube-ads.md` | Scripts: gancho 5s (3 variações) + anúncio completo + headline/descrição |

## Ativa próximas esteiras

- **E5** (Performance) → auditoria das campanhas após período de veiculação
- **E4** (Landing Page) → criar ou otimizar a página de destino dos anúncios
- **C1** (Vídeo Longo) → o vídeo do anúncio pode ser a versão longa do conteúdo orgânico
