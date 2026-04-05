import numpy as np
from sklearn.linear_model import LogisticRegression


def train_model():
    """Train a simple risk prediction model."""
    X = np.array([
        [80, 90],
        [70, 85],
        [40, 50],
        [30, 40],
        [90, 95],
        [20, 30],
    ])

    y = np.array([0, 0, 1, 1, 0, 1])

    model = LogisticRegression()
    model.fit(X, y)

    return model