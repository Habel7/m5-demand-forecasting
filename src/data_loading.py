"""Load and downcast the M5 dataset.

The raw sales file is ~450MB as float64 — downcasting keeps it laptop-friendly.
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def reduce_memory(df: pd.DataFrame) -> pd.DataFrame:
    """Downcast numeric columns to the smallest safe dtype."""
    for col in df.select_dtypes(include=["int64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="integer")
    for col in df.select_dtypes(include=["float64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="float")
    return df


def load_calendar() -> pd.DataFrame:
    cal = pd.read_csv(DATA_DIR / "calendar.csv", parse_dates=["date"])
    return reduce_memory(cal)


def load_sales(evaluation: bool = False) -> pd.DataFrame:
    name = "sales_train_evaluation.csv" if evaluation else "sales_train_validation.csv"
    sales = pd.read_csv(DATA_DIR / name)
    return reduce_memory(sales)


def load_prices() -> pd.DataFrame:
    prices = pd.read_csv(DATA_DIR / "sell_prices.csv")
    return reduce_memory(prices)


def melt_sales(sales: pd.DataFrame, calendar: pd.DataFrame) -> pd.DataFrame:
    """Reshape wide day-columns (d_1 ... d_1913) into long format with real dates."""
    id_cols = ["id", "item_id", "dept_id", "cat_id", "store_id", "state_id"]
    long = sales.melt(id_vars=id_cols, var_name="d", value_name="units")
    long = long.merge(calendar[["d", "date", "wm_yr_wk"]], on="d", how="left")
    return reduce_memory(long)


if __name__ == "__main__":
    cal = load_calendar()
    print(f"Calendar: {cal.shape}, {cal['date'].min().date()} to {cal['date'].max().date()}")
