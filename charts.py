from __future__ import annotations

import os
from pathlib import Path
from typing import Dict

import pandas as pd

_MPL_DIR = Path(".mplconfig")
_MPL_DIR.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(_MPL_DIR.resolve()))

import matplotlib.pyplot as plt


def plot_bar_sales_per_product(
    df: pd.DataFrame, output_path: str | None = None, show: bool = True
) -> None:
    """Build a bar chart of total sales per product."""
    working = df.copy()
    if "TotalSales" not in working.columns:
        working["TotalSales"] = working["UnitPrice"] * working["QuantitySold"]

    summary = working.groupby("Description")["TotalSales"].sum().sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    plt.bar(summary.index, summary.values, color="#2a9d8f")
    plt.title("Total Sales per Product")
    plt.xlabel("Product Name")
    plt.ylabel("Total Sales (PHP)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=150)
    if show:
        plt.show()
    else:
        plt.close()


def plot_key_items_pie(
    key_items: Dict[str, Dict[str, object]], output_path: str | None = None, show: bool = True
) -> None:
    """Build a pie chart for highest, lowest, and median sales items."""
    labels = [
        f"Highest: {key_items['highest']['Description']}",
        f"Lowest: {key_items['lowest']['Description']}",
        f"Median: {key_items['median']['Description']}",
    ]
    values = [
        float(key_items["highest"]["TotalSales"]),
        float(key_items["lowest"]["TotalSales"]),
        float(key_items["median"]["TotalSales"]),
    ]

    plt.figure(figsize=(9, 9))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Sales Share: Highest vs Lowest vs Median Item")
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=150)
    if show:
        plt.show()
    else:
        plt.close()
