# TASK OWNERSHIP PLAN (HORIZONTAL SCALING)

This version minimizes blocking so all 4 members can work in parallel from day 1.

## Parallel-First Team Rules
- Use a shared interface contract early: columns (`ItemCode`, `Description`, `UnitPrice`, `QuantitySold`, `TotalSales`) and output schema for key items.
- Each part develops with sample/stub data first, then switches to real merged data.
- Integrate in short checkpoints (not one big handoff at the end).

## Part 1 - Data Pipeline and Fixtures
**Owner:** Member 1

### Scope
- Create `MercuryDrugSales.csv` with at least 100 dummy records
- Provide a small fixture CSV (for fast tests) and one main CSV (for final run)
- Add data validation helper for required columns and numeric fields

### Deliverables
- Dataset files
- Reusable validation utility
- Data dictionary notes

### Dependencies
- Depends on: None
- Blocks: Final production run only (others can proceed using fixture/stub data)

## Part 2 - Analytics Engine
**Owner:** Member 2

### Scope
- Build logic to compute `TotalSales = UnitPrice * QuantitySold`
- Identify highest, lowest, and median sales items
- Expose results through reusable functions (not only print statements)

### Deliverables
- Analysis module/functions
- Structured output contract for key items and totals

### Dependencies
- Depends on: Shared interface contract only
- Blocks: No direct blocking; visualization and QA can use mocked outputs immediately

## Part 3 - Visualization Layer
**Owner:** Member 3

### Scope
- Build bar chart for total sales per product
- Build pie chart for highest/lowest/median sales share
- Keep chart functions independent by accepting DataFrame/function inputs

### Deliverables
- Chart module/functions
- Screenshot-ready chart templates

### Dependencies
- Depends on: Shared interface contract only
- Blocks: No direct blocking; can proceed with sample DataFrame before final merge

## Part 4 - Reliability, QA, and Packaging
**Owner:** Member 4

### Scope
- Implement error handling (missing file, invalid format, empty dataset)
- Create integration tests/checklist for analysis + charts
- Prepare submission artifacts: console screenshot, chart screenshots, short documentation

### Deliverables
- Error-handling wrapper and run checklist
- QA notes and final submission package

### Dependencies
- Depends on: Shared interface contract only for early work
- Blocks: Final submission assembly only

## Minimal Blocking Dependency Map
1. Shared interface contract (Day 1) enables Parts 2, 3, and 4 in parallel.
2. Part 1 is only required for final real-data execution, not for development start.
3. Parts 2 and 3 are peer tracks and should not block each other.
4. Part 4 runs continuously with mocks/stubs, then validates final integrated build.

## Integration Checkpoints (to avoid vertical handoffs)
1. Checkpoint A (early): agree on function signatures and output schema.
2. Checkpoint B (mid): connect analytics to charts using fixture data.
3. Checkpoint C (late): swap in final dataset, run full QA, capture required outputs.
