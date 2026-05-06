# Catálogo de Serviços — Time de Marketing Digital

Referência rápida para o meta-orquestrador selecionar esteiras. Cada serviço tem ID único, pré-requisitos e tempo estimado de execução (em prompts/rodadas).

---

## Categoria A — Fundação Estratégica

| ID | Serviço | Entregável | Pré-requisito | Tempo |
|----|---------|-----------|---------------|-------|
| A1 | ICP & Persona | ICP.md + personas.md + jornada visual | nenhum | curto |
| A2 | Posicionamento de Marca | posicionamento.md + copy-banco.md | A1 | curto |
| A3 | Go-to-Market de Produto | gtm-plan.md + landing.md + release.md + calendário | A1 + A2 | médio |

> A1 e A2 são pré-requisitos de quase tudo. Se não existirem, ative-os primeiro.

---

## Categoria B — Conteúdo Orgânico

| ID | Serviço | Entregável | Pré-requisito | Tempo |
|----|---------|-----------|---------------|-------|
| B1 | Estratégia Editorial | pilares.md + calendário 30d + fluxo repurposing | A1 + A2 | médio |
| B2 | Blog & SEO | artigo SEO 1.500-3.000 palavras + derivações | A1 + B1 | médio |
| B3 | Conteúdo Rico | ebook ou white paper ou case study + landing captura | A1 + A2 | longo |
| B4 | Podcast & Webinar | roteiro de episódio completo | A1 + B1 | curto |
| B5 | Infográfico | briefing visual completo para Canva | A1 | curto |

---

## Categoria C — Vídeo

| ID | Serviço | Entregável | Pré-requisito | Tempo |
|----|---------|-----------|---------------|-------|
| C1 | Vídeo Longo (YouTube) | roteiro + metadados + thumbnail brief | A1 + A2 | médio |
| C2 | Short Video (Reels/TikTok/Shorts) | 3-5 roteiros curtos + plano repurposing | A1 | médio |
| C3 | Auditoria de Canal YouTube | relatório de performance + recomendações | nenhum | médio |

---

## Categoria D — Social Media

| ID | Serviço | Entregável | Pré-requisito | Tempo |
|----|---------|-----------|---------------|-------|
| D1 | Gestão Multi-plataforma | estratégia + calendário + banco de copy + playbook engajamento | A1 + A2 + B1 | longo |
| D2 | Conteúdo Instagram | legenda + carrossel + roteiro Reels | A1 | curto |
| D3 | Conteúdo LinkedIn | post + carrossel + artigo | A1 | curto |
| D4 | Conteúdo Facebook | posts + estratégia grupos | A1 | curto |
| D5 | Outreach de Influenciadores | lista priorizada por tier + proposta | A1 + A2 | médio |
| D6 | Engajamento de Comunidade | templates de resposta + playbook de crise | A1 | curto |

---

## Categoria E — Aquisição Paga

| ID | Serviço | Entregável | Pré-requisito | Tempo |
|----|---------|-----------|---------------|-------|
| E1 | Campanha Meta Ads | estrutura + copy + plano A/B | A1 + A2 + E4 | médio |
| E2 | Campanha YouTube Ads | script 5s + segmentação + checklist | A1 + A2 | médio |
| E3 | Campanha TikTok Ads | estrutura + criativos + configurações | A1 + A2 | médio |
| E4 | Landing Page | copy completo + variações headline | A1 + A2 | médio |
| E5 | Playbook de Performance | auditoria + otimização de campanhas ativas | E1 ou E2 ou E3 | médio |

---

## Categoria F — Analytics & Growth

| ID | Serviço | Entregável | Pré-requisito | Tempo |
|----|---------|-----------|---------------|-------|
| F1 | Relatório Mensal | dashboard consolidado + hipóteses de crescimento | nenhum | médio |
| F2 | Auditoria SEO | relatório técnico + plano de ação priorizado | nenhum | médio |
| F3 | Experimento de Crescimento | hipóteses ICE + plano de teste + relatório resultado | F1 | médio |
| F4 | Inteligência Competitiva | relatório de concorrentes via scraping | A1 | curto |

---

## Categoria G — Inteligência Estratégica

| ID | Serviço | Entregável | Pré-requisito | Tempo |
|----|---------|-----------|---------------|-------|
| G1 | Inteligência de Mercado | achados-pesquisa.md + deck-executivo.md + plano-acoes.md + 3 planilhas operacionais + fluxograma.png | nenhum | longo |

> G1 é esteira de entrada — pode preceder A1 e A2 e alimenta todo o grafo com base em dados reais de pesquisa.

---

## Grafo de Dependências (resumo)

```
G1 (Inteligência de Mercado) ────────────────────────► A1, A2, B1, E1-E3, F4
A1 (ICP) ─────────────────────────────────────────────► tudo
A2 (Posicionamento) ──────────────────────────────────► A3, B1, B3, D1, D5, E1-E4
A3 (GTM) ─────────────────────────────────────────────► campanhas de lançamento
B1 (Editorial) ───────────────────────────────────────► B2, B4, D1
C1 (YouTube Longo) ───────────────────────────────────► C2 (repurposing)
E4 (Landing Page) ────────────────────────────────────► E1, E2, E3
F1 (Relatório) ───────────────────────────────────────► F3
```

---

## Legenda de Tempo

| Tempo | Prompts estimados |
|-------|-----------------|
| Curto | 2-3 rodadas |
| Médio | 4-6 rodadas |
| Longo | 7+ rodadas (pode envolver múltiplos agentes) |
