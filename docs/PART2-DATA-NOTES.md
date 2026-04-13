# Part 2 Data Notes

This file documents the Part 2 Analytics Engine outputs.

## File Produced

- `analytics_engine.py` (analysis module with reusable functions)

## Scope Implemented

1. Compute `TotalSales = UnitPrice * QuantitySold`
2. Identify highest, lowest, and median sales items
3. Expose reusable functions with structured outputs

## Functions

- `compute_total_sales(df)`
  - Input: DataFrame with `ItemCode`, `Description`, `UnitPrice`, `QuantitySold`
  - Output: Copy of DataFrame with added `TotalSales`

- `identify_key_sales_items(df)`
  - Input: DataFrame that includes `TotalSales`
  - Output: Dictionary with `highest`, `lowest`, `median`

- `summarize_sales(df)`
  - Input: DataFrame with required columns
  - Output: Structured summary dictionary for integration

## Output Contract

```python
{
    "row_count": int,
    "grand_total_sales": float,
    "key_items": {
        "highest": {
            "ItemCode": str,
            "Description": str,
            "TotalSales": float,
        },
        "lowest": {
            "ItemCode": str,
            "Description": str,
            "TotalSales": float,
        },
        "median": {
            "ItemCode": str,
            "Description": str,
            "TotalSales": float,
        },
    },
}
```

## Notes for Integration

- Functions are reusable and do not rely on print-only outputs.
- `summarize_sales(...)` is the main handoff function for Part 3 and Part 4.
