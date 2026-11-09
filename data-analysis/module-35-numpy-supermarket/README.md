# Module 35 — Supermarket Sales Analysis with NumPy

## Overview

This project is part of my Python Data Analysis coursework. It explores supermarket sales using NumPy and Pandas to practice descriptive statistics, ranking, grouping, and correlation analysis.

## Dataset

The analysis uses `supermarket_sales.csv`, containing 1,000 supermarket transactions.

## Analysis

The notebook includes:

- Descriptive statistics for unit prices and quantities.
- Average transaction values by city, product line, and customer gender.
- Sales rankings and percentage contributions by category.
- Correlation matrices for transaction hour, sales total, unit price, and customer rating.

## Key Results

| Metric | Result |
|---|---:|
| Total transactions | 1,000 |
| Total sales | 322,966.75 |
| Average transaction value | 322.97 |
| Hour–total correlation | −0.0028 |
| Unit price–rating correlation | −0.0088 |

## Tools

Python, NumPy, Pandas, and Jupyter Notebook.

## Notes

Customer ratings measure satisfaction, not profit margin. Correlations do not imply causation.

## How to Run

1. Open `module-35-supermarket-analysis.ipynb` in VS Code or Jupyter.
2. Ensure `supermarket_sales.csv` is in the same folder.
3. Install NumPy and Pandas if necessary.
4. Select a Python kernel and run all cells.