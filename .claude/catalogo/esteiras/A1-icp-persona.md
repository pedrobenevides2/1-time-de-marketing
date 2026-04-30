# Esteira A1 — ICP & Persona

## Quando usar

- Início de qualquer projeto ou campanha sem ICP definido
- Produto novo ou expansão para novo segmento de mercado
- Reposicionamento ou pivot de negócio
- Antes de criar qualquer conteúdo, copy ou campanha de ads

## Pré-requisitos

Nenhum. Esta é a esteira raiz — pode ser executada sem nada definido antes.

## Entrada esperada

- Nome do produto/serviço
- Problema que resolve
- Base de clientes atual (se houver — pode ser "zero clientes ainda")
- Concorrentes conhecidos (2-3 nomes, pode ser aproximado)
- Ticket médio ou faixa de preço esperada

## Sequência de execução

### Passo 1 — /scraping
- **Input:** lista de concorrentes + nicho de mercado
- **Output:** dados de comportamento de audiência, linguagem usada, dores recorrentes, canais dos concorrentes
- **Como chamar:** `/scraping` — informe os concorrentes e peça análise de audiência e linguagem

### Passo 2 — /icp-persona
- **Input:** briefing do produto + dados do scraping do Passo 1
- **Output:** ICP detalhado (perfil demográfico, psicográfico, comportamento de compra) + 2 personas com nome, dores, objetivos, objeções e CTAs por canal
- **Como chamar:** `/icp-persona` — forneça produto + dados coletados no passo anterior

### Passo 3 — /diagrama
- **Input:** jornada de compra das personas (extraída do Passo 2)
- **Output:** mapa visual de jornada do cliente em Mermaid (tipo `journey`) pronto para GitHub/Notion
- **Como chamar:** `/diagrama` — peça um diagrama de jornada do cliente com as etapas: descoberta, consideração, decisão, compra, fidelização

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `ICP.md` | Perfil do cliente ideal com critérios firmográficos/demográficos |
| `personas.md` | 2-3 personas detalhadas com dores, objetivos, objeções e CTAs |
| `jornada-visual.md` | Diagrama Mermaid da jornada de compra |

## Ativa próximas esteiras

- **A2** (Posicionamento) — usa o ICP como base
- **B1** (Estratégia Editorial) — usa personas para definir pilares
- **C1/C2** (Vídeo) — usa personas para definir tom e formato
- **D1-D6** (Social) — usa ICP para segmentação de plataformas
- **E1-E4** (Ads) — usa ICP para segmentação de públicos
- **F4** (Inteligência Competitiva) — expande a pesquisa de concorrentes
