# Mercury Drug Store Sales Transactions

## Activity Overview
Build a Python program that analyzes and visualizes Mercury Drug Store sales transactions.

Your program must:
- Read transaction data from a CSV file
- Compute sales values
- Identify key performance items
- Generate charts using `pandas` and `matplotlib`

---

## Learning Objectives
- Apply file handling by loading data from a CSV file
- Perform data manipulation using `pandas`
- Compute and analyze values using operators and expressions
- Use control structures to determine highest, lowest, and median values
- Implement data visualization with `matplotlib` (bar and pie charts)
- Demonstrate clean coding practices and error handling

---

## Input File
Use a CSV file named:

- `MercuryDrugSales.csv`

Create at least **100 dummy records**.

### Required Dataset Fields
- `ItemCode` - Unique product identifier
- `Description` - Product name
- `UnitPrice` - Price per unit
- `QuantitySold` - Number of units sold

---

## Program Requirements
1. Load the dataset using `pandas`.
2. Compute a new column:
	- `TotalSales = UnitPrice * QuantitySold`
3. Identify and display the following:
	- Highest selling item
	- Lowest selling item
	- Median sales item (item closest to the dataset median `TotalSales`)
4. For each identified item, display:
	- `ItemCode`
	- `Description`
	- `TotalSales` (formatted to 2 decimal places)
5. Generate charts:
	- Bar chart of total sales per product
	- Pie chart of sales share for highest, lowest, and median items

---

## Error Handling Requirements
Handle these cases gracefully:
- Missing file
- Invalid data format
- Empty dataset

---

## Expected Submission
- Python source code (`.py`)
- Screenshot of console output
- Screenshot of generated charts
- Short documentation (1-2 paragraphs) describing:
  - Program logic
  - Challenges encountered

---

## Grading Rubric (100 Points)
- Functionality: 25
- Data Handling: 15
- Visualization: 20
- Code Quality: 15
- Error Handling: 10
- Output Formatting: 10
- Documentation: 5

---

## Student Task
Upload your Python file, screenshots, and short documentation based on the requirements above.

## Additional Instructions
- This is a group activity; use your groupings in the Terminal Requirement Activity.
- Only the group leader is required to submit the requirements.
