# Esteira E4 — Landing Page de Conversão

## Quando usar

- Página de destino para campanha de ads
- Página de captura de leads (lead magnet, newsletter, webinar)
- Página de vendas de produto ou serviço
- Página de lançamento de produto

## Pré-requisitos

- **A1** (ICP & Persona) — para quem a página fala
- **A2** (Posicionamento) — proposta de valor e diferenciação

## Entrada esperada

- Produto/serviço/oferta com descrição completa
- ICP e personas (output A1)
- Posicionamento e proposta de valor (output A2)
- Objetivo da página (lead, venda direta, inscrição, pré-venda)
- Prova social disponível (depoimentos, números, logos de clientes)
- CTA principal (o que o visitante deve fazer)

## Sequência de execução

### Passo 1 — /posicionamento (se não existir)
- **Só execute se A2 não foi feita antes**
- **Input:** produto + ICP
- **Output:** proposta de valor base para a página
- **Como chamar:** `/posicionamento` — forneça produto e ICP

### Passo 2 — /landing-page
- **Input:** produto + posicionamento + ICP + prova social + CTA
- **Output:** copy completo da landing page com todos os blocos:
  - Hero section (headline + subheadline + CTA)
  - Seção de problema (agitação da dor)
  - Seção de solução (sua oferta como resposta)
  - Benefícios (3-5 benefícios com ícone sugerido)
  - Como funciona (3 passos simples)
  - Prova social (depoimentos, números, logos)
  - Objeções e respostas (FAQ)
  - CTA final + garantia (se houver)
- **Como chamar:** `/landing-page` — forneça todos os inputs

### Passo 3 — /copy-anatomy
- **Input:** headline principal da landing page
- **Output:** 5 variações de headline para A/B test, classificadas por abordagem (medo, ganho, curiosidade, resultado, identidade)
- **Como chamar:** `/copy-anatomy` — peça 5 variações de headline com diferentes abordagens

### Passo 4 — growth-hacker
- **Input:** landing page completa + métricas de conversão (se já existir baseline)
- **Output:** hipóteses de otimização com ICE score:
  - O que testar primeiro (headline, CTA, prova social, formulário)
  - Elementos de CRO prioritários
  - Ferramentas gratuitas para heatmap e gravação (Clarity, Hotjar Free)
- **Como chamar:** chame o agente `growth-hacker` pedindo hipóteses de CRO

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `landing-page.md` | Copy completo de todos os blocos |
| `variacoes-headline.md` | 5 variações de headline para teste |
| `hipoteses-cro.md` | Hipóteses de otimização com ICE score |

## Ativa próximas esteiras

- **E1** (Meta Ads) → landing page pronta para receber tráfego pago
- **E2** (YouTube Ads) → landing page como destino dos anúncios
- **E3** (TikTok Ads) → landing page como destino dos anúncios
- **F3** (Experimento) → testar hipóteses de CRO com tráfego real
