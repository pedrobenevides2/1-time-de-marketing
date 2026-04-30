# Esteira C1 — Vídeo Longo (YouTube)

## Quando usar

- Produção de vídeo para YouTube (educativo, tutorial, case, review)
- Primeiro vídeo do canal (vídeo de apresentação)
- Vídeo de pilar que vai gerar repurposing em shorts
- Conteúdo de maior profundidade que artigo de blog

## Pré-requisitos

- **A1** (ICP & Persona) — para definir tom, linguagem e formato
- **A2** (Posicionamento) — para manter coerência de mensagem

## Entrada esperada

- Tópico ou palavra-chave alvo para YouTube
- URL do canal (se existir) ou nicho do canal
- Objetivo do vídeo (educação, conversão, autoridade, SEO)
- Duração aproximada desejada (8-15 min, 15-30 min...)
- CTA do vídeo (inscrição, link na bio, compra, cadastro)

## Sequência de execução

### Passo 1 — youtube-specialist
- **Input:** tópico + canal + objetivo
- **Output:** análise SERP YouTube (concorrentes, gaps, ângulo único), estratégia de retenção (pacing, estrutura de gancho, momentos de engajamento), outline detalhado com timestamps
- **Como chamar:** chame o agente `youtube-specialist` com tópico, canal e objetivo

### Passo 2 — /video-script
- **Input:** outline do Passo 1 + ICP + CTA + duração
- **Output:** roteiro completo com:
  - Hook (primeiros 30 segundos)
  - Desenvolvimento por seções com marcações de câmera
  - Momentos de engajamento (pedido de like/comentário)
  - CTA final
  - Sugestões de B-roll e edição
- **Como chamar:** `/video-script` — informe outline, ICP, CTA e duração

### Passo 3 — /youtube-seo
- **Input:** roteiro + tópico + canal
- **Output:** pacote completo de metadados:
  - Título (até 60 caracteres, keyword na frente)
  - Descrição otimizada (1ª linha + links + timestamps + hashtags)
  - Tags (10-15 tags)
  - Hashtags (3-5)
  - Capítulos com timestamps
  - 3 opções de título para A/B test
- **Como chamar:** `/youtube-seo` — forneça roteiro e tópico

### Passo 4 — youtube-specialist
- **Input:** título finalizado + proposta de valor do vídeo
- **Output:** brief completo de thumbnail:
  - Composição (elementos, hierarquia visual)
  - Expressão facial recomendada
  - Texto (até 4 palavras impactantes)
  - Cores e estilo
  - Referências visuais de thumbnails de sucesso no nicho
- **Como chamar:** chame o agente `youtube-specialist` pedindo brief de thumbnail

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `roteiro.md` | Roteiro completo com marcações de câmera e edição |
| `metadados-youtube.md` | Título, descrição, tags, hashtags, capítulos |
| `thumbnail-brief.md` | Brief completo para criação no Canva |

## Ativa próximas esteiras

- **C2** (Short Video) → extrair 3-5 cortes do vídeo para TikTok/Reels/Shorts
- **B2** (Blog+SEO) → transformar roteiro em artigo de blog (repurposing)
- **D2** (Instagram) → criar carrossel com os principais insights do vídeo
- **D3** (LinkedIn) → post executivo baseado no tema do vídeo
