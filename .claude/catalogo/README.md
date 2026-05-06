# Catálogo — Guia de Uso para o Meta-Orquestrador

Este diretório contém o catálogo de serviços e as esteiras de processo do time de marketing digital.

## Como usar este catálogo

1. Leia `servicos.md` para ver todos os 24 serviços disponíveis com IDs e pré-requisitos
2. Identifique quais serviços são necessários para a ideia estratégica do usuário
3. Leia os arquivos de esteira correspondentes em `esteiras/` para detalhar cada pipeline
4. Monte o plano cascata em blocos (respeitando dependências)

## Estrutura de Esteiras

```
esteiras/
├── G1-inteligencia-mercado.md  Inteligência — Pesquisa → Direcionamentos 3×3
├── A1-icp-persona.md           Fundação — ICP e personas
├── A2-posicionamento.md        Fundação — Posicionamento de marca
├── A3-go-to-market.md          Fundação — Plano de lançamento
├── B1-estrategia-editorial.md  Conteúdo — Pilares e calendário
├── B2-blog-seo.md              Conteúdo — Artigos SEO
├── B3-conteudo-rico.md         Conteúdo — Ebook/White Paper/Case Study
├── B4-podcast-webinar.md       Conteúdo — Roteiros de áudio/live
├── B5-infografico.md           Conteúdo — Briefing visual
├── C1-video-longo.md           Vídeo — YouTube longo
├── C2-video-curto.md           Vídeo — Reels/TikTok/Shorts
├── C3-auditoria-youtube.md     Vídeo — Auditoria de canal
├── D1-gestao-social.md         Social — Gestão multi-plataforma
├── D2-instagram.md             Social — Conteúdo Instagram
├── D3-linkedin.md              Social — Conteúdo LinkedIn
├── D4-facebook.md              Social — Conteúdo Facebook
├── D5-influenciadores.md       Social — Outreach de influenciadores
├── D6-engajamento.md           Social — Comunidade e engajamento
├── E1-meta-ads.md              Pago — Campanha Meta Ads
├── E2-youtube-ads.md           Pago — Campanha YouTube Ads
├── E3-tiktok-ads.md            Pago — Campanha TikTok Ads
├── E4-landing-page.md          Pago — Landing page de conversão
├── E5-performance.md           Pago — Playbook de performance
├── F1-relatorio.md             Analytics — Relatório mensal
├── F2-auditoria-seo.md         Analytics — Auditoria SEO
├── F3-experimento.md           Analytics — Experimento de crescimento
└── F4-inteligencia.md          Analytics — Inteligência competitiva
```

## Regras de Dependência

- **A1 sempre primeiro** se ICP não existir. É pré-requisito de quase tudo.
- **A2 antes de mensagem** — qualquer serviço que gere copy precisa de posicionamento definido.
- **B1 antes de calendário** — não agende sem pilares editoriais definidos.
- **E4 antes de Ads** — não rode tráfego pago sem landing page pronta.
- **F1 antes de F3** — não crie hipóteses de crescimento sem dados de baseline.

## Formato dos Arquivos de Esteira

Cada arquivo segue esta estrutura:

```markdown
# Esteira [ID] — [Nome]
## Quando usar
## Pré-requisitos
## Entrada esperada
## Sequência de execução
### Passo N — AGENTE ou /skill
- Input / Output / Como chamar
## Entregáveis finais
## Ativa próximas esteiras
```

## Agentes disponíveis (referência rápida)

| Agente | Squad | Modelo |
|--------|-------|--------|
| `inteligencia-estrategica` | Inteligência | opus-4-7 |
| `diretor-de-marketing` | Orquestração | opus-4-7 |
| `content-strategist` | Conteúdo | sonnet-4-6 |
| `seo-specialist` | Conteúdo | sonnet-4-6 |
| `criador-de-conteudo` | Conteúdo | sonnet-4-6 |
| `youtube-specialist` | Vídeo | sonnet-4-6 |
| `short-video-creator` | Vídeo | sonnet-4-6 |
| `social-media-manager` | Social | sonnet-4-6 |
| `ads-strategist` | Ads | sonnet-4-6 |
| `growth-hacker` | Ads/Growth | sonnet-4-6 |
| `analytics-analyst` | Analytics | sonnet-4-6 |

## Skills disponíveis (referência rápida)

`/pesquisa-mercado` `/direcionamentos-estrategicos`  
`/icp-persona` `/posicionamento` `/content-calendar` `/produto-gtm`  
`/blog-post` `/white-paper` `/case-study` `/ebook-outline` `/webinar-script` `/podcast-script` `/infographic-brief`  
`/video-script` `/youtube-seo` `/tiktok-strategy`  
`/instagram-publisher` `/linkedin-creator` `/facebook-strategy` `/community-engagement` `/influencer-outreach`  
`/copy-anatomy` `/landing-page` `/press-release`  
`/facebook-ads` `/youtube-ads` `/tiktok-ads` `/performance-marketing`  
`/analytics-report` `/seo-audit`  
`/scraping` `/diagrama`
