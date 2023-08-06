"""Test the Nearest Point on Curve Transformer module."""

import numpy as np

from caft.equation import SympyODRegressor
from caft.npoc import AnalyticalNPOCTransformer


def test_AnalyticalNPOCTransformer_no_transform():
    """Test the AnalyticalNPOCTransformer class."""
    X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
    y = 3 * X ** 3

    sodr = SympyODRegressor(equation="a*x**3", beta0={"a": 5})
    anpoc = AnalyticalNPOCTransformer(estimator=sodr, optimiser="halley")
    anpoc.fit(X, y)
    X_same, y_same = anpoc.transform(X, y)

    # all point on the line so no transformation
    assert np.allclose(X.reshape(-1), X_same)
    assert np.allclose(y.reshape(-1), y_same)


def test_AnalyticalNPOCTransformer_transform_dist_change():
    """Test the AnalyticalNPOCTransformer class."""
    n = 9
    X = np.linspace(0.8, 1.0, n).reshape(-1, 1)
    X_err = np.random.normal(0, 0.01, size=(n, 1))
    y_err = np.random.normal(0, 0.1, size=(n, 1))
    y = 3 * (X + X_err) ** 3 + y_err
    # roughly scale to [0, 1]
    y = y / 3

    sodr = SympyODRegressor(equation="a*x**3", beta0={"a": 5})
    anpoc = AnalyticalNPOCTransformer(estimator=sodr, optimiser="halley")
    anpoc.fit(X, y)
    X_t, y_t = anpoc.transform(X, y)

    y_pred = anpoc.estimator_.predict(X)

    Xy = np.hstack((X, y))
    Xy_t = np.vstack((X_t, y_t)).T
    Xy_pred = np.hstack((X, y_pred.reshape(-1, 1)))

    assert all(
        np.sqrt(((Xy - Xy_t) ** 2).sum(axis=1))
        < np.sqrt(((Xy - Xy_pred) ** 2).sum(axis=1))
    )
