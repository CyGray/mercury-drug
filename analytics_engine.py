from __future__ import annotations

from typing import Dict, List

import pandas as pd


REQUIRED_COLUMNS = ["ItemCode", "Description", "UnitPrice", "QuantitySold"]


def compute_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of df with TotalSales = UnitPrice * QuantitySold."""
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    result = df.copy()
    result["UnitPrice"] = pd.to_numeric(result["UnitPrice"], errors="raise")
    result["QuantitySold"] = pd.to_numeric(result["QuantitySold"], errors="raise")
    result["TotalSales"] = result["UnitPrice"] * result["QuantitySold"]
    return result


def _item_payload(row: pd.Series) -> Dict[str, object]:
    return {
        "ItemCode": str(row["ItemCode"]),
        "Description": str(row["Description"]),
        "TotalSales": float(row["TotalSales"]),
    }


def identify_key_sales_items(df: pd.DataFrame) -> Dict[str, Dict[str, object]]:
    """Return highest, lowest, and median sales items from a DataFrame with TotalSales."""
    if df.empty:
        raise ValueError("Dataset is empty.")
    if "TotalSales" not in df.columns:
        raise ValueError("Column 'TotalSales' is required.")

    working = df.copy()
    working["TotalSales"] = pd.to_numeric(working["TotalSales"], errors="raise")

    highest_row = working.loc[working["TotalSales"].idxmax()]
    lowest_row = working.loc[working["TotalSales"].idxmin()]

    median_value = float(working["TotalSales"].median())
    closest_index = (working["TotalSales"] - median_value).abs().idxmin()
    median_row = working.loc[closest_index]

    return {
        "highest": _item_payload(highest_row),
        "lowest": _item_payload(lowest_row),
        "median": _item_payload(median_row),
    }


def summarize_sales(df: pd.DataFrame) -> Dict[str, object]:
    """Run Part 2 analytics and return structured output for reuse by other parts."""
    with_totals = compute_total_sales(df)
    key_items = identify_key_sales_items(with_totals)

    return {
        "row_count": int(len(with_totals)),
        "grand_total_sales": float(with_totals["TotalSales"].sum()),
        "key_items": key_items,
    }
