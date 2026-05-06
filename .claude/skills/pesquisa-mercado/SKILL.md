---
name: pesquisa-mercado
description: Lê pesquisa de mercado (qualquer formato colado ou arquivo) e extrai achados estruturados — evidências quantitativas, qualitativas, comportamentos, dores e oportunidades. Output: relatório de achados pronto para alimentar /direcionamentos-estrategicos.
allowed-tools: Read, Write
---

# Pesquisa de Mercado — Extração de Achados

## Informações necessárias

1. Conteúdo da pesquisa (cole o texto, passe o caminho do arquivo ou descreva os dados disponíveis)
2. Contexto do negócio (produto/serviço, mercado, momento — ex: "pré-lançamento", "expansão")
3. Áreas de interesse prioritárias (Vendas, Comunicação/Marketing, Branding — ou todas)
4. Período/abrangência da pesquisa (quando foi feita, amostra, metodologia se disponível)

## Template de output — achados-pesquisa.md

### Ficha técnica da pesquisa

| Campo | Dado |
|-------|------|
| Fonte / metodologia | |
| Tamanho da amostra | |
| Período de coleta | |
| Cobertura geográfica | |

### Achados quantitativos

| Dado | Valor | Implicação direta |
|------|-------|------------------|

### Achados qualitativos

| Tema | Verbatim ou resumo | Frequência/relevância |
|------|-------------------|----------------------|

### Comportamentos e jornada do consumidor

[Narrativa estruturada por etapa: descoberta → consideração → decisão → fidelização]

### Dores e barreiras identificadas

[Lista priorizada por frequência na pesquisa: alta / média / baixa]

### Oportunidades sinalizadas

[Lista com evidência direta da pesquisa para cada oportunidade]

### Lacunas da pesquisa

[O que a pesquisa não cobre e que seria relevante saber antes de gerar direcionamentos]

## Ferramentas

- `Read` — ler arquivo de pesquisa se o usuário passar caminho
- `Write` — salvar `achados-pesquisa.md` na pasta raiz do projeto
