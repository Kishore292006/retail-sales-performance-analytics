from src.data_cleaning import (
    load_raw_data,
    clean_data,
    validate_data,
    save_cleaned_data
)

from src.analysis import (
    calculate_overall_kpis,
    analyze_sales_by_category,
    analyze_sales_by_region,
    analyze_sales_by_channel,
    analyze_monthly_sales,
    analyze_order_status,
    analyze_profit_margin_by_category
)

def main():
    df = load_raw_data()
    df = clean_data(df)

    validate_data(df)
    save_cleaned_data(df)

    calculate_overall_kpis(df)
    analyze_sales_by_category(df)
    analyze_sales_by_region(df)
    analyze_sales_by_channel(df)
    analyze_monthly_sales(df)
    analyze_order_status(df)
    analyze_profit_margin_by_category(df)



if __name__ == "__main__":
    main()