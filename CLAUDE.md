# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projeto

Time completo de agentes e skills de marketing digital — YouTube, Instagram, TikTok, Facebook, conteúdo longo, ads e analytics. Stack 100% gratuito.

- **GitHub:** https://github.com/pedrobenevides2/1-time-de-marketing
- **Início:** 22/04/2026

## Arquitetura em Camadas

```
/estrategia-cascata (skill — ponto de entrada para ideias estratégicas)
         ↓
meta-orquestrador (agente Opus — transforma ideia em plano cascata)
         ↓
diretor-de-marketing (agente Opus — CMO, coordena squads)
         ↓
Squads 1-5 (10 agentes especializados)
         ↓
32 Skills (outputs pontuais e padronizados)
```

**Quando usar cada camada:**
- **`/estrategia-cascata`** — entrada de uma ideia vaga ou objetivo novo; o sistema decide quais serviços ativar
- **`meta-orquestrador`** — quando você já sabe que precisa de uma campanha completa e quer o plano cascata
- **`diretor-de-marketing`** — quando já sabe o que quer e precisa que o time execute
- **Agente especialista direto** — tarefa complexa dentro de um squad específico
- **Skill direta** — output padronizado e rápido (ex: `/blog-post`, `/youtube-seo`)

## Sistema de Esteiras (`.claude/catalogo/`)

O catálogo em `.claude/catalogo/` define os 24 serviços oferecidos e os pipelines de execução:

```
.claude/catalogo/
├── servicos.md       ← 24 serviços com IDs (A1-F4), pré-requisitos e tempo
├── README.md         ← grafo de dependências e referência de agentes/skills
├── PROGRESSO.md      ← rastreamento de implementação
└── esteiras/         ← pipeline passo a passo por serviço
```

**Categorias de serviços:**

| Cat | Serviços | IDs |
|-----|----------|-----|
| A — Fundação | ICP & Persona · Posicionamento · GTM | A1-A3 |
| B — Conteúdo | Editorial · Blog+SEO · Conteúdo Rico · Podcast · Infográfico | B1-B5 |
| C — Vídeo | YouTube Longo · Short Video · Auditoria Canal | C1-C3 |
| D — Social | Multi-plataforma · Instagram · LinkedIn · Facebook · Influenciadores · Comunidade | D1-D6 |
| E — Ads | Meta · YouTube · TikTok · Landing Page · Performance | E1-E5 |
| F — Analytics | Relatório · Auditoria SEO · Experimento · Inteligência Competitiva | F1-F4 |

**Regras de dependência críticas:**
- A1 (ICP) é pré-requisito de quase tudo
- A2 (Posicionamento) deve existir antes de qualquer copy ou campanha
- E4 (Landing Page) deve existir antes de rodar ads (E1-E3)
- F1 (Relatório) deve existir antes de F3 (Experimento)

## Agentes (10)

| Agente | Squad | Modelo |
|--------|-------|--------|
| `diretor-de-marketing` | Orquestração | claude-opus-4-7 |
| `meta-orquestrador` | Meta-estratégia | claude-opus-4-7 |
| `content-strategist` | Conteúdo | claude-sonnet-4-6 |
| `seo-specialist` | Conteúdo | claude-sonnet-4-6 |
| `criador-de-conteudo` | Conteúdo | claude-sonnet-4-6 |
| `youtube-specialist` | Vídeo | claude-sonnet-4-6 |
| `short-video-creator` | Vídeo | claude-sonnet-4-6 |
| `social-media-manager` | Social | claude-sonnet-4-6 |
| `ads-strategist` | Ads | claude-sonnet-4-6 |
| `growth-hacker` | Ads/Growth | claude-sonnet-4-6 |
| `analytics-analyst` | Analytics | claude-sonnet-4-6 |

## Skills (32)

Estratégia: `/icp-persona` `/posicionamento` `/content-calendar` `/produto-gtm`

Conteúdo longo: `/blog-post` `/white-paper` `/case-study` `/ebook-outline` `/webinar-script` `/podcast-script` `/infographic-brief`

Vídeo: `/video-script` `/youtube-seo` `/tiktok-strategy`

Social: `/instagram-publisher` `/linkedin-creator` `/facebook-strategy` `/community-engagement` `/influencer-outreach`

Copy: `/copy-anatomy` `/landing-page` `/press-release`

Ads: `/facebook-ads` `/youtube-ads` `/tiktok-ads` `/performance-marketing`

Analytics: `/analytics-report` `/seo-audit`

Utilidades: `/scraping` `/diagrama`

## Integrações Google (`credentials/`)

Scripts Python chamados via `Bash(python *)`:

```bash
python credentials/ga4_report.py [dias]                    # relatório GA4 por canal
python credentials/search_console_report.py [dias] [top_n] # top keywords
```

- Service account: `marketing-agent@time-de-marketing-494122.iam.gserviceaccount.com`
- GA4 Property ID: `534288947` | Measurement ID: `G-XW2ZTK4SFP`
- Search Console: `sc-domain:4fg.com.br`
- `credentials/google-credentials.json` não commitar (no `.gitignore`)

## Documentação Visual

- `diagramas.md` — 4 diagramas Mermaid: estrutura 3 camadas, fluxo de campanha, decisão agente/skill, repurposing. Renderiza no GitHub/Notion/VSCode.

## .gitignore

`credentials/google-credentials.json` não deve ser commitado.
