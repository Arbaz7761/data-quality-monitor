from config import NULL_THRESHOLD

def check_threshold_alerts(quality_report: dict) -> list:
    """Generate alert messages if metrics exceed thresholds."""
    alerts = []

    # Check null percentages
    for col, pct in quality_report["null_percentages"].items():
        if pct > NULL_THRESHOLD * 100:
            alerts.append(f"⚠️  ALERT: Column '{col}' has {pct}% null values!")

    # Check duplicates
    if quality_report["duplicate_rows"] > 0:
        alerts.append(f"⚠️  ALERT: {quality_report['duplicate_rows']} duplicate rows found!")

    # Check outliers
    for col, count in quality_report["outliers"].items():
        alerts.append(f"⚠️  ALERT: Column '{col}' has {count} outliers!")

    return alerts