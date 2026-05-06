# Protocolo de Uso — Time de Marketing

Guia operacional para primeiro uso e início de cada processo.

---

## 1. Primeiro Uso

### Fase 1 — Leitura obrigatória (5 min)

- [ ] `CLAUDE.md` — arquitetura do sistema, agentes, skills e convenções
- [ ] `README.md` — time completo e referência de todas as skills
- [ ] `.claude/catalogo/servicos.md` — 25 serviços com IDs, pré-requisitos e tempo estimado

### Fase 2 — Diagnóstico do ponto de partida

Responda antes de executar qualquer coisa:

| Pergunta | Sim | Não |
|---------|-----|-----|
| Tenho pesquisa de mercado disponível? | Comece pelo G1 | Pule para Fase 3 |
| ICP e personas já estão definidos? | Pode pular A1 | A1 é obrigatório antes de tudo |
| Posicionamento de marca já existe? | Pode pular A2 | A2 é obrigatório antes de copy/conteúdo/ads |
| Há landing page criada? | Pode rodar ads | E4 deve existir antes de E1, E2, E3 |

### Fase 3 — Construção das fundações (ordem obrigatória)

```
[se tiver pesquisa]  G1 → /pesquisa-mercado
                      ↓
                     A1 → /icp-persona
                      ↓
                     A2 → /posicionamento
                      ↓
                    pronto para qualquer esteira
```

Não pule esta sequência. A1 e A2 são pré-requisitos de quase tudo.

### Fase 4 — Escolha o ponto de entrada

| Situação | Ponto de entrada |
|---------|----------------|
| Ideia vaga, não sei o que preciso | `diretor-de-marketing` — peça um plano |
| Tenho pesquisa de mercado | `/pesquisa-mercado` → esteira G1 |
| Sei o serviço, quero o pipeline completo | esteira correspondente (`A1` a `F4`, `G1`) |
| Quero apenas um output rápido | `/skill-name` diretamente |
| Tarefa complexa de análise ou estratégia | Agente especializado diretamente |

---

## 2. Início de Cada Processo

Execute este protocolo antes de iniciar qualquer esteira.

### Passo 1 — Confirmar pré-requisitos

1. Abra `.claude/catalogo/esteiras/[ID-da-esteira].md`
2. Leia a seção **Pré-requisitos**
3. Verifique se os arquivos listados existem no projeto

> Se algum pré-requisito estiver faltando, rode a esteira correspondente primeiro.

### Passo 2 — Preparar os dados de entrada

1. Leia a seção **Entrada esperada** da esteira
2. Reúna todos os dados antes de chamar o primeiro passo
3. Defina o nome do projeto ou pasta onde os entregáveis serão salvos

### Passo 3 — Escolher o ponto de entrada correto

| O que tenho | Como entrar |
|-------------|-------------|
| Dados brutos, briefing ou ideia | Passo 1 da esteira |
| Output de uma esteira anterior | Passo subsequente da nova esteira |
| Só quero um entregável específico | Skill correspondente diretamente |

### Passo 4 — Executar e acompanhar

- Siga a sequência numerada da esteira — não pule passos
- Aguarde cada passo concluir antes de avançar
- No nível operacional (Passo 3 do G1, por exemplo), permita múltiplas rodadas — é o passo mais longo e detalhado
- Se o agente pedir dados que você não tem, informe explicitamente para que ele sinalize lacunas em vez de inventar

---

## 3. Guia de Decisão — Skill vs Agente vs Esteira

| Situação | Use |
|---------|-----|
| Output pontual e padronizado (post, script, relatório) | `/skill` diretamente |
| Tarefa com raciocínio multi-etapa (análise, planejamento) | Agente diretamente |
| Pipeline completo com múltiplas entregas sequenciais | Esteira (todos os passos) |
| Campanha completa ou ideia estratégica sem destino claro | `diretor-de-marketing` |
| Pesquisa de mercado para transformar em ação | `inteligencia-estrategica` ou `/pesquisa-mercado` |

