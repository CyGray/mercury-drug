# Part 1 Data Notes

This file documents the Part 1 outputs for data preparation and validation.

## Files Produced
- `data/MercuryDrugSales.csv` (main dataset, 120 rows)
- `data/MercuryDrugSales.fixture.csv` (small fixture dataset, 12 rows)
- `data_validation.py` (reusable validation utility)

## Data Dictionary
- `ItemCode`: Product code (string)
- `Description`: Product name (string)
- `UnitPrice`: Price per unit (numeric, positive)
- `QuantitySold`: Quantity sold (numeric, non-negative integer expected)

## Validation Rules Applied
1. Dataset must not be empty.
2. Required columns must exist:
   - `ItemCode`
   - `Description`
   - `UnitPrice`
   - `QuantitySold`
3. `ItemCode` and `Description` cannot be blank/missing.
4. `UnitPrice` and `QuantitySold` must be numeric.
5. `UnitPrice` and `QuantitySold` cannot be negative.
6. Duplicate full rows are flagged as warnings (not hard errors).

## How to Run Validation
Run from project root:

```powershell
python data_validation.py
```

Expected output includes:
- Total row count
- PASS/FAIL status
- Any errors and warnings

## Handoff Notes for Other Parts
- Part 2 can use either `data/MercuryDrugSales.csv` or `data/MercuryDrugSales.fixture.csv`.
- Part 3 can start immediately with the fixture file for faster chart iteration.
- Part 4 can reuse `load_and_validate_csv(...)` in `data_validation.py` for quality checks.