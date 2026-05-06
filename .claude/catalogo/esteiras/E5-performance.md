# Esteira E5 — Playbook de Performance

## Quando usar

- Campanhas pagas estão no ar mas sem resultado esperado
- Revisão quinzenal/mensal de todas as campanhas ativas
- CPA subindo, CTR caindo ou ROAS abaixo do target
- Antes de escalar budget (garantir que a base está saudável)

## Pré-requisitos

- **E1** (Meta Ads) e/ou **E2** (YouTube Ads) e/ou **E3** (TikTok Ads) — pelo menos uma campanha ativa para auditar

## Entrada esperada

- Plataformas com campanhas ativas (Meta, YouTube, TikTok)
- Métricas atuais: CPC, CPM, CTR, CPA, ROAS, taxa de conversão, frequência
- Período de análise (últimos 7, 14 ou 30 dias)
- Meta/target de cada campanha (qual CPA é aceitável, qual ROAS é o mínimo)
- Budget atual por campanha

## Sequência de execução

### Passo 1 — ads-strategist
- **Input:** plataformas + métricas + período + metas + budget
- **Output:** diagnóstico por campanha: o que está funcionando, o que está drenando budget, hipóteses de causa (criativo cansado, segmentação errada, landing page com problema, sazonalidade)
- **Como chamar:** chame `ads-strategist` com todos os dados de performance

### Passo 2 — /performance-marketing
- **Input:** diagnóstico (Passo 1) + metas + budget disponível
- **Output:**
  - Plano de ação priorizado: o que pausar, o que escalar, o que testar
  - Novas variações de criativo a testar (hooks alternativos)
  - Ajustes de segmentação e exclusões de público
  - Recomendações de landing page (se CTR está bom mas conversão é baixa)
  - Estrutura de teste A/B para as próximas 2 semanas
- **Como chamar:** `/performance-marketing` — forneça o diagnóstico e as metas

### Passo 3 — analytics-analyst
- **Input:** plano de ação (Passo 2) + dados de atribuição disponíveis
- **Output:** dashboard de acompanhamento (métricas a monitorar diariamente), alertas de performance (quando intervir), projeção de resultados com os ajustes aplicados
- **Como chamar:** chame `analytics-analyst` pedindo framework de monitoramento e projeções

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `auditoria-ads.md` | Diagnóstico por campanha: o que funciona, o que não funciona e por quê |
| `plano-otimizacao.md` | Ações priorizadas: pausar, escalar, testar — com novas variações de criativo |
| `framework-monitoramento.md` | Dashboard de métricas + alertas + projeções |

## Ativa próximas esteiras

- **F3** (Experimento de Crescimento) → formalizar as hipóteses de otimização com metodologia ICE
- **E4** (Landing Page) → se a landing page for identificada como gargalo
- **F1** (Relatório) → incluir performance de ads no relatório mensal consolidado
