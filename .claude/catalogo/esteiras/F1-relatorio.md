# Esteira F1 — Relatório Mensal

## Quando usar

- Fechamento de mês para análise de performance
- Revisão de campanha após período mínimo de 30 dias
- Relatório para cliente ou stakeholder
- Base de dados para experimentos de crescimento (F3)

## Pré-requisitos

Nenhum — pode ser executada a qualquer momento com dados disponíveis.

## Entrada esperada

- Período de análise (mês/ano ou intervalo de datas)
- Canais ativos: GA4, Search Console, YouTube, Instagram, Facebook, TikTok
- Metas definidas para o período (se houver)
- Acesso aos scripts Python de GA4 e Search Console do projeto

## Sequência de execução

### Passo 1 — analytics-analyst
- **Input:** período + canais + metas
- **Output:** coleta e interpretação dos dados brutos de cada canal:
  - GA4: sessões, usuários, canais de aquisição, conversões, bounce rate
  - Search Console: impressões, cliques, CTR, posição média, top keywords
  - YouTube: views, tempo de exibição, inscrições, CTR de thumbnail
  - Meta (Instagram/Facebook): alcance, engajamento, seguidores, posts com melhor performance
  - TikTok: views, curtidas, compartilhamentos, crescimento de seguidores
- **Como chamar:** chame o agente `analytics-analyst` com período e canais. Se GA4 estiver configurado, rode: `python credentials/ga4_report.py 30` e `python credentials/search_console_report.py 30 20`

### Passo 2 — /analytics-report
- **Input:** dados coletados pelo analytics-analyst (Passo 1)
- **Output:** relatório consolidado no template padrão:
  - Resumo executivo (3 bullets principais)
  - Performance por canal com variação mês anterior
  - Top 3 conteúdos de melhor performance
  - KPIs vs metas
  - Insights acionáveis
  - Recomendações para próximo mês
- **Como chamar:** `/analytics-report` — forneça os dados do Passo 1

### Passo 3 — growth-hacker
- **Input:** relatório consolidado (Passo 2)
- **Output:** 3 hipóteses de crescimento baseadas nos dados com ICE score (impacto, confiança, esforço) + recomendação de qual testar primeiro
- **Como chamar:** chame o agente `growth-hacker` com o relatório e peça hipóteses de crescimento para o próximo mês

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `relatorio-YYYY-MM.md` | Relatório consolidado com métricas de todos os canais |
| `hipoteses-crescimento.md` | 3 hipóteses com ICE score + priorização |

## Ativa próximas esteiras

- **F3** (Experimento) → executar a hipótese de maior ICE score
- **B2** (Blog+SEO) → criar conteúdo baseado nas keywords de maior oportunidade
- **E5** (Performance) → otimizar campanhas com base nos dados de ads
