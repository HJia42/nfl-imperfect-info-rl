from typing import List


def bin_yardline(yardline: int, edges: List[int] | None = None, labels: List[str] | None = None) -> str:
    """Simple yardline binning. Yardline measured from own GL [1..99].

    Default bins:
      [0, 20, 50, 80, 100] -> ["Own", "Mid", "Opp", "RedZone"]
    """
    if edges is None:
        edges = [0, 20, 50, 80, 100]
    if labels is None:
        labels = ["Own", "Mid", "Opp", "RedZone"]
    assert len(edges) == len(labels) + 1
    for i in range(len(labels)):
        if edges[i] < yardline <= edges[i + 1]:
            return labels[i]
    return labels[-1]

