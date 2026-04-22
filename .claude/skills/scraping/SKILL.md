---
name: scraping
description: Coleta estruturada de dados públicos da web para inteligência de marketing — monitoramento de concorrentes, tendências, preços, conteúdo viral e pesquisa de mercado. Usa WebFetch, WebSearch e Python (gratuitos). Baseado no modelo Spider King.
allowed-tools: WebFetch, WebSearch, Bash(python3 *), Read, Write
---

# Scraping — Coleta de Dados para Marketing

Coleta dados públicos da web de forma estruturada. Sem browser automation, sem dependências pagas.

## Casos de uso de marketing

| Objetivo | O que coletar | Fonte |
|----------|--------------|-------|
| Análise de concorrentes | Preços, produtos, copies de ads | Site + Meta Ad Library |
| Tendências de conteúdo | Tópicos virais, hashtags | TikTok, YouTube, Google Trends |
| Pesquisa de palavras-chave | Sugestões de autocomplete | Google, YouTube, TikTok |
| Monitoramento de marca | Menções públicas | Google Search |
| Benchmarking | Métricas públicas de canais | YouTube, Instagram público |
| Pesquisa de influenciadores | Perfis e métricas públicas | Instagram, TikTok |

---

## Fase 1 — Reconhecimento (sempre antes de coletar)

Antes de qualquer coleta, responda:

```
1. O dado é público e acessível sem login?
2. Qual a URL base do alvo?
3. Os dados estão no HTML estático ou carregados via JavaScript?
4. Existe API pública (ou documentada) que entrega esses dados?
5. Qual o volume: página única, lista paginada ou stream contínuo?
```

**Classificação do alvo:**
- `html-estático` → WebFetch direto
- `api-pública` → chamada direta à API REST/JSON
- `js-dinâmico` → inspecionar Network tab para encontrar a API real por trás
- `requer-login` → fora do escopo (use dados exportados manualmente)

---

## Fase 2 — Coleta por tipo

### HTML estático (WebFetch)
```python
# Claude usa WebFetch diretamente
# URL → extrai dados com parsing de markdown/texto
```

### API pública (Python requests)
```python
import requests, json

headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get("https://api.exemplo.com/endpoint", headers=headers)
data = r.json()

# Salvar resultado
with open("dados_coletados.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

### Paginação automática
```python
resultados = []
pagina = 1

while True:
    r = requests.get(f"https://api.exemplo.com/items?page={pagina}", headers=headers)
    dados = r.json()
    if not dados.get("items"):
        break
    resultados.extend(dados["items"])
    pagina += 1

print(f"{len(resultados)} itens coletados")
```

### Google Search (via WebSearch)
```
Buscar: site:concorrente.com OR "concorrente" preço -inurl:login
Buscar: TikTok viral "[nicho]" 2025
```

---

## Fase 3 — Casos práticos de marketing

### Monitorar anúncios de concorrentes (Meta Ad Library — grátis)
```
URL: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=[MARCA]
WebFetch → extrair: formatos, copies, CTAs, duração das campanhas
```

### Coletar sugestões de autocomplete (pesquisa de keywords)
```python
import requests

def google_autocomplete(termo):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={termo}"
    r = requests.get(url)
    return r.json()[1]

sugestoes = google_autocomplete("marketing digital")
print(sugestoes)
```

### Tendências TikTok (Creative Center — grátis)
```
WebFetch: https://ads.tiktok.com/business/creativecenter/trend-keywords/pc/en
Extrair: trending hashtags, sons populares, categorias em alta
```

### Métricas públicas de canal YouTube
```python
# YouTube Data API v3 — grátis (10k unidades/dia)
# Chave de API: console.cloud.google.com (sem custo no tier gratuito)
import requests

API_KEY = "SUA_CHAVE"
canal_id = "UCxxxxxx"
url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={canal_id}&key={API_KEY}"
r = requests.get(url)
stats = r.json()["items"][0]["statistics"]
print(f"Inscritos: {stats['subscriberCount']}, Views: {stats['viewCount']}")
```

---

## Fase 4 — Entrega estruturada

Sempre entregue os dados coletados em:
1. **JSON**: para processar depois
2. **Markdown table**: para leitura rápida
3. **Insights**: 3-5 conclusões acionáveis dos dados

## Restrições invioláveis (modelo Spider King)

- Somente dados **publicamente acessíveis sem login**
- Sem automação de browser (Selenium, Playwright) — use APIs diretas
- Sem dados pessoais identificáveis
- Respeite `robots.txt` e termos de uso do site
- Rate limiting: máximo 1 requisição/segundo em sites sem API pública
