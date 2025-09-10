from src.data.binning import bin_yardline


def test_bin_yardline_defaults():
    assert bin_yardline(10) == "Own"
    assert bin_yardline(40) == "Mid"
    assert bin_yardline(70) == "Opp"
    assert bin_yardline(90) == "RedZone"
