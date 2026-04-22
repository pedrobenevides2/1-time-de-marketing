---
name: content-calendar
description: Gera calendário editorial mensal multi-plataforma em formato de tabela markdown. Distribui conteúdo por canal, formato, pilar e responsável. Pronto para copiar no Notion, Google Sheets ou arquivo do projeto.
---
# Content Calendar

## Informações necessárias
1. Canais ativos (YouTube, TikTok, Instagram, Facebook, Blog, Email, Podcast)
2. Frequência por canal
3. Pilares de conteúdo definidos (use `/posicionamento` se não tiver)
4. Datas especiais do mês (lançamentos, feriados, eventos)
5. Tema do mês (opcional)

## Calendário mensal

Gere uma tabela com esta estrutura:

```markdown
# Calendário de Conteúdo — [Mês/Ano]
Tema do mês: [tema central]

| Data | Dia | Canal | Formato | Pilar | Título/Assunto | CTA | Status |
|------|-----|-------|---------|-------|----------------|-----|--------|
| 01/XX | Seg | Instagram | Carrossel | Educativo | "5 erros de..." | Salvar | 📝 Briefing |
| 01/XX | Seg | TikTok | Vídeo 30s | Educativo | Corte do carrossel | Seguir | 📝 Briefing |
| 02/XX | Ter | Blog | Artigo | SEO | "Como fazer X" | Newsletter | 📝 Briefing |
...
```

**Status legend:**
- 📝 Briefing = precisa de brief
- ✍️ Produção = em criação
- 👀 Revisão = aguardando aprovação
- ✅ Aprovado = pronto para publicar
- 📅 Agendado = no agendador
- ✔️ Publicado = no ar

## Distribuição de pilares no mês

```
Pilar 1 (Educativo):   40% dos posts
Pilar 2 (Bastidores):  20% dos posts
Pilar 3 (Cases/Prova): 20% dos posts
Pilar 4 (Promoção):    20% dos posts
```

## Regra de repurposing no calendário

Para cada conteúdo-raiz, gere as derivações:
- 1 artigo de blog → 1 vídeo YouTube + 1 carrossel + 1 email + 3 TikToks
- 1 vídeo longo → 5 Shorts + 5 Reels + 5 TikToks

## Ferramentas gratuitas para usar o calendário
- Google Sheets (compartilhável com o time)
- Notion (database com kanban de status)
- Meta Business Suite (agendamento FB + Instagram)
- TikTok Creator Studio (agendamento TikTok)
