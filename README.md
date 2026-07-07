# E-Commerce Sales Pipeline & Customer Segmentation Tool

An automated Python data pipeline built using `pandas` to ingest raw, messy transaction records, calculate critical retail business metrics, and segment customer lists for targeted digital marketing campaigns.

## Business Problem Solved
Online store exports are frequently cluttered with duplicate records, incomplete customer profiles (missing emails), and raw financial numbers. This pipeline strips out unusable entries, automates core revenue metrics, and flags high-value buyers so marketing teams can immediately deploy targeted VIP retention campaigns without manual filtering.

## Features & Logic Breakdowns
The main processing engine (`process_sales.py`) handles data transformation using the following architectural phases:

1. **Deduplication:** Filters out redundant platform sync logs to maintain clean, unique customer IDs.
2. **Data Validation:** Drops customer rows lacking valid email addresses to optimize campaign delivery and lower marketing software costs.
3. **Metric Engineering:** Computes **Average Order Value (AOV)** per user ($\text{AOV} = \frac{\text{Total Spent}}{\text{Total Orders}}$).
4. **Behavioral Segmentation:** Uses conditional evaluation logic to classify buyers:
   * **VIP Customer:** Cumulative spend $\ge \$500$
   * **Standard Customer:** Cumulative spend $< \$500$
5. **Operational Sort:** Organizes lists from maximum lifetime value downward to highlight top store earners.

## Installation & Usage
Ensure you have the Python ecosystem installed, along with the `pandas` core framework:
```bash
pip install pandas
