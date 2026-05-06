# Esteira F2 — Auditoria SEO

## Quando usar

- Site novo sendo otimizado pela primeira vez
- Queda de tráfego orgânico sem causa aparente
- Antes de uma estratégia de blog/conteúdo (para saber o ponto de partida)
- Revisão semestral de SEO on-page e técnico

## Pré-requisitos

Nenhum — pode ser executada em qualquer momento, sem dependências.

## Entrada esperada

- URL do site ou páginas específicas a auditar
- Palavras-chave principais que a marca quer rankear
- Acesso ao Google Search Console (se disponível — cole os dados de impressões e cliques)
- Principais concorrentes orgânicos (2-3 URLs)
- Objetivo do site: geração de leads, e-commerce, autoridade, blog

## Sequência de execução

### Passo 1 — seo-specialist
- **Input:** URL + palavras-chave + concorrentes + objetivo
- **Output:** análise inicial de: autoridade do domínio (estimada), gap de palavras-chave vs. concorrentes, velocidade de carregamento perceptível, estrutura de URLs e navegação
- **Como chamar:** chame `seo-specialist` com URL, keywords e concorrentes; peça análise de gap e pontos críticos

### Passo 2 — /seo-audit
- **Input:** URL + palavras-chave + dados do Search Console (se disponível) + análise do Passo 1
- **Output:** relatório completo de auditoria on-page e técnico:
  - **Título e meta description:** presença de keyword, comprimento, duplicatas
  - **Headings (H1-H3):** estrutura, keywords, hierarquia
  - **Conteúdo:** profundidade, cobertura semântica, gaps temáticos
  - **Links internos:** distribuição de link juice, páginas órfãs
  - **Core Web Vitals:** LCP, CLS, FID (estimativa)
  - **Mobile:** usabilidade em dispositivos móveis
  - **Schema markup:** presença e oportunidades
  - **Lista priorizada de problemas:** crítico / médio / baixo
- **Como chamar:** `/seo-audit` — forneça URL, keywords e relatório inicial do Passo 1

### Passo 3 — seo-specialist (plano de ação)
- **Input:** relatório de auditoria (Passo 2) + recursos disponíveis para correção
- **Output:** plano de ação priorizado em 3 horizontes — quick wins (1-2 semanas), melhorias médio prazo (1-3 meses), projetos de longo prazo (3-6 meses)
- **Como chamar:** chame `seo-specialist` pedindo plano de ação priorizado com os 3 horizontes

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `relatorio-seo.md` | Auditoria completa: problemas técnicos, on-page e de conteúdo |
| `plano-acao-seo.md` | Quick wins + melhorias + projetos em 3 horizontes temporais |

## Ativa próximas esteiras

- **B2** (Blog & SEO) → usar os gaps de keywords para pautar novos artigos
- **F3** (Experimento) → testar hipóteses de melhoria de SEO com metodologia ICE
- **F1** (Relatório) → incluir métricas SEO no relatório mensal consolidado
