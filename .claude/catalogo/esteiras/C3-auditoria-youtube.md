# Esteira C3 — Auditoria de Canal YouTube

## Quando usar

- Canal sem crescimento consistente há mais de 3 meses
- Vídeos com boa produção mas baixa performance (CTR ou retenção ruins)
- Antes de relançar ou reposicionar um canal existente
- Diagnóstico de canal recém-criado para evitar erros estruturais

## Pré-requisitos

Nenhum — pode ser executada com um canal existente ou como pesquisa pré-criação.

## Entrada esperada

- URL do canal a auditar (ou de canais referência se o canal ainda não existir)
- Acesso ao YouTube Studio (dados de analytics: impressões, CTR, retenção média, top vídeos)
- Nicho do canal e objetivo (monetização, leads, autoridade, suporte a produto)
- Principais concorrentes ou referências no YouTube (2-3 canais)

## Sequência de execução

### Passo 1 — youtube-specialist
- **Input:** URL do canal + dados do YouTube Studio + nicho + objetivo + canais de referência
- **Output:** diagnóstico completo:
  - **Thumbnails:** padrão visual, legibilidade, consistência de identidade
  - **Títulos:** uso de keywords, comprimento, clareza vs. curiosidade
  - **Descrições:** SEO, links, timestamps
  - **CTR médio** vs. benchmark do nicho
  - **Retenção média** vs. benchmark
  - **Consistência de publicação:** frequência e regularidade
  - **Top 3 vídeos** — o que funcionou e por quê
  - **Bottom 3 vídeos** — o que não funcionou e por quê
- **Como chamar:** chame `youtube-specialist` com todos os dados; peça diagnóstico completo

### Passo 2 — /seo-audit (adaptado para YouTube)
- **Input:** 5-10 vídeos do canal + palavras-chave alvo + análise do Passo 1
- **Output:** auditoria de SEO nos vídeos: gaps de keyword, tags subutilizadas, descrições incompletas, capítulos ausentes, hashtags não usadas, oportunidades de thumbnail A/B test
- **Como chamar:** `/seo-audit` — informe que é para YouTube e forneça os vídeos e keywords

### Passo 3 — youtube-specialist (plano de ação)
- **Input:** diagnóstico (Passo 1) + auditoria SEO (Passo 2) + recursos disponíveis
- **Output:** plano de ação em 3 fases:
  - **Fase 1 (Quick Wins, 1-2 semanas):** atualizar thumbnails e títulos dos top vídeos, corrigir descrições, adicionar capítulos
  - **Fase 2 (1-3 meses):** reposicionar canal se necessário, nova série de vídeos no nicho certo, frequência ideal
  - **Fase 3 (3-6 meses):** estratégia de keywords de longo prazo, colaborações para crescimento
- **Como chamar:** chame `youtube-specialist` pedindo plano de ação em 3 fases

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `relatorio-canal.md` | Diagnóstico completo: CTR, retenção, thumbnails, títulos, consistência |
| `auditoria-seo-youtube.md` | SEO dos vídeos: gaps de keyword, descrições, tags e capítulos |
| `plano-otimizacao-canal.md` | Plano de ação em 3 fases (quick wins, médio e longo prazo) |

## Ativa próximas esteiras

- **C1** (Vídeo Longo) → produzir os próximos vídeos já com as correções aplicadas
- **C2** (Short Video) → criar Shorts dos vídeos existentes para atrair novo público
- **F1** (Relatório) → incluir métricas do canal no relatório mensal consolidado
