# Esteira F3 — Experimento de Crescimento

## Quando usar

- Métricas estagnadas e sem clareza de qual alavanca mexer
- Validação de hipótese antes de investir recursos em escala
- Cultura de crescimento por dados (teste antes de decidir)
- Otimização de funil em algum ponto específico (topo, meio, fundo)

## Pré-requisitos

- **F1** (Relatório Mensal) — dados de baseline obrigatórios antes de formular hipóteses

## Entrada esperada

- Métrica que precisa melhorar (ex: taxa de conversão da landing page, CTR de e-mail, retenção)
- Baseline atual dessa métrica (do F1)
- Hipóteses já levantadas (se houver)
- Recursos disponíveis para o teste (budget, tempo, acesso técnico)
- Duração máxima do experimento

## Sequência de execução

### Passo 1 — growth-hacker
- **Input:** métrica alvo + baseline + hipóteses preliminares + recursos disponíveis
- **Output:** lista de hipóteses priorizadas pela metodologia ICE (Impact, Confidence, Ease), com score para cada uma, descrição do mecanismo causal (por que esta mudança deve melhorar a métrica) e qual evidência sustenta cada hipótese
- **Como chamar:** chame `growth-hacker` com a métrica, o baseline e as hipóteses; peça priorização ICE

### Passo 2 — growth-hacker (plano de teste)
- **Input:** hipótese de maior score (Passo 1) + recursos + duração
- **Output:** plano detalhado de A/B test ou experimento:
  - Hipótese formatada (Se [mudança], então [resultado], porque [mecanismo])
  - Variante A (controle) vs. Variante B (teste)
  - Tamanho de amostra necessário para significância estatística
  - Duração mínima do teste
  - Métricas primária e secundárias a monitorar
  - Como implementar sem código (se possível) ou lista técnica mínima
- **Como chamar:** chame `growth-hacker` novamente com a hipótese vencedora

### Passo 3 — analytics-analyst (análise de resultado)
- **Input:** dados coletados durante o experimento + plano de teste (Passo 2)
- **Output:** relatório de resultado — ganhou/perdeu/inconclusivo, magnitude do efeito, significância estatística, próximos passos (escalar, iterar, descartar)
- **Como chamar:** chame `analytics-analyst` ao fim do período de teste com os dados coletados

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `hipoteses-ice.md` | Lista priorizada de hipóteses com scores ICE e mecanismos causais |
| `plano-teste.md` | Plano detalhado do experimento: hipótese, variantes, amostra, duração, métricas |
| `relatorio-resultado.md` | Resultado do teste com análise estatística e próximos passos |

## Ativa próximas esteiras

- **F1** (Relatório) → atualizar o relatório mensal com os resultados do experimento
- **E5** (Performance) → aplicar os aprendizados nas campanhas pagas
- **B2** (Blog & SEO) → se o experimento for sobre conteúdo, implementar melhorias no blog
