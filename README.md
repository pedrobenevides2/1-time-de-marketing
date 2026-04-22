# Time de Marketing

Equipe de agentes e skills de marketing construída sobre o modelo OpenSquad,
com inspiração em agency-agents, marketingagentskills e awesome-claude-code-subagents.

---

## Organograma

```
                    ┌─────────────────────────────┐
                    │    DIRETOR DE MARKETING      │
                    │     (Orchestrator Agent)     │
                    │  Estratégia · Coordenação    │
                    └──────────────┬──────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
┌─────────▼──────────┐  ┌─────────▼──────────┐  ┌─────────▼──────────┐
│  CRIADOR DE        │  │  SEO SPECIALIST     │  │  GROWTH HACKER     │
│  CONTEÚDO          │  │  (Agent)            │  │  (Agent)           │
│  (Agent)           │  │                     │  │                    │
│ Posts · Artigos    │  │ SEO Técnico         │  │ Experimentos       │
│ Roteiros · Emails  │  │ Keywords · Links    │  │ A/B Tests · Funil  │
└────────────────────┘  └─────────────────────┘  └────────────────────┘
```

---

## Skills disponíveis (otimizadas para tokens)

```
ESTRATÉGIA                    CONTEÚDO & COPY
├── /icp-persona              ├── /copy-anatomy
├── /posicionamento           ├── /press-release
└── /produto-gtm              └── /landing-page

CANAIS DIGITAIS               PERFORMANCE
├── /linkedin-creator         ├── /performance-marketing
├── /instagram-publisher      └── /seo-audit
```

---

## Quando usar agente vs skill

| Situação | Use |
|---|---|
| Campanha completa do zero | `diretor-de-marketing` (orquestra tudo) |
| Criar conteúdo para múltiplas plataformas | `criador-de-conteudo` |
| Auditoria técnica completa de SEO | `seo-specialist` |
| Desenhar experimento de crescimento | `growth-hacker` |
| Criar personas de cliente | `/icp-persona` (skill) |
| Definir posicionamento | `/posicionamento` (skill) |
| Escrever um post para LinkedIn | `/linkedin-creator` (skill) |
| Escrever legenda de Instagram | `/instagram-publisher` (skill) |
| Copy de landing page | `/landing-page` (skill) |
| Press release | `/press-release` (skill) |
| Checklist de SEO on-page | `/seo-audit` (skill) |
| Plano de lançamento de produto | `/produto-gtm` (skill) |
| Estruturar copy persuasivo | `/copy-anatomy` (skill) |
| Planejar campanha de anúncios | `/performance-marketing` (skill) |

---

## Fluxo padrão de campanha

```
1. /icp-persona          → quem é o público
2. /posicionamento       → qual a mensagem central
3. criador-de-conteudo   → produção multi-canal
4. /copy-anatomy         → textos de conversão
5. /landing-page         → página de destino
6. /performance-marketing → anúncios pagos
7. seo-specialist        → tráfego orgânico
8. growth-hacker         → experimentos e otimização
```

---

## Fontes e inspirações

- [OpenSquad](https://github.com/renatoasse/opensquad) — modelo principal de squads
- [marketingagentskills](https://github.com/realjaymes/marketingagentskills) — estrutura de skills com referências
- [agency-agents](https://github.com/msitarzewski/agency-agents) — definições de agentes especializados
- [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) — padrão de subagentes
