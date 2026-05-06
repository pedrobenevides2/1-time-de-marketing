# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projeto

Time completo de agentes e skills de marketing digital — YouTube, Instagram, TikTok, Facebook, conteúdo longo, ads e analytics. Stack 100% gratuito.

- **GitHub:** https://github.com/pedrobenevides2/1-time-de-marketing
- **Painel:** https://pedrobenevides2.github.io/1-time-de-marketing/painel.html
- **Início:** 22/04/2026

---

## Arquitetura em Camadas

```
/estrategia-cascata  (skill — ponto de entrada para ideias vagas)
         ↓
meta-orquestrador    (agente Opus — lê catálogo, resolve dependências, gera plano cascata)
         ↓
diretor-de-marketing (agente Opus — CMO, coordena squads)
         ↓
Squads 1-5 (9 agentes especializados) + inteligencia-estrategica (Opus)
         ↓
33 Skills (outputs pontuais e padronizados)
```

**Quando usar cada camada:**
- `/estrategia-cascata` — ideia vaga, sem saber por onde começar
- `meta-orquestrador` — objetivo claro, quer o plano cascata automático
- `diretor-de-marketing` — já sabe o que quer, precisa que o time execute
- Agente direto — tarefa complexa dentro de um squad específico
- Skill direta — output padronizado e rápido

---

## Catálogo de Serviços (`.claude/catalogo/`)

Contém 27 serviços e os pipelines de execução:

```
.claude/catalogo/
├── servicos.md       ← 27 serviços com IDs (G1, A1–F4), pré-requisitos e tempo
├── README.md         ← grafo de dependências e referência de agentes/skills
├── PROGRESSO.md      ← rastreamento de implementação (sistema 100% concluído)
└── esteiras/         ← pipeline passo a passo por serviço (27 arquivos)
```

**Categorias de serviços:**

| Cat | IDs | Serviços |
|-----|-----|----------|
| G — Inteligência | G1 | Pesquisa → Direcionamentos 3×3 |
| A — Fundação | A1–A3 | ICP · Posicionamento · GTM |
| B — Conteúdo | B1–B5 | Editorial · Blog+SEO · Rico · Podcast · Infográfico |
| C — Vídeo | C1–C3 | YouTube Longo · Short Video · Auditoria Canal |
| D — Social | D1–D6 | Multi-plataforma · Instagram · LinkedIn · Facebook · Influenciadores · Comunidade |
| E — Ads | E1–E5 | Meta · YouTube · TikTok · Landing Page · Performance |
| F — Analytics | F1–F4 | Relatório · Auditoria SEO · Experimento · Inteligência Competitiva |

**Regras de dependência críticas:**
- A1 (ICP) é pré-requisito de quase tudo
- A2 (Posicionamento) deve existir antes de copy ou campanha
- E4 (Landing Page) deve existir antes de E1–E3 (Ads)
- F1 (Relatório) deve existir antes de F3 (Experimento)

---

## Agentes (12)

| Agente | Nickname | Squad | Modelo |
|--------|----------|-------|--------|
| `meta-orquestrador` | O Visionário | Meta-estratégia | claude-opus-4-7 |
| `diretor-de-marketing` | Godão | Orquestração | claude-opus-4-7 |
| `inteligencia-estrategica` | Sherlock | Inteligência | claude-opus-4-7 |
| `content-strategist` | A Narradora | Conteúdo | claude-sonnet-4-6 |
| `seo-specialist` | Google Whisper | Conteúdo | claude-sonnet-4-6 |
| `criador-de-conteudo` | A Máquina | Conteúdo | claude-sonnet-4-6 |
| `youtube-specialist` | Rei dos Plays | Vídeo | claude-sonnet-4-6 |
| `short-video-creator` | Ninja dos Reels | Vídeo | claude-sonnet-4-6 |
| `social-media-manager` | Dona das Redes | Social | claude-sonnet-4-6 |
| `ads-strategist` | Caçador de Cliques | Ads | claude-sonnet-4-6 |
| `growth-hacker` | Mago do Crescimento | Ads/Growth | claude-sonnet-4-6 |
| `analytics-analyst` | Profeta dos Números | Analytics | claude-sonnet-4-6 |

