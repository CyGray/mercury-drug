from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pandas as pd


REQUIRED_COLUMNS = ["ItemCode", "Description", "UnitPrice", "QuantitySold"]


def validate_sales_dataframe(df: pd.DataFrame) -> Dict[str, List[str]]:
    """Validate a Mercury Drug sales DataFrame and return error details."""
    errors: List[str] = []
    warnings: List[str] = []

    if df.empty:
        errors.append("Dataset is empty.")
        return {"errors": errors, "warnings": warnings}

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        errors.append(f"Missing required columns: {', '.join(missing_columns)}")
        return {"errors": errors, "warnings": warnings}

    for column in ["ItemCode", "Description"]:
        has_blank = df[column].isna().any() or (df[column].astype(str).str.strip() == "").any()
        if has_blank:
            errors.append(f"Column '{column}' has blank or missing values.")

    for column in ["UnitPrice", "QuantitySold"]:
        converted = pd.to_numeric(df[column], errors="coerce")
        if converted.isna().any():
            errors.append(f"Column '{column}' contains non-numeric values.")
        if (converted < 0).any():
            errors.append(f"Column '{column}' contains negative values.")

    if not errors:
        duplicate_rows = df.duplicated(subset=["ItemCode", "Description", "UnitPrice", "QuantitySold"]).sum()
        if duplicate_rows > 0:
            warnings.append(f"Found {duplicate_rows} fully duplicated transaction rows.")

    return {"errors": errors, "warnings": warnings}


def load_and_validate_csv(csv_path: str | Path) -> Dict[str, object]:
    """Load CSV and run validation checks with safe exception handling."""
    csv_path = Path(csv_path)

    if not csv_path.exists():
        return {
            "ok": False,
            "errors": [f"File not found: {csv_path}"],
            "warnings": [],
            "row_count": 0,
        }

    try:
        df = pd.read_csv(csv_path)
    except Exception as exc:
        return {
            "ok": False,
            "errors": [f"Invalid data format or unreadable CSV: {exc}"],
            "warnings": [],
            "row_count": 0,
        }

    result = validate_sales_dataframe(df)
    return {
        "ok": len(result["errors"]) == 0,
        "errors": result["errors"],
        "warnings": result["warnings"],
        "row_count": int(len(df)),
    }


if __name__ == "__main__":
    report = load_and_validate_csv("data/MercuryDrugSales.csv")

    print("Validation Report")
    print("-" * 40)
    print(f"Rows: {report['row_count']}")
    print(f"Status: {'PASS' if report['ok'] else 'FAIL'}")

    if report["errors"]:
        print("Errors:")
        for err in report["errors"]:
            print(f"- {err}")

    if report["warnings"]:
        print("Warnings:")
        for warn in report["warnings"]:
            print(f"- {warn}")
