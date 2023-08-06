"""Test the affine transform module"""

import numpy as np

from caft.affine import ContinuousAffineFeatureTransformer
from caft.equation import SympyODRegressor


def test_ContinuousAffineFeatureTransformer():
    n = 9
    X = np.linspace(0.8, 1.0, n).reshape(-1, 1)
    X_err = np.random.normal(0, 0.01, size=(n, 1))
    y_err = np.random.normal(0, 0.1, size=(n, 1))
    y = 3 * (X + X_err) ** 3 + y_err
    # roughly scale to [0, 1]
    y = y / 3

    sodr = SympyODRegressor(equation="a*x**3", beta0={"a": 5})

    at = ContinuousAffineFeatureTransformer(sodr, optimiser="halley")
    at.fit(X, y)
    X_t, y_t = at.transform(X, y)
    y_p = at.transformer_.estimator_.predict(X)

    assert not np.array_equal(X, X_t)
    assert not np.array_equal(y, y_t)
    assert not np.array_equal(y, y_p)

    assert hasattr(at, "transformer_")
    assert hasattr(at, "optimiser")
    assert hasattr(at, "regressor")
