import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CLEANED_FILE = PROJECT_ROOT / "data" / "processed" / "sales_cleaned.csv"

def load_cleaned_data():
    df = pd.read_csv(CLEANED_FILE, parse_dates=["order_date"])
    return df

def calculate_overall_kpis(df):
    total_sales = df["sales"].sum()
    total_profit = df["profit"].sum()
    total_orders = df["order_id"].nunique()
    profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

    print("----- Overall Business KPIs -----")
    print(f"Total Sales: ₹{total_sales:,.2f}")
    print(f"Total Profit: ₹{total_profit:,.2f}")
    print(f"Total Orders: {total_orders:,}")
    print(f"Profit Margin: {profit_margin:.2f}%")


def analyze_sales_by_category(df):
    category_summary = df.groupby("category").agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    category_summary = category_summary.sort_values(
        by="total_sales",
        ascending=False
    )
    print("\n----- Sales by Category -----")
    print(category_summary.round(2))


def analyze_sales_by_region(df):
    region_summary = df.groupby("region").agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    region_summary = region_summary.sort_values(
        by="total_sales",
        ascending=False
    )
    print("\n----- Sales by Region -----")
    print(region_summary.round(2))


def analyze_sales_by_channel(df):
    channel_summary = df.groupby("sales_channel").agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        total_orders=("order_id", "nunique")
    )
    channel_summary = channel_summary.sort_values(
        by="total_sales",
        ascending=False
    )
    print("\n----- Sales by Channel -----")
    print(channel_summary.round(2))


def analyze_monthly_sales(df):
    df = df.copy()
    df["month"] = df["order_date"].dt.to_period("M")
    monthly_summary = df.groupby("month").agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    print("\n----- Monthly Sales Trend -----")
    print(monthly_summary.round(2))


    highest_month = monthly_summary["total_sales"].idxmax()
    lowest_month = monthly_summary["total_sales"].idxmin()

    print(f"\nHighest Sales Month: {highest_month}")
    print(f"Highest Monthly Sales: ₹{monthly_summary.loc[highest_month, 'total_sales']:,.2f}")

    print(f"\nLowest Sales Month: {lowest_month}")
    print(f"Lowest Monthly Sales: ₹{monthly_summary.loc[lowest_month, 'total_sales']:,.2f}")


def analyze_order_status(df):
    status_summary = df.groupby("order_status").agg(
        total_orders=("order_id", "nunique"),
        total_sales=("sales", "sum")
    )
    print("\n----- Order Status Analysis -----")
    print(status_summary.round(2))


def analyze_profit_margin_by_category(df):
    category_summary = df.groupby("category").agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    category_summary["profit_margin"] = np.where(
        category_summary["total_sales"] != 0,
        category_summary["total_profit"]
        / category_summary["total_sales"] * 100,
        np.nan
    )
    category_summary = category_summary.sort_values(
        by="profit_margin",
        ascending=False
    )
    print("\n----- Profit Margin by Category -----")
    print(category_summary.round(2))



if __name__=="__main__":
    df = load_cleaned_data()
    calculate_overall_kpis(df)
    analyze_sales_by_category(df)
    analyze_sales_by_region(df)
    analyze_sales_by_channel(df)
    analyze_monthly_sales(df)
    analyze_order_status(df)
    analyze_profit_margin_by_category(df)