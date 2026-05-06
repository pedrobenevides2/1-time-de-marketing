# Esteira G1 — Inteligência de Mercado

## Quando usar

- A empresa realizou ou recebeu pesquisa de mercado e precisa transformar os dados em ação
- Antes de revisar posicionamento, mensagem ou estratégia comercial com base em dados primários
- Quando há gap entre o que a empresa acredita sobre o mercado e o que os dados mostram
- Planejamento estratégico anual ou semestral apoiado em pesquisa

## Pré-requisitos

Nenhum — esteira de entrada. Pode ser executada antes de A1 e A2, pois alimenta ambas.

## Entrada esperada

- Pesquisa de mercado em qualquer formato: texto colado, arquivo (.md, .txt, .pdf, .docx), resumo verbal ou planilha de dados
- Contexto do negócio (produto, mercado, momento)
- Áreas de foco prioritárias (Vendas, Comunicação/Marketing, Branding — ou todas as três)
- Horizonte de planejamento (ex: próximos 6 meses, ano fiscal)

## Sequência de execução

### Passo 1 — /pesquisa-mercado
- **Input:** conteúdo da pesquisa + contexto do negócio + áreas de interesse + período
- **Output:** `achados-pesquisa.md` — relatório estruturado com ficha técnica, achados quanti/quali, comportamentos, dores, oportunidades e lacunas
- **Como chamar:** `/pesquisa-mercado` — cole ou forneça a pesquisa e informe o contexto do negócio

### Passo 2 — inteligencia-estrategica (cruzamento)
- **Input:** `achados-pesquisa.md`
- **Output:** mapa de temas centrais com cruzamentos entre as três áreas; 3-5 achados mais estratégicos; sinalização de lacunas que podem bloquear direcionamentos
- **Como chamar:** chame o agente `inteligencia-estrategica` com o relatório e peça análise de cruzamento antes de gerar direcionamentos

### Passo 3 — /direcionamentos-estrategicos
- **Input:** `achados-pesquisa.md` + mapa de cruzamentos (Passo 2) + contexto estratégico da empresa
- **Output:** seis entregáveis em três níveis:
  - **Estratégico:** `deck-executivo.md` — top 5-10 direcionamentos por área, com evidência e urgência
  - **Tático:** `plano-acoes.md` — tabela com área, estratégia, objetivo, to-do, owner, prazo, KPI, status
  - **Operacional:** `operacional-vendas.md`, `operacional-comunicacao.md`, `operacional-branding.md` — detalhamento completo pronto para executar (copy, textos de site, especificações de trade, scripts de vendas, etc.)
- **Como chamar:** `/direcionamentos-estrategicos` — forneça o relatório e o mapa de cruzamentos

### Passo 4 — inteligencia-estrategica (consistência)
- **Input:** os três níveis gerados no Passo 3
- **Output:** revisão de alinhamento vertical — inconsistências sinalizadas e corrigidas; cada ação tática ancorada em um direcionamento estratégico; cada detalhe operacional derivado de uma ação tática
- **Como chamar:** chame `inteligencia-estrategica` pedindo revisão de consistência entre os três níveis

### Passo 5 — Bash(python3) via inteligencia-estrategica
- **Input:** estrutura da esteira (geração visual)
- **Output:** `imagem/G1-fluxograma.png` — fluxograma numerado da esteira como imagem
- **Como chamar:** o agente `inteligencia-estrategica` executa o script Python embutido em seu prompt

## Entregáveis finais

| Arquivo | Conteúdo |
|---------|---------|
| `achados-pesquisa.md` | Relatório estruturado: ficha técnica, achados quanti/quali, comportamentos, dores, oportunidades, lacunas |
| `deck-executivo.md` | Nível Estratégico — top 5-10 direcionamentos por área com evidência e urgência |
| `plano-acoes.md` | Nível Tático — tabela área, estratégia, to-do, owner, prazo, KPI, status (15-30 linhas) |
| `operacional-vendas.md` | Nível Operacional — detalhamento completo das ações de Vendas/Comercial |
| `operacional-comunicacao.md` | Nível Operacional — detalhamento completo das ações de Comunicação e Marketing |
| `operacional-branding.md` | Nível Operacional — detalhamento completo das ações de Branding |
| `imagem/G1-fluxograma.png` | Fluxograma numerado da esteira como imagem PNG |

## Ativa próximas esteiras

- **A1** (ICP & Persona) → achados da pesquisa alimentam ou refinam personas existentes
- **A2** (Posicionamento) → direcionamentos estratégicos de Branding alimentam diretamente A2
- **B1** (Estratégia Editorial) → direcionamentos de Comunicação viram pilares editoriais
- **E1-E3** (Ads) → achados de comportamento do consumidor alimentam segmentação de campanhas pagas
- **F4** (Inteligência Competitiva) → lacunas da pesquisa podem ser aprofundadas via scraping de concorrentes
