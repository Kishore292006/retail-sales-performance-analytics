import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "Project_1_Raw_Retail_Sales.csv"
CLEANED_FILE = PROJECT_ROOT / "data" / "processed" / "sales_cleaned.csv"

def load_raw_data():
    df = pd.read_csv(RAW_FILE)
    return df

def clean_data(df):
    df.columns=[x.lower() for x in df.columns]

    df=df.drop_duplicates()

    df['region']=df['region'].replace({
        'north':'North',
        'WEST': 'West',
        'south':'South'
    })

    df['payment_method'] = df['payment_method'].replace({
        'UPI': 'Upi',
        'credit card': 'Credit Card',
        'upi': 'Upi'
    })

    df['sales_channel'] = df['sales_channel'].replace({
        'online': 'Online',
        'store': 'Store'
    })

    df['order_date'] = pd.to_datetime(df['order_date'], format='mixed')

    df['customer_name'] = df['customer_name'].fillna('Unknown')
    df['city'] = df['city'].fillna('Unknown')
    df['payment_method'] = df['payment_method'].fillna('Unknown')
    df['discount'] = df['discount'].fillna(0)

    df = df[
        (df['quantity'] > 0)
        & (df['unit_price'] > 0)
        & (df['discount'] >= 0)
        & (df['discount'] <= 1)
        ]

    return df

def save_cleaned_data(df):
    CLEANED_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEANED_FILE, index=False)
    print(f"Cleaned data saved to {CLEANED_FILE}")

def validate_data(df):
    print("\n--- Data Validation Report ---")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print(f"Missing values: {df.isnull().sum().sum()}")
    print(f"Invalid quantities: {(df['quantity'] <= 0).sum()}")
    print(f"Invalid unit prices: {(df['unit_price'] <= 0).sum()}")
    print(f"Invalid discounts: {((df['discount'] < 0) | (df['discount'] > 1)).sum()}")
    print(f"Invalid dates: {df['order_date'].isnull().sum()}")

    assert df.duplicated().sum() == 0, "Duplicate rows found"
    assert df.isnull().sum().sum() == 0, "Missing values found"
    assert (df['quantity'] > 0).all(), "Invalid quantities found"
    assert (df['unit_price'] > 0).all(), "Invalid unit prices found"
    assert df['discount'].between(0, 1).all(), "Invalid discounts found"
    assert df['order_date'].notna().all(), "Invalid dates found"

    calculated_sales = (
        df['quantity'] * df['unit_price'] * (1 - df['discount'])
    ).round(2)
    sales_mismatches = (
        (calculated_sales - df['sales']).abs() > 1
    ).sum()
    print(f"Sales mismatches (difference > 1): {sales_mismatches}")
    print("\n--- Financial Validation ---")
    print("Sales mismatches are reported separately from basic data-quality checks.")

    if sales_mismatches == 0:
        print("All validation checks passed!")
    else:
        print("WARNING: Sales mismatches require investigation.")

if __name__ == "__main__":
    df = load_raw_data()
    df = clean_data(df)

    validate_data(df)
    save_cleaned_data(df)