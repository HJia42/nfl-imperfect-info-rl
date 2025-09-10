from pathlib import Path
import pandas as pd


def load_play_by_play(csv_path: str | Path) -> pd.DataFrame:
    """Load a CSV into a DataFrame. Minimal validation only."""
    return pd.read_csv(csv_path)

