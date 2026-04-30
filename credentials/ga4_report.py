"""
Relatório GA4 — chamado pelo analytics-analyst
Uso: python3 ga4_report.py [dias]
"""
import sys
import json
from pathlib import Path
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension
from google.oauth2 import service_account

CREDENTIALS_FILE = Path(__file__).parent / "google-credentials.json"
PROPERTY_ID = "534288947"
DAYS = int(sys.argv[1]) if len(sys.argv) > 1 else 30

credentials = service_account.Credentials.from_service_account_file(
    str(CREDENTIALS_FILE),
    scopes=["https://www.googleapis.com/auth/analytics.readonly"]
)
client = BetaAnalyticsDataClient(credentials=credentials)

request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    date_ranges=[DateRange(start_date=f"{DAYS}daysAgo", end_date="today")],
    dimensions=[Dimension(name="sessionDefaultChannelGroup")],
    metrics=[
        Metric(name="sessions"),
        Metric(name="totalUsers"),
        Metric(name="bounceRate"),
        Metric(name="averageSessionDuration"),
        Metric(name="conversions"),
    ],
)

response = client.run_report(request)

results = []
for row in response.rows:
    results.append({
        "canal": row.dimension_values[0].value,
        "sessoes": int(row.metric_values[0].value),
        "usuarios": int(row.metric_values[1].value),
        "bounce_rate": f"{float(row.metric_values[2].value)*100:.1f}%",
        "duracao_media_s": int(float(row.metric_values[3].value)),
        "conversoes": int(float(row.metric_values[4].value)),
    })

results.sort(key=lambda x: x["sessoes"], reverse=True)

print(f"\n=== GA4 — Últimos {DAYS} dias ({PROPERTY_ID}) ===\n")
print(f"{'Canal':<30} {'Sessões':>8} {'Usuários':>9} {'Bounce':>8} {'Duração':>9} {'Conv.':>6}")
print("-" * 75)
for r in results:
    mins = r['duracao_media_s'] // 60
    secs = r['duracao_media_s'] % 60
    print(f"{r['canal']:<30} {r['sessoes']:>8,} {r['usuarios']:>9,} {r['bounce_rate']:>8} {mins}m{secs:02d}s {r['conversoes']:>6}")

print(f"\nTotal canais: {len(results)}")
print(json.dumps({"periodo_dias": DAYS, "canais": results}, ensure_ascii=False, indent=2))