**Regra prática:**
- 1 output → `/skill`
- 1 tarefa complexa → agente
- 1 pipeline de entregáveis → esteira

---

## 4. Referência Rápida

### Skills de entrada (sem pré-requisito)

```
/pesquisa-mercado       Pesquisa → achados estruturados (entrada da esteira G1)
/icp-persona            ICP + buyer personas (entrada da esteira A1)
/posicionamento         Posicionamento + mensagem central (entrada da esteira A2)
/seo-audit              Auditoria SEO de qualquer página
/scraping               Coleta de dados de concorrentes e tendências
/analytics-report       Relatório de performance (requer acesso GA4/Search Console)
```

### Sequência de fundação para projetos novos

```
G1 → A1 → A2 → B1 → [específico por objetivo]
```

### Skills de produção (requerem A1 como base)

```
/blog-post              /video-script           /youtube-seo
/instagram-publisher    /linkedin-creator       /facebook-strategy
/copy-anatomy           /landing-page           /press-release
/facebook-ads           /youtube-ads            /tiktok-ads
/content-calendar       /produto-gtm            /tiktok-strategy
/white-paper            /case-study             /ebook-outline
/webinar-script         /podcast-script         /infographic-brief
/performance-marketing  /influencer-outreach    /community-engagement
/diagrama
```

### Agentes e quando chamar cada um

| Agente | Quando chamar |
|--------|--------------|
| `inteligencia-estrategica` | Tem pesquisa de mercado e precisa de direcionamentos |
| `diretor-de-marketing` | Campanha completa, coordenação de múltiplos squads |
| `content-strategist` | Definir pilares editoriais e calendário de médio prazo |
| `youtube-specialist` | SEO YouTube, thumbnails, estratégia de retenção |
| `short-video-creator` | Estratégia e roteiros TikTok, Reels, Shorts |
| `social-media-manager` | Estratégia multi-plataforma, engajamento |
| `ads-strategist` | Estruturar campanhas Meta, YouTube ou TikTok Ads |
| `analytics-analyst` | Relatórios GA4, insights e hipóteses de crescimento |
| `seo-specialist` | SEO técnico, auditoria e estratégia orgânica |
| `criador-de-conteudo` | Produção de conteúdo multi-formato |
| `growth-hacker` | Experimentos A/B, funil, hipóteses de crescimento |

---

## 5. Mapa do Sistema

```
PROTOCOLO.md                       ← este arquivo (leia primeiro)
CLAUDE.md                          ← arquitetura completa e convenções
README.md                          ← time, skills e stack gratuito

.claude/
├── catalogo/
│   ├── servicos.md                ← 25 serviços (IDs G1, A1-F4) com pré-requisitos
│   ├── README.md                  ← índice de esteiras + referência rápida
│   ├── PROGRESSO.md               ← status de implementação do sistema
│   └── esteiras/                  ← passo a passo de cada pipeline
├── agents/                        ← 11 agentes (definições e responsabilidades)
└── skills/                        ← 30+ skills (templates de output)

credentials/                       ← scripts de integração Google (GA4, Search Console)
imagem/                            ← fluxogramas e diagramas gerados
```

---

## 6. Grafo de Dependências Simplificado

```
G1 (pesquisa) ──────────────────────────► A1, A2, B1, E1-E3, F4
                                           │
A1 (ICP) ──────────────────────────────► tudo
                                           │
A2 (posicionamento) ───────────────────► copy, conteúdo, ads, branding
                                           │
B1 (editorial) ────────────────────────► B2, B4, D1
                                           │
E4 (landing page) ─────────────────────► E1, E2, E3 (ads só depois)
                                           │
F1 (relatório) ────────────────────────► F3 (experimento)
```

**Regra de ouro:** nunca rode ads sem landing page. Nunca crie conteúdo sem ICP e posicionamento.
