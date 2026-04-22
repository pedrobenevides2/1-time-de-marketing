---
name: facebook-ads
description: Estrutura campanhas de Meta Ads (Facebook + Instagram) — objetivos, públicos, criativos e copy. Usa Meta Ads Manager nativo (gratuito). Zero custo de ferramenta externa.
---
# Facebook / Meta Ads

## Estrutura de campanha

```
CAMPANHA → Objetivo
  └── CONJUNTO → Público + Orçamento + Período
        └── ANÚNCIO → Criativo + Copy + CTA
```

## Objetivos por etapa do funil

| Etapa | Objetivo no Meta | Quando usar |
|-------|-----------------|------------|
| Topo | Alcance / Awareness | Marca nova, lançamento |
| Meio | Tráfego / Engajamento / Visualizações | Aquecer audiência |
| Fundo | Conversões / Leads / Vendas | ROI direto |

## Públicos (do mais quente ao mais frio)

1. **Remarketing**: visitantes do site, engajamento no perfil, lista de clientes
2. **Lookalike**: similar aos melhores clientes (1-3%)
3. **Interesse**: segmentação por comportamento e interesse
4. **Amplo**: sem segmentação — deixe o algoritmo otimizar (funciona com Pixel maduro)

## Copy para Meta Ads

```
LINHA 1 (texto principal — primeiras 125 chars):
[Hook direto — dor, dado ou benefício]

LINHA 2-4:
[Desenvolvimento — o que é, para quem, como funciona]

LINHA 5:
[CTA — ação específica + urgência se real]

HEADLINE (abaixo da imagem, 27 chars):
[Benefício principal ou oferta]

DESCRIÇÃO (opcional, 27 chars):
[Reforço do CTA ou proposta de valor]
```

## Criativos que convertem (Canva Free + CapCut)

| Formato | CTR médio | Melhor para |
|---------|----------|------------|
| Vídeo 15-30s | Alto | Awareness + conversão |
| Carrossel | Médio-alto | Produtos, features, steps |
| Imagem estática | Médio | Ofertas diretas |
| Stories 9:16 | Alto | Remarketing |

## Orçamento mínimo para teste

- Por conjunto de anúncios: R$30-50/dia (mínimo para o algoritmo aprender)
- Teste 3-5 criativos por conjunto simultaneamente
- Aguarde 7 dias antes de otimizar (fase de aprendizado)

## Checklist de lançamento

- [ ] Pixel instalado e eventos configurados no GA4
- [ ] UTM em todos os links
- [ ] Clientes existentes excluídos do público
- [ ] Lookalike criado a partir da lista de clientes
- [ ] Criativos testados no Ad Preview
- [ ] Política de publicidade revisada (evitar rejeição)
