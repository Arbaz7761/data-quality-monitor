
import json
import os
import sys
from monitor.loader import load_data, SUPPORTED_FORMATS
from monitor.detector import run_all_checks
from monitor.reporter import generate_report
from monitor.alerts import check_threshold_alerts

def run_monitor(file_path):
    print("=" * 50)
    print("  AI-Powered Data Quality Monitor")
    print("=" * 50)

    # Step 1: Load data
    try:
        df = load_data(file_path)
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print(f"Please check the file path and try again.")
        return
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print(f"Supported formats: {SUPPORTED_FORMATS}")
        return

    # Step 2: Run checks
    print("\n[Detector] Running quality checks...")
    report = run_all_checks(df)

    # Step 3: Show raw report
    print("\n📊 QUALITY REPORT")
    print("=" * 40)
    print(f"\n🔷 Shape: {report['shape'][0]} rows × {report['shape'][1]} columns")

    print(f"\n🔴 Null Percentages:")
    if report['null_percentages']:
        for col, pct in report['null_percentages'].items():
            print(f"   {col}: {pct}% missing")
    else:
        print("   ✅ No null values found!")

    print(f"\n🔴 Outliers Detected:")
    if report['outliers']:
        for col, count in report['outliers'].items():
            print(f"   {col}: {count} outliers")
    else:
        print("   ✅ No outliers found!")

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
    # Check if file path given
    if len(sys.argv) < 2:
        print("\n📂 Usage: python main.py <file_path>")
        print("📂 Examples:")
        print("   python main.py data/sample_data.csv")
        print("   python main.py data/myfile.json")
        print("   python main.py data/myfile.xlsx")
        print("   python main.py data/myfile.parquet")
        print(f"\n✅ Supported formats: {SUPPORTED_FORMATS}")
    else:
        file_path = sys.argv[1]
        run_monitor(file_path)