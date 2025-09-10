from pathlib import Path
from typing import Dict

import yaml


def load_defense_effects(config_path: str | Path) -> Dict[str, float]:
    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("defense_effects", {})
