# Esteira B2 — Blog & SEO

## Quando usar

- Produção de artigo otimizado para busca orgânica
- Estratégia de cluster de conteúdo para um tópico
- Atualização de artigo existente para ranquear melhor
- Publicação periódica do calendário editorial

## Pré-requisitos

- **A1** (ICP & Persona) — para saber com quem o artigo fala
- **B1** (Estratégia Editorial) — para saber em qual pilar o artigo se encaixa

## Entrada esperada

- Palavra-chave principal ou tópico
- Intenção de busca (informacional, transacional, navegacional)
- URL do site/blog
- Pilar editorial ao qual pertence
- CTA do artigo (assinar newsletter, baixar ebook, solicitar contato...)

## Sequência de execução

### Passo 1 — seo-specialist
- **Input:** palavra-chave + URL do site + pilar editorial
- **Output:** keyword research (volume, dificuldade, variações LSI), análise de intenção de busca, mapa de cluster (artigo pilar + artigos de apoio), outline estruturado do artigo
- **Como chamar:** chame o agente `seo-specialist` com a palavra-chave, URL e objetivo

### Passo 2 — /blog-post
- **Input:** outline do Passo 1 + ICP + CTA
- **Output:** artigo completo de 1.500-3.000 palavras com H1, meta description, introdução, H2/H3, body com dados/exemplos, conclusão, links internos e externos sugeridos, alt text de imagens
- **Como chamar:** `/blog-post` — forneça outline, ICP e CTA

### Passo 3 — /seo-audit
- **Input:** artigo finalizado do Passo 2
- **Output:** checklist SEO on-page revisado (título, meta, headings, densidade de keyword, links, imagens, mobile) com ajustes prioritários
- **Como chamar:** `/seo-audit` — passe o artigo completo para revisão

### Passo 4 — criador-de-conteudo
- **Input:** artigo aprovado (Passo 3)
- **Output:** 3 derivações do artigo para distribuição:
  - Post para LinkedIn (perspectiva profissional)
  - Post para Instagram (adaptado para carrossel)
  - Email para newsletter (resumo + link)
- **Como chamar:** chame o agente `criador-de-conteudo` pedindo as 3 derivações

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `artigo-seo.md` | Artigo completo otimizado, pronto para publicar |
| `checklist-seo.md` | Revisão SEO on-page com status de cada item |
| `derivacoes-sociais.md` | Versões para LinkedIn, Instagram e email |

## Ativa próximas esteiras

- **C1** (YouTube Longo) → transformar artigo em roteiro de vídeo
- **C2** (Short Video) → extrair dicas do artigo para shorts
- **B3** (Conteúdo Rico) → expandir artigo de alto tráfego em ebook
- **F2** (Auditoria SEO) → medir performance do artigo após publicação
