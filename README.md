# Amazon Sales 2025 — End-to-End Data Analyst Portfolio Project

**Author:** Abhishek Wagge | B.Com (Gulbarga University, 2024) | Aspiring Data Analyst / MIS Executive / BI Analyst
**Tools used:** Excel (Pivot Tables, Charts, Dashboard, Formulas) · SQL (SQLite) · Python (Pandas, Matplotlib, Seaborn) · R (tidyverse, ggplot2, statistical tests)

---

## 1. Project Overview

This project simulates a full year (Jan–Dec 2025) of Amazon India e-commerce order data — 12,000 orders across 8 product categories, 12 cities, 3 sales channels, and 5 payment methods — and walks through the complete data analyst workflow:

**Raw Data → Cleaning → SQL Querying → Python EDA → R Statistical Testing → Excel Dashboard → Business Insights & Recommendations**

This is designed as an **interview-ready portfolio project**: it demonstrates end-to-end skills across the exact tools listed in most Data Analyst / MIS Executive / BI Analyst / Reporting Analyst job descriptions in India.

> **Note on data:** This is a realistically simulated dataset (not scraped from Amazon's actual systems), built with seasonality (festive sale spikes in Oct/Nov), realistic price bands per category, return/cancellation patterns, and customer segments — so the analysis and insights below are demonstrative of analytical method, not real Amazon financials.

---

## 2. Folder Structure

```
amazon_sales_project/
│
├── data/
│   ├── amazon_sales_2025.csv        <- Raw dataset (12,000 rows, 20 columns)
│   ├── amazon_sales.db               <- SQLite database (preloaded)
│   └── generate_data.py              <- Script used to generate the dataset
│
├── sql/
│   ├── 01_schema.sql                 <- Table schema (DDL)
│   ├── 02_analysis_queries.sql       <- 15 business-question SQL queries
│   └── load_to_sqlite.py             <- Loads CSV into SQLite
│
├── python/
│   ├── amazon_sales_analysis.py      <- Full EDA + visualizations
│   ├── amazon_sales_2025_cleaned.csv <- Cleaned dataset (with derived columns)
│   ├── monthly_revenue_summary.csv
│   ├── category_revenue_summary.csv
│   └── charts/                       <- 8 PNG charts
│
├── r/
│   ├── amazon_sales_analysis.R       <- EDA + hypothesis testing (t-test, chi-sq, regression)
│   └── charts/                       <- ggplot2 charts (generated when run in RStudio)
│
├── excel/
│   └── Amazon_Sales_2025_Analysis.xlsx  <- Raw data + Pivot tables + Dashboard with charts
│
└── docs/
    ├── README.md                     <- This file
    ├── Insights_Report.md            <- Full written analysis & business recommendations
    └── Interview_QA_Prep.md          <- Common interview questions based on this project
```

---

## 3. Dataset Schema

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date / Order_Time | Date & time of order placement |
| Customer_ID | Unique customer identifier |
| Customer_Segment | Prime / Non-Prime |
| Category | Product category (8 categories) |
| Product | Product name |
| Quantity | Units ordered |
| Unit_Price | Price per unit (₹) |
| Gross_Amount | Quantity × Unit_Price |
| Discount_Pct | Discount percentage applied |
| Discount_Amount | Discount value (₹) |
| Net_Amount | Final amount paid (₹) |
| City / State | Delivery location |
| Sales_Channel | Amazon App / Amazon Web / Alexa Voice Order |
| Payment_Method | Card / UPI / Wallet / COD / Net Banking |
| Order_Status | Delivered / Returned / Cancelled / Shipped - In Transit |
| Rating | Customer rating (1-5, blank if not rated/not delivered) |
| Delivery_Days | Days taken for delivery |

---

## 4. How to Run Each Part

### SQL
```bash
cd sql
python3 load_to_sqlite.py          # creates data/amazon_sales.db
# Then open amazon_sales.db in DB Browser for SQLite and run 02_analysis_queries.sql
```

### Python
```bash
cd python
pip install pandas numpy matplotlib seaborn
python3 amazon_sales_analysis.py
```

### R
```r
# In RStudio, set working directory to /r
install.packages(c("tidyverse","lubridate","scales"))
source("amazon_sales_analysis.R")
```

### Excel
Open `excel/Amazon_Sales_2025_Analysis.xlsx`:
- **Dashboard** tab — KPI summary cards (live formulas)
- **Pivot_Category** — category revenue + bar chart
- **Pivot_Monthly** — monthly trend + line chart
- **Pivot_City_Segment** — city, segment, channel breakdowns + pie chart
- **Order_Status_Analysis** — returns/cancellations + pie chart
- **Raw_Data** — full 12,000-row dataset

---

## 5. Key Business Questions Answered

1. What is the overall revenue, order volume, and AOV for 2025?
2. Which months show festive-season spikes, and what's the MoM growth pattern?
3. Which categories and products drive the most revenue?
4. Which cities/states are top revenue contributors, and how does delivery speed vary?
5. Do Prime customers spend significantly more than Non-Prime (statistically tested)?
6. Is there a relationship between payment method and return/cancellation rate?
7. What discount band maximizes revenue without eroding margins?
8. Which categories have the highest return rates (potential quality/fit issues)?
9. Does a higher discount correlate with lower customer ratings?

Full answers + business recommendations are in `docs/Insights_Report.md`.

---

## 6. Why This Project Helps in Interviews

- Covers the **full analytics stack** (SQL + Excel + Python + R) — matches almost every JD for Data Analyst / MIS / BI / Reporting Analyst roles in India.
- Demonstrates **business framing**: every query/chart is tied to a real business question, not just "show me the data."
- Includes **statistical rigor** (t-test, chi-square, correlation, regression in R) — differentiates from basic dashboard-only projects.
- **Dashboard-ready** Excel file with live formulas — good to screen-share in interviews.
- Comes with a prep doc (`Interview_QA_Prep.md`) so you can explain your own project confidently.