**Formato de agente** (`.claude/agents/<nome>.md`):
```yaml
---
name: nome-do-agente
description: quando usar este agente (usado pelo Claude para selecionar automaticamente)
model: claude-opus-4-7   # ou claude-sonnet-4-6
tools: Read, Write, Edit, WebSearch, WebFetch
---
# Corpo em markdown com papel, time, como orquestrar
```

---

## Skills (33)

Estratégia: `/estrategia-cascata` `/icp-persona` `/posicionamento` `/content-calendar` `/produto-gtm` `/pesquisa-mercado` `/direcionamentos-estrategicos`

Conteúdo longo: `/blog-post` `/white-paper` `/case-study` `/ebook-outline` `/webinar-script` `/podcast-script` `/infographic-brief`

Vídeo: `/video-script` `/youtube-seo` `/tiktok-strategy`

Social: `/instagram-publisher` `/linkedin-creator` `/facebook-strategy` `/community-engagement` `/influencer-outreach`

Copy: `/copy-anatomy` `/landing-page` `/press-release`

Ads: `/facebook-ads` `/youtube-ads` `/tiktok-ads` `/performance-marketing`

Analytics: `/analytics-report` `/seo-audit`

Utilidades: `/scraping` `/diagrama`

**Formato de skill** (`.claude/skills/<nome>/SKILL.md`):
```yaml
---
name: nome-da-skill
description: o que ela entrega (1 linha)
allowed-tools: Read, Write
---
# Corpo: instruções de output, seções obrigatórias, exemplos
```

---

## Painel Visual (`painel.html`)

Arquivo HTML único (~1.900 linhas) sem dependências externas além da Anthropic API e Google OAuth. Acessível via GitHub Pages.

### Estrutura interna do painel

**Dados (arrays JS):**
- `AGENTS` — 12 agentes com `{ id, nickname, name, short, emoji, color, role, skills, outputs, passesTo }`
- `STAFF` — 3 personagens fictícios (Bete das Planilhas, Seu Geraldo da TI, Fernandinho do Café) com `{ id, nickname, emoji, color, bio }`
- `ESTEIRAS` — 27 esteiras com `{ id, name, icon, color, img, desc, steps[] }`
- `CATEGORIES` — categorias G/A/B/C/D/E/F para filtros

**Estado global:**
```javascript
const State = {
  apiKey, sheetId, clientId, driveId,        // credenciais
  ga4Id, ga4Mid, gsc, saEmail,               // stack gratuito (opcionais)
  produto, icp,                               // contexto do projeto
  activeAgent, activeEsteira,                 // agente/esteira ativos
  messages, deliverables,                     // histórico e entregáveis
  sheetsToken, attachedContent,
  hiddenEsteiras: new Set(),                  // esteiras desabilitadas (persiste em localStorage)
  features: { office, sheetsAuto, compact, cache }
}
```

**Funções críticas — não renomear sem atualizar todas as referências:**

| Função | O que faz |
|--------|-----------|
| `buildOffice()` | Renderiza o org chart hierárquico no Painel 4 |
| `setAgentState(id, state, text)` | Atualiza speech bubble do agente (idle/thinking/active/done) |
| `animateIntern(fromId, toId, label)` | Anima o estagiário entre mesas após resposta da API |
| `sendMessage()` | Envia mensagem para a API, aciona estados e intern |
| `uploadToDrive(name, content)` | Faz upload de entregável para Google Drive, retorna link compartilhável |
| `saveToSheets(ctx)` | Salva linha no Sheets com 8 colunas (requer `ctx` com `{agentId, atividade, esteira, input, resposta, driveLinks}`) |
| `initSheetsHeaders()` | Cria cabeçalhos na aba "Conversas" (A1:H1) — executar só uma vez |
| `showFlowchart(id)` | Abre modal de esteira, seta `State.activeEsteira` |
| `buildProcGrid()` | Renderiza o grid de esteiras no Painel 2 |
| `zoomFlow(delta)` | Zoom no modal de fluxograma (0 = reset) |
| `openSettings()` / `saveSettings()` | Lê/salva todas as configurações do `State` no `localStorage` |

