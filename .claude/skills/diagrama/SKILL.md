---
name: diagrama
description: Gera diagramas, organogramas, fluxos de processo e workflows internos usando Mermaid.js (renderiza no GitHub, Notion, VSCode — grátis) e Python matplotlib para gráficos de dados. Use para mapear equipes, processos de campanha, pipelines e planejamento visual.
allowed-tools: Write, Bash(python3 *)
---

# Diagrama — Organogramas, Workflows e Processos

Gera diagramas visuais usando **Mermaid.js** (texto puro que vira imagem) e **Python** para gráficos de dados. Zero custo, zero instalação extra.

## Ferramentas gratuitas

| Ferramenta | Tipo | Renderiza em |
|-----------|------|-------------|
| **Mermaid.js** | Flowcharts, org charts, sequência, Gantt | GitHub, Notion, VSCode, Obsidian |
| **draw.io** (diagrams.net) | Qualquer diagrama visual | Web, desktop (grátis) |
| **Excalidraw** | Estilo hand-drawn | Web (excalidraw.com — grátis) |
| **Python matplotlib** | Gráficos de dados | Local (grátis) |
| **Canva Free** | Organogramas visuais | Web |

**Recomendação padrão: Mermaid.js** — escreva código, Cole no GitHub/Notion e vira diagrama automaticamente.

---

## Tipos de diagrama e quando usar

| Tipo | Use para | Sintaxe Mermaid |
|------|---------|----------------|
| Flowchart | Processos, fluxos de decisão | `flowchart TD` |
| Organograma | Times, hierarquias | `flowchart TB` com subgraphs |
| Sequência | Interações entre sistemas/pessoas | `sequenceDiagram` |
| Gantt | Cronograma de projetos | `gantt` |
| Mindmap | Brainstorming, pilares de conteúdo | `mindmap` |
| Quadrante | Priorização (ICE, 2x2) | `quadrantChart` |
| Jornada | Customer journey | `journey` |

---

## Templates prontos

### Organograma de time
```mermaid
flowchart TB
    CEO["👤 Diretor\nde Marketing"]
    CEO --> A["📊 Content\nStrategist"]
    CEO --> B["🎬 Vídeo\nSquad"]
    CEO --> C["📱 Social Media\nManager"]
    CEO --> D["📈 Ads\nStrategist"]
    CEO --> E["🔍 Analytics\nAnalyst"]

    B --> B1["YouTube\nSpecialist"]
    B --> B2["Short Video\nCreator"]

    style CEO fill:#6c63ff,color:#fff
    style A fill:#1a1d27,color:#e8eaf0
    style B fill:#1a1d27,color:#e8eaf0
```

### Fluxo de campanha
```mermaid
flowchart LR
    A([🎯 Briefing]) --> B[ICP & Persona]
    B --> C[Posicionamento]
    C --> D{Tipo de\ncampanha?}
    D -->|Orgânico| E[Calendário\nde Conteúdo]
    D -->|Pago| F[Estrutura\nde Anúncios]
    E --> G[Produção\nde Conteúdo]
    F --> G
    G --> H[Publicação]
    H --> I[Analytics\n& Otimização]
    I -->|Iterar| D
```

### Pipeline de conteúdo (repurposing)
```mermaid
flowchart TD
    A["📝 Artigo\nde Blog"] --> B["🎬 Vídeo\nYouTube"]
    B --> C["⚡ Shorts"]
    B --> D["🎵 TikTok"]
    B --> E["📸 Reels"]
    A --> F["📧 Email\nNewsletter"]
    A --> G["🖼️ Carrossel\nLinkedIn"]
    A --> H["🎙️ Podcast\nEpisódio"]
```

### Gantt de lançamento
```mermaid
gantt
    title Plano de Lançamento
    dateFormat  YYYY-MM-DD
    section Pré-lançamento
    ICP & Posicionamento    :done, 2026-04-22, 3d
    Landing Page            :active, 2026-04-25, 5d
    Conteúdo pré-launch     :2026-04-28, 7d
    section Lançamento
    Dia D — publicações     :milestone, 2026-05-05, 1d
    Ads no ar               :2026-05-05, 7d
    section Pós-lançamento
    Nurturing & análise     :2026-05-12, 14d
```

### Mindmap de pilares de conteúdo
```mermaid
mindmap
  root((Marca))
    Educativo
      Tutoriais
      Dicas rápidas
      Guias completos
    Bastidores
      Processos internos
      Time e cultura
    Prova Social
      Cases de clientes
      Depoimentos
    Promoção
      Lançamentos
      Ofertas
```

### Jornada do cliente
```mermaid
journey
    title Jornada de Compra
    section Descoberta
      Vê anúncio no Instagram: 3: Cliente
      Assiste Reels: 5: Cliente
    section Consideração
      Visita o site: 4: Cliente
      Lê case study: 5: Cliente
    section Decisão
      Assiste webinar: 5: Cliente
      Solicita proposta: 4: Cliente
    section Compra
      Fecha contrato: 5: Cliente, Time
```

---

## Como gerar e entregar

1. Identifique o tipo de diagrama necessário
2. Colete as informações (times, etapas, entidades)
3. Gere o código Mermaid
4. Salve em arquivo `.md` — Cole no GitHub/Notion para renderizar
5. Para gráficos de dados: gere script Python com matplotlib

## Gráfico de dados com Python (grátis)

```python
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.facecolor'] = '#0f1117'
matplotlib.rcParams['axes.facecolor'] = '#1a1d27'
matplotlib.rcParams['text.color'] = '#e8eaf0'

canais = ['Instagram', 'YouTube', 'TikTok', 'Facebook']
engajamento = [4.2, 3.8, 7.1, 1.9]
cores = ['#6c63ff', '#00d4aa', '#f59e0b', '#3b82f6']

plt.figure(figsize=(10, 5))
plt.bar(canais, engajamento, color=cores, edgecolor='none')
plt.title('Taxa de Engajamento por Canal (%)', fontsize=14, pad=15)
plt.ylabel('Engajamento (%)')
plt.savefig('engajamento-canais.png', dpi=150, bbox_inches='tight')
print("Gráfico salvo.")
```

## Como renderizar Mermaid localmente (grátis)

```bash
# Opção 1: extensão VSCode "Markdown Preview Mermaid Support"
# Opção 2: copie o código em mermaid.live (editor online grátis)
# Opção 3: cole em bloco ```mermaid no GitHub ou Notion
```
