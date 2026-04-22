import json
import os
from monitor.loader import load_data
from monitor.detector import run_all_checks
from monitor.reporter import generate_report
from monitor.alerts import check_threshold_alerts

def run_monitor():
    print("=" * 50)
    print("  AI-Powered Data Quality Monitor")
    print("=" * 50)

    # Step 1: Load data
    df = load_data()

    # Step 2: Run checks
    print("\n[Detector] Running quality checks...")
    report = run_all_checks(df)

    # Step 3: Show raw report
    print("\n📊 QUALITY REPORT")
    print("=" * 40)
    print(f"\n🔷 Shape: {report['shape'][0]} rows × {report['shape'][1]} columns")

    print(f"\n🔴 Null Percentages:")
    for col, pct in report['null_percentages'].items():
        print(f"   {col}: {pct}% missing")

    print(f"\n🔴 Outliers Detected:")
    for col, count in report['outliers'].items():
        print(f"   {col}: {count} outliers")

    print(f"\n🔴 Duplicate Rows: {report['duplicate_rows']}")

    # Step 4: Alerts
    alerts = check_threshold_alerts(report)
    if alerts:
        print("\n🚨 ALERTS:")
        for alert in alerts:
            print(f"   {alert}")
    else:
        print("\n✅ No critical alerts.")

    # Step 5: AI Report
    print("\n[AI] Generating plain-English analysis...")
    print("(This may take 10-15 seconds...)\n")
    ai_summary = generate_report(report)
    print("🤖 AI ANALYSIS:")
    print("-" * 40)
    print(ai_summary)

    # Step 6: Save report
    os.makedirs("sample_output", exist_ok=True)
    with open("sample_output/latest_report.txt", "w", encoding="utf-8") as f:
        f.write(ai_summary)
    print("\n✅ Report saved to sample_output/latest_report.txt")

if __name__ == "__main__":
    run_monitor()