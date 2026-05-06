# Esteira D1 — Gestão Multi-plataforma Social Media

## Quando usar

- Início de presença organizada nas redes sociais (sem estratégia definida)
- Revisão semestral de estratégia de social
- Quando o social está "apagando incêndio" sem planejamento
- Lançamento de produto que exige coordenação entre plataformas

## Pré-requisitos

- **A1** (ICP & Persona) — para segmentar plataformas e tom por canal
- **A2** (Posicionamento) — para garantir consistência de mensagem
- **B1** (Estratégia Editorial) — para alinhar social com os pilares de conteúdo

## Entrada esperada

- ICP e personas (output A1)
- Posicionamento e mensagem central (output A2)
- Pilares editoriais (output B1)
- Canais ativos ou desejados (Instagram, LinkedIn, Facebook, TikTok, YouTube)
- Frequência disponível por canal (posts/semana)
- Objetivo principal (awareness, leads, comunidade, vendas)

## Sequência de execução

### Passo 1 — social-media-manager
- **Input:** ICP + posicionamento + pilares + canais + frequência + objetivo
- **Output:** estratégia por plataforma (tom, formato ideal, frequência recomendada, KPIs), regras de cross-posting e adaptação de formato por canal
- **Como chamar:** chame o agente `social-media-manager` com todos os inputs acima

### Passo 2 — /content-calendar
- **Input:** estratégia por plataforma (Passo 1) + canais + frequência + pilares
- **Output:** calendário mensal multi-plataforma com data, canal, formato, pilar, título/assunto, CTA e status
- **Como chamar:** `/content-calendar` — informe os canais, frequência e pilares definidos

### Passo 3 — /community-engagement
- **Input:** plataformas ativas + persona principal + tom de voz
- **Output:** templates de resposta a comentários por tipo (elogio, dúvida, reclamação, crise), playbook de moderação, incentivos a UGC
- **Como chamar:** `/community-engagement` — informe plataformas e tom de voz da marca

### Passo 4 — /diagrama
- **Input:** estrutura de plataformas + fluxo de repurposing
- **Output:** diagrama Mermaid mostrando quais plataformas recebem conteúdo original vs. derivado
- **Como chamar:** `/diagrama` — peça diagrama de distribuição de conteúdo por plataforma

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `estrategia-social.md` | Estratégia por plataforma com tom, formato, frequência e KPIs |
| `calendario-mensal.md` | Calendário 30 dias multi-plataforma pronto para Notion/Sheets |
| `banco-copy.md` | Banco de copy por plataforma e tipo de post |
| `playbook-engajamento.md` | Templates de resposta + playbook de crise + incentivos UGC |
| `fluxo-distribuicao.md` | Diagrama de distribuição e repurposing entre plataformas |

## Ativa próximas esteiras

- **D2** (Instagram) → produção de posts, carrosséis e Reels com base no calendário
- **D3** (LinkedIn) → conteúdo executivo e profissional
- **D4** (Facebook) → estratégia de grupos e posts orgânicos
- **D5** (Influenciadores) → amplificação do conteúdo via parceiros
- **D6** (Engajamento) → playbook detalhado de gestão de comunidade
- **E1-E3** (Ads) → a estratégia orgânica informa a segmentação paga
