---
name: estrategia-cascata
description: Ponto de entrada para objetivos estratégicos vagos. Coleta objetivo, público, prazo e restrições, depois aciona meta-orquestrador para montar o plano cascata completo de esteiras.
allowed-tools: Read, Write
---

# Estratégia em Cascata — Ponto de Entrada

## Informações necessárias

Antes de acionar o `meta-orquestrador`, colete as 4 informações abaixo. Se alguma já foi mencionada pelo usuário, não repita a pergunta — registre e siga.

1. **Objetivo de negócio** — o que precisa ser alcançado? (ex: lançar produto, crescer canal no YouTube, gerar leads, reposicionar marca)
2. **Público-alvo** — quem é o cliente? Se A1 (ICP & Persona) já foi executado, informe o caminho do arquivo; se não, uma descrição inicial já é suficiente
3. **Prazo** — quando o resultado precisa aparecer? (ex: 30 dias, 3 meses, data específica)
4. **Restrições** — o que limita a execução? (budget disponível, tamanho da equipe, ferramentas disponíveis, canais já ativos ou descartados)

## O que acontece depois

Com as 4 informações coletadas, acione o agente `meta-orquestrador` passando:
- Objetivo formatado
- Público / referência ao arquivo de ICP se existir
- Prazo
- Restrições

O meta-orquestrador lê o catálogo completo de esteiras, resolve as dependências e entrega `plano-cascata.md` — uma tabela ordenada com as esteiras certas, os pré-requisitos, estimativa de tempo e um briefing direto para o `diretor-de-marketing` executar.

## Template de output — plano-cascata.md

O arquivo é gerado pelo `meta-orquestrador` e salvo na pasta do projeto. Estrutura esperada:

```markdown
# Plano Cascata — [Objetivo]

## Resumo executivo
- [3 bullets com apostas principais]

## Sequência de execução
| Ordem | Esteira | ID | Pré-requisito | Tempo | Status |
...

## Briefing para execução
[Instruções para diretor-de-marketing]
```