**Layout dos 4 painéis:**
```
┌─────────────────┬──────────────────────────────┐
│ Painel 1        │ Painel 2                      │
│ Controles/Chat  │ Esteiras (grid de processos)  │
├─────────────────┤                               │
│ Painel 3        │                               │
│ Chat / Mensagens│                               │
├─────────────────┴──────────────────────────────┤
│ Painel 4 — Escritório (org chart hierárquico)  │
└─────────────────────────────────────────────────┘
```

**Org chart — andares do escritório:**
- CEO: `meta-orquestrador`
- Diretoria: `diretor-de-marketing`, `inteligencia-estrategica`
- Coordenação: `content-strategist`, `ads-strategist`, `analytics-analyst` + Bete das Planilhas (STAFF)
- Especialistas: `seo-specialist`, `criador-de-conteudo`, `youtube-specialist`, `short-video-creator`, `social-media-manager`, `growth-hacker` + Seu Geraldo da TI, Fernandinho do Café (STAFF)

**Integração Google (escopo OAuth):**
- `https://www.googleapis.com/auth/spreadsheets`
- `https://www.googleapis.com/auth/drive.file`

**Sheets — aba "Conversas" (8 colunas A:H):**
Horário · Agente · Nickname · Atividade · Esteira · Input · Resposta · Entregáveis (Drive)

**Padrão de entregável detectado no texto do agente:**
```
## ENTREGÁVEL: nome-do-arquivo.md
```
O sistema extrai o nome, faz upload ao Drive, exibe link `☁ Drive` no painel.

### Como adicionar um novo agente ao painel

1. Adicionar entrada no array `AGENTS` com todos os campos incluindo `nickname` e `passesTo`
2. Adicionar o agente ao andar correto dentro de `buildOffice()` (array `floors`)
3. Adicionar `<option>` no `<select id="agent-select">` do HTML
4. Criar `.claude/agents/<nome>.md`

### Como adicionar uma nova esteira ao painel

1. Adicionar entrada no array `ESTEIRAS` com `id`, `name`, `icon`, `color`, `desc`, `steps[]`
2. Criar `.claude/catalogo/esteiras/<ID>-<nome>.md`
3. Atualizar `.claude/catalogo/servicos.md` e `.claude/catalogo/README.md`

---

## Integrações Google (`credentials/`)

Scripts Python chamados via terminal:

```bash
python credentials/ga4_report.py [dias]                    # relatório GA4 por canal
python credentials/search_console_report.py [dias] [top_n] # top keywords
```

- Service account: `marketing-agent@time-de-marketing-494122.iam.gserviceaccount.com`
- GA4 Property ID: `534288947` | Measurement ID: `G-XW2ZTK4SFP`
- Search Console: `sc-domain:4fg.com.br`
- `credentials/google-credentials.json` **não commitar** (já está no `.gitignore`)

---

## Convenções

- `localStorage` chave `mkt-cfg` — todas as configurações do painel (JSON)
- `localStorage` chave `mkt-hidden` — array de IDs de esteiras desabilitadas
- Entregáveis detectados automaticamente pelo padrão `## ENTREGÁVEL: <nome>`
- `passesTo[]` no agente define para quem o estagiário se move após resposta
- `State.activeEsteira` é setado em `showFlowchart()` e usado em `saveToSheets()`
- Nicknames dos agentes são exibidos nos name-tags das mesas (não os IDs)

## .gitignore

`credentials/google-credentials.json` não deve ser commitado.
