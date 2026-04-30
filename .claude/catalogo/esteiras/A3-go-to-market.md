# Esteira A3 — Go-to-Market de Produto

## Quando usar

- Lançamento de produto, curso, serviço ou feature nova
- Expansão para novo canal ou mercado
- Relançamento de produto existente com novo posicionamento

## Pré-requisitos

- **A1** (ICP & Persona)
- **A2** (Posicionamento de Marca)

## Entrada esperada

- Produto a lançar com descrição completa
- Data alvo de lançamento (ou horizonte em semanas)
- Budget disponível para ads (pode ser zero)
- Canais digitais disponíveis (site, redes sociais, email list)
- Prova social disponível (depoimentos, resultados de beta, clientes anteriores)

## Sequência de execução

### Passo 1 — /produto-gtm
- **Input:** produto + ICP + posicionamento + data de lançamento + budget
- **Output:** plano GTM estruturado em 4 fases (pré-lançamento, lançamento, pós-lançamento, avaliação) com canais, mensagens, cronograma e KPIs por fase
- **Como chamar:** `/produto-gtm` — forneça todos os inputs acima

### Passo 2 — /landing-page
- **Input:** produto + posicionamento + proposta de valor + prova social disponível
- **Output:** copy completo da landing page de lançamento (hero, benefícios, prova social, objeções, FAQ, CTA)
- **Como chamar:** `/landing-page` — informe produto, posicionamento e prova social

### Passo 3 — /press-release
- **Input:** dados do lançamento (produto, data, diferenciais, quotes da marca)
- **Output:** release profissional pronto para envio a veículos e compartilhamento em redes
- **Como chamar:** `/press-release` — informe todos os dados do lançamento

### Passo 4 — /content-calendar
- **Input:** cronograma do GTM (do Passo 1) + pilares de mensagem
- **Output:** calendário editorial de 30 dias pré e pós-lançamento com posts por canal
- **Como chamar:** `/content-calendar` — informe fases do GTM, canais e frequência desejada

### Passo 5 — ads-strategist (se houver budget)
- **Input:** landing page + ICP + budget estimado por canal
- **Output:** estrutura de campanhas pagas para o lançamento (campanha de aquecimento + campanha de conversão)
- **Como chamar:** chame o agente `ads-strategist` informando objetivo, público e budget

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `gtm-plan.md` | Plano completo em 4 fases com cronograma e KPIs |
| `landing-lancamento.md` | Copy completo da landing page |
| `release.md` | Comunicado de imprensa pronto |
| `calendario-lancamento.md` | Calendário editorial 30 dias |
| `ads-brief.md` | Estrutura de campanhas pagas (se aplicável) |

## Ativa próximas esteiras

- **B1** (Editorial) → continua o calendário após o lançamento
- **C1** (YouTube Longo) → vídeo de apresentação do produto
- **C2** (Short Video) → teasers e conteúdo de lançamento para redes
- **E1-E3** (Ads) → campanhas completas baseadas no brief
- **F1** (Relatório) → mede resultado do lançamento
