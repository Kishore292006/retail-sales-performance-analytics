# Retail Sales Performance & Profitability Analytics

An end-to-end retail sales analytics project using Python, Pandas, NumPy, Matplotlib, Seaborn, and Power BI to clean sales data, perform exploratory data analysis (EDA), identify business trends, and build an interactive dashboard.

## Dashboard Preview

<p align="center">
  <img src="images/sales_dashboard.png" alt="Retail Sales Performance and Profitability Analytics Dashboard" width="100%">
</p>

## Project Overview

This project analyzes a synthetic retail sales dataset containing order details, customer information, product categories, sales channels, discounts, costs, sales, and profit.

The objective is to transform raw sales data into meaningful business insights through data cleaning, validation, exploratory analysis, KPI calculations, and interactive visualization.

## Business Objectives

* Analyze overall sales, profit, and profit margin.
* Identify top-performing product categories and regions.
* Compare online and in-store sales performance.
* Understand monthly sales trends.
* Examine order statuses, including delivered, cancelled, and returned orders.
* Explore relationships between discounts, sales, and profit.
* Present findings through an interactive Power BI dashboard.

## Tools and Technologies

* **Python** — data processing and analysis
* **Pandas** — data cleaning and manipulation
* **NumPy** — numerical operations
* **Matplotlib** — data visualization
* **Seaborn** — statistical visualization
* **Power BI** — interactive dashboards and KPI reporting
* **Jupyter Notebook** — data exploration and EDA
* **Git and GitHub** — version control and project sharing

## Project Workflow

### 1. Data Understanding

* Inspected dataset dimensions, column names, and data types.
* Examined descriptive statistics and individual columns.
* Identified potential data-quality issues.

### 2. Data Cleaning and Validation

* Removed duplicate records.
* Standardized column names and selected categorical values.
* Converted order dates into datetime format.
* Handled missing values in selected columns.
* Checked invalid quantities, unit prices, and discount values.
* Validated the cleaned dataset using automated checks.

### 3. Exploratory Data Analysis (EDA)

* Analyzed sales and profit by product category.
* Compared regional and sales-channel performance.
* Examined monthly sales trends.
* Analyzed order-status distribution.
* Investigated profit margins across categories.
* Explored correlations between numerical variables.

### 4. Business Analysis

Calculated and compared key performance indicators (KPIs), including total sales, total profit, and profit margin, to understand business performance.

### 5. Power BI Dashboard

Developed an interactive dashboard featuring:

* Total Sales
* Total Profit
* Profit Margin
* Monthly Sales Trend
* Sales by Category
* Sales by Region
* Sales by Channel
* Top-performing Category, Region, and Channel
* Year, Category, and Region slicers

## Key Business Insights

* **Product categories:** Electronics recorded the highest sales and profit among the analyzed categories.
* **Regional performance:** The South region recorded the highest sales and profit, while the East region recorded the lowest.
* **Sales channels:** Online sales contributed more total sales and profit than store sales, while average order values were relatively close.
* **Monthly trends:** Sales remained relatively stable across the analyzed period, with month-to-month variation.
* **Discounts:** Higher discount levels were associated with lower average sales and profit in the exploratory analysis. This relationship does not establish causation.
* **Profitability:** Category profit margins were relatively similar, at approximately 25.7%–26.0%.

## Data Quality Notes

The cleaned dataset was checked for duplicate records, missing values, invalid numerical values, and invalid dates.

Financial validation identified 431 records where calculated sales differed from recorded sales by more than ₹1. These discrepancies were identified for further investigation. Recorded sales and profit values were not silently overwritten.

The dataset is synthetic and is used for learning and portfolio demonstration. The findings should not be interpreted as actual results from a real retailer.

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
└── README.md
```

## How to Run the Project

### Prerequisites

* Python 3.12 or a compatible Python version
* Required Python libraries
* Jupyter Notebook or PyCharm
* Power BI Desktop to open the dashboard

### 1. Clone the Repository

```bash
git clone https://github.com/Kishore292006/retail-sales-performance-analytics.git
cd retail-sales-performance-analytics
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 3. Run the Python Analysis

From the project root, run:

```bash
python src/main.py
```

The script loads the raw dataset, cleans and validates the data, saves the cleaned CSV, and performs the analysis.

### 4. Explore the Notebooks

Open the notebooks in the `notebooks/` folder to review data understanding, cleaning, and exploratory analysis.

### 5. Open the Power BI Dashboard

Open `powerbi/Sales_Analytics_Dashboard.pbix` in Power BI Desktop to explore the interactive dashboard.

## Future Improvements

* Investigate and document the financial discrepancies in the source data.
* Add automated tests for data cleaning and validation.
* Improve the analysis of cancelled and returned orders.
* Add more advanced business metrics and dashboard insights.
* Develop a repeatable data refresh and reporting workflow.

## Conclusion

This project demonstrates an end-to-end analytics workflow, from raw data inspection and cleaning to exploratory analysis, business KPI reporting, and interactive Power BI visualization. It emphasizes data quality, evidence-based findings, and clear business communication.

**Author:** Kishore
**Project:** Retail Sales Performance & Profitability Analytics
**Focus Areas:** Python, Data Analysis, EDA, Business Analytics, and Power BI
