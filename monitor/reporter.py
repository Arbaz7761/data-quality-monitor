import json

def generate_report(quality_report: dict) -> str:
    """Generate a plain English analysis of the quality report."""

    null_issues = quality_report["null_percentages"]
    outliers = quality_report["outliers"]
    duplicates = quality_report["duplicate_rows"]
    shape = quality_report["shape"]

    report = f"""
📋 DATA QUALITY ANALYSIS REPORT
================================

📊 Dataset Overview:
- Total rows: {shape[0]}
- Total columns: {shape[1]}

🔴 Critical Issues Found:
"""
    # Null issues
    for col, pct in null_issues.items():
        if pct > 50:
            report += f"• CRITICAL: Column '{col}' is {pct}% empty — consider dropping this column\n"
        elif pct > 10:
            report += f"• WARNING: Column '{col}' has {pct}% missing values — fill with mean/median\n"
        else:
            report += f"• MINOR: Column '{col}' has {pct}% missing values — safe to fill or drop\n"

    # Outlier issues
    report += f"\n🔴 Outliers Detected:\n"
    for col, count in outliers.items():
        report += f"• Column '{col}' has {count} outliers — investigate before analysis\n"

    # Duplicates
    report += f"\n🔴 Duplicate Rows: {duplicates}\n"
    if duplicates == 0:
        report += "• No duplicates found — data looks clean!\n"
    else:
        report += f"• Remove {duplicates} duplicate rows before analysis\n"

    # Recommendations
    report += f"""
✅ Recommendations:
- Drop or impute columns with >50% missing values
- Use median imputation for numeric columns with nulls
- Investigate outliers — they may be data entry errors
- Always validate data before running ML models
"""
    return report