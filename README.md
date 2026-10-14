# Retail Sales Performance & Profitability Analytics

An end-to-end retail sales analytics project using Python, Pandas, NumPy, Matplotlib, Seaborn, and Power BI to analyze sales performance, profitability, product trends, regional performance, discounts, and sales channels.

## Dashboard Preview

![Retail Sales Performance & Profitability Analytics Dashboard](images/sales_dashboard.png)

## Project Overview

This project analyzes retail sales data to understand revenue, profit, product performance, regional trends, discounts, and sales channels. It follows an end-to-end analytics workflow that includes data understanding, data cleaning, exploratory data analysis (EDA), KPI analysis, and interactive Power BI dashboard development.

The goal is to transform raw transactional data into meaningful business insights and present the results through an interactive dashboard.

## Problem Statement

Retail businesses generate large volumes of transactional data, but raw records alone do not provide a clear understanding of business performance.

Data quality issues such as missing values, duplicate records, inconsistent categories, invalid data, and discrepancies in sales calculations can affect the reliability of business reporting.

Without a structured analytical workflow, stakeholders may find it difficult to evaluate profitability, compare product and regional performance, understand discount-related trends, and monitor sales across different channels.

This project addresses the following business questions:

- How are overall sales, profit, and profit margin performing?
- Which product categories and regions contribute to sales performance?
- How are discounts related to profitability?
- How does performance vary across sales channels?
- What data quality issues require further investigation?

## Proposed Solution

The project implements an end-to-end retail analytics workflow using Python and Power BI.

- **Data Cleaning:** Identified and handled data quality issues, including duplicate records, missing values, inconsistent categories, and invalid data.
- **Exploratory Data Analysis:** Examined sales, profitability, discounts, product categories, regions, and sales channels.
- **KPI Analysis:** Analyzed key business metrics such as total sales, total profit, and profit margin.
- **Interactive Dashboard:** Developed a Power BI dashboard with KPI cards, charts, and interactive filters.
- **Data Quality Validation:** Investigated inconsistencies between recorded sales and formula-derived sales, documenting discrepancies for further investigation.

The cleaned dataset, analytical notebooks, Python scripts, and Power BI dashboard provide a consolidated view of retail performance.

## Project Structure

```text
Project_1_Sales_Analytics/
├── data/
│   ├── raw/
│   │   └── Project_1_Raw_Retail_Sales.csv
│   └── processed/
│       └── sales_cleaned.csv
├── images/
│   └── sales_dashboard.png
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda.ipynb
├── powerbi/
│   ├── Sales_Analytics_Dashboard.pbix
│   └── Sales_Analytics_Dashboard.docx
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── data_cleaning.py
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Data exploration and EDA |
| Power BI | Interactive dashboard development |
| Git & GitHub | Version control and project hosting |

## Project Workflow

1. **Data Understanding:** Inspected the dataset structure, columns, and data quality.
2. **Data Cleaning:** Checked and handled duplicate records, missing values, inconsistent categories, and invalid data.
3. **Exploratory Data Analysis:** Examined sales, profit, discounts, product categories, regional trends, and sales channels.
4. **KPI Analysis:** Evaluated sales, profit, and profit margin to understand business performance.
5. **Dashboard Development:** Created an interactive Power BI dashboard with KPI cards, charts, and filters.
6. **Validation and Documentation:** Documented data quality findings and potential issues requiring additional investigation.

## Key Analysis Areas

- Total sales and total profit
- Profit margin
- Product and category performance
- Regional sales trends
- Discount and profitability relationships
- Sales channel performance
- Data quality and sales calculation discrepancies

## Challenges Faced & Solutions

### 1. Data Quality Issues

**Challenge:** Raw retail data contained data quality issues, including missing values, duplicate records, inconsistent categories, and invalid data.

**Solution:** Used Pandas to inspect the dataset, identify data quality issues, apply appropriate cleaning steps, and prepare the data for analysis.

### 2. Sales Calculation Discrepancies

**Challenge:** During data validation, 431 records were identified where recorded sales differed from formula-derived sales by more than ₹1.

**Solution:** Compared recorded sales with formula-derived values and documented the discrepancies for further investigation. The underlying cause was not established, so the records were treated as a data quality concern rather than assuming which value was correct.

### 3. Understanding Profitability and Discount Trends

**Challenge:** Looking at total sales alone does not provide a complete picture of business performance. Sales, profit, profit margin, and discounts need to be examined together.

**Solution:** Conducted EDA to explore relationships among these metrics and organized the findings into business-focused analytical categories. Any relationship observed in the dataset should be interpreted as an association unless further analysis establishes causation.

### 4. Presenting Analysis Clearly

**Challenge:** Notebook outputs and individual charts can make it difficult for stakeholders to get a consolidated view of business performance.

**Solution:** Built a Power BI dashboard with KPI cards, visualizations, and interactive filters to make it easier to explore sales and profitability from different perspectives.

## Data Quality Note

During validation, 431 records were identified where recorded sales differed from formula-derived sales by more than ₹1.

These discrepancies were documented for further investigation. Their underlying cause has not been established, and the analysis does not assume that either the recorded or formula-derived values are necessarily correct.

This validation step highlights the importance of checking data consistency before relying on analytical results for business decisions.

## Installation and Setup

### Prerequisites

- Python installed on your system
- Git
- Jupyter Notebook or JupyterLab
- Microsoft Power BI Desktop to open the dashboard

### 1. Clone the Repository

```bash
git clone https://github.com/Kishore292006/retail-sales-performance-analytics.git
cd retail-sales-performance-analytics
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the Dataset

Ensure the raw retail dataset is available at:

```text
data/raw/Project_1_Raw_Retail_Sales.csv
```

If the dataset is not included in the repository, place your authorized copy at this path before running the cleaning workflow.

### 5. Explore the Notebooks

Open Jupyter Notebook or JupyterLab and run the notebooks in sequence:

1. `01_data_understanding.ipynb`
2. `02_data_cleaning.ipynb`
3. `03_eda.ipynb`

These notebooks document the data understanding, cleaning, and exploratory analysis workflow.

### 6. Run the Python Scripts

Run the project scripts from the project root, following the file paths and execution order configured in the source code.

The Power BI dashboard can be opened using Microsoft Power BI Desktop.

## Business Value

This project demonstrates how raw retail data can be transformed into structured analysis and interactive visual reporting.

It helps stakeholders:

- Monitor sales and profitability metrics.
- Compare product and regional performance.
- Explore discount-related profitability patterns.
- Review sales performance across channels.
- Identify data quality issues that may affect reporting reliability.

The findings provide a starting point for business investigation. Additional context and validation would be needed before using them to make operational decisions.

## Limitations & Future Improvements

- Investigate the root cause of the 431 sales calculation discrepancies.
- Validate important business metrics against trusted source records.
- Add further time-based analysis if the required date fields are available.
- Extend the dashboard with additional business metrics where supported by the dataset.
- Automate data validation and reporting for future datasets.

## Author

**Kishore Mattapalli**  
B.Tech — Computer Science and Engineering (AI & Machine Learning)  
GD Goenka University

- **GitHub:** [Retail Sales Performance & Profitability Analytics](https://github.com/Kishore292006/retail-sales-performance-analytics)
- **LinkedIn:** [Kishore Mattapalli](https://www.linkedin.com/in/mattapalli-kishore-74a134410)

---

*This project was developed as part of my data analytics portfolio to demonstrate practical skills in Python, data cleaning, exploratory data analysis, business metrics, and Power BI dashboard development.*