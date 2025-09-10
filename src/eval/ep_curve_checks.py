import pandas as pd


def is_monotonic_ep_curve(df: pd.DataFrame, value_col: str) -> bool:
    vals = df[value_col].values
    return all(vals[i] <= vals[i + 1] for i in range(len(vals) - 1))
