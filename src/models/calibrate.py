from typing import Any


def calibrate_epa_model(data) -> Any:
    # Placeholder: return a no-op model
    class _Model:
        def predict(self, X):  # noqa: N802
            return [0.0] * len(X)

    return _Model()

