# Esteira B5 — Infográfico

## Quando usar

- Dados complexos que precisam de visualização para se tornarem compreensíveis
- Conteúdo altamente compartilhável para redes sociais e blog
- Comparações, rankings, processos ou estatísticas do nicho
- Suporte visual para artigos de blog ou apresentações

## Pré-requisitos

- **A1** (ICP & Persona) — para calibrar complexidade, linguagem e estética preferida pela persona

## Entrada esperada

- Tema ou dado que será visualizado
- Tipo de infográfico: processo passo a passo, comparação, estatísticas/dados, timeline, mapa, checklist
- Dados disponíveis (números, percentuais, fontes)
- Onde será publicado (Instagram, blog, LinkedIn, apresentação)
- Estilo visual referência (minimalista, colorido, técnico, descontraído)

## Sequência de execução

### Passo 1 — /scraping (se os dados precisam ser coletados)
- **Input:** tema + tipos de dados necessários + fontes relevantes
- **Output:** dados quantitativos e qualitativos coletados, estatísticas com fontes, tendências visuais do nicho
- **Como chamar:** `/scraping` — peça coleta de dados e estatísticas sobre o tema

### Passo 2 — /infographic-brief
- **Input:** tema + tipo de infográfico + dados (do Passo 1 ou fornecidos) + plataforma de publicação + estilo
- **Output:** briefing completo para design no Canva Free:
  - Hierarquia de informação (o que aparece em destaque vs. complementar)
  - Estrutura visual sugerida (número de seções, fluxo de leitura)
  - Copy de cada seção (título, texto de suporte, dados)
  - Paleta de cores, tipografia e ícones recomendados
  - Dimensões para cada plataforma (Instagram 1:1, Stories 9:16, blog 800px)
- **Como chamar:** `/infographic-brief` — forneça dados, tipo, plataforma e estilo

### Passo 3 — /diagrama (para infográficos de processo)
- **Input:** passos do processo + hierarquia definida no Passo 2
- **Output:** código Mermaid do fluxo — pode ser usado como base para o designer ou publicado diretamente no GitHub/Notion
- **Como chamar:** `/diagrama` — peça fluxo ou diagrama do processo descrito

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `brief-infografico.md` | Briefing completo: hierarquia, copy, cores, dimensões por plataforma |
| `dados-coletados.md` | Dados e estatísticas com fontes (se Passo 1 foi executado) |
| `diagrama-processo.md` | Código Mermaid do fluxo (se infográfico de processo) |

## Ativa próximas esteiras

- **D2** (Instagram) → publicar o infográfico como carrossel ou post de feed
- **D3** (LinkedIn) → publicar como carrossel ou acompanhando um post
- **B2** (Blog & SEO) → embutir o infográfico em artigo de blog sobre o mesmo tema
