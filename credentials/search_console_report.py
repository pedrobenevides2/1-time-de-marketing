"""
Relatório Search Console — chamado pelo seo-specialist
Uso: python3 search_console_report.py [dias] [top_n]
"""
import sys
import json
from pathlib import Path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import date, timedelta

CREDENTIALS_FILE = Path(__file__).parent / "google-credentials.json"
SITE_URL = "sc-domain:4fg.com.br"
DAYS = int(sys.argv[1]) if len(sys.argv) > 1 else 30
TOP_N = int(sys.argv[2]) if len(sys.argv) > 2 else 20

credentials = service_account.Credentials.from_service_account_file(
    str(CREDENTIALS_FILE),
    scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
)
service = build("searchconsole", "v1", credentials=credentials)

end_date = date.today() - timedelta(days=2)
start_date = end_date - timedelta(days=DAYS)

body = {
    "startDate": start_date.isoformat(),
    "endDate": end_date.isoformat(),
    "dimensions": ["query"],
    "rowLimit": TOP_N,
    "orderBy": [{"fieldName": "clicks", "sortOrder": "DESCENDING"}]
}

response = service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()
rows = response.get("rows", [])

print(f"\n=== Search Console — Top {TOP_N} keywords ({DAYS} dias) ===")
print(f"Período: {start_date} → {end_date}\n")
print(f"{'Keyword':<45} {'Cliques':>8} {'Imp.':>8} {'CTR':>7} {'Pos.':>6}")
print("-" * 80)

keywords = []
for row in rows:
    kw = {
        "keyword": row["keys"][0],
        "cliques": row["clicks"],
        "impressoes": row["impressions"],
        "ctr": f"{row['ctr']*100:.1f}%",
        "posicao": round(row["position"], 1)
    }
    keywords.append(kw)
    print(f"{kw['keyword']:<45} {kw['cliques']:>8,} {kw['impressoes']:>8,} {kw['ctr']:>7} {kw['posicao']:>6}")

# Totais
total_clicks = sum(r["cliques"] for r in keywords)
total_imp = sum(r["impressoes"] for r in keywords)
print(f"\nTotal (top {TOP_N}): {total_clicks:,} cliques · {total_imp:,} impressões")

print(json.dumps({"periodo_dias": DAYS, "keywords": keywords}, ensure_ascii=False, indent=2))
