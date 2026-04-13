from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from analytics_engine import summarize_sales
from charts import plot_bar_sales_per_product, plot_key_items_pie
from data_validation import load_and_validate_csv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze and visualize Mercury Drug sales transactions."
    )
    parser.add_argument(
        "--csv",
        default="data/MercuryDrugSales.csv",
        help="Path to CSV input file (default: data/MercuryDrugSales.csv)",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Generate chart files without opening chart windows.",
    )
    return parser


def print_summary(summary: dict) -> None:
    key_items = summary["key_items"]

    print("Mercury Drug Sales Analysis")
    print("-" * 40)
    print(f"Rows Processed: {summary['row_count']}")
    print(f"Grand Total Sales: PHP {summary['grand_total_sales']:.2f}")
    print("")
    print("Key Performance Items")
    print("-" * 40)

    for label in ["highest", "lowest", "median"]:
        item = key_items[label]
        print(f"{label.title()} Selling Item")
        print(f"ItemCode: {item['ItemCode']}")
        print(f"Description: {item['Description']}")
        print(f"TotalSales: PHP {item['TotalSales']:.2f}")
        print("")


def main() -> int:
    args = build_parser().parse_args()
    csv_path = Path(args.csv)

    validation_report = load_and_validate_csv(csv_path)
    if not validation_report["ok"]:
        print("Validation failed.")
        for err in validation_report["errors"]:
            print(f"- {err}")
        return 1

    df = pd.read_csv(csv_path)
    summary = summarize_sales(df)
    print_summary(summary)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    bar_path = output_dir / "bar_total_sales_per_product.png"
    pie_path = output_dir / "pie_key_items_sales_share.png"

    plot_bar_sales_per_product(df, output_path=str(bar_path), show=not args.no_show)
    plot_key_items_pie(summary["key_items"], output_path=str(pie_path), show=not args.no_show)

    print("Charts generated:")
    print(f"- {bar_path}")
    print(f"- {pie_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
