"""Nearest Point on Curve Transformer."""

import sympy as sp
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin, clone
from scipy.optimize import root_scalar


class AnalyticalNPOCTransformer(BaseEstimator, TransformerMixin):
    """Fit a regressor and transform data to the nearest point on it's curve.

    Can be used with any "equation regressor" that implements `fit` and
    `predict` methods, `wrt` and `sp_equation` attributes to find the nearest
    points on a curve in Euclidean space. It is recommended that you scale the
    X and y variables prior to fitting, if they are of varying magnitudes.

    Parameters
    ----------
    estimator : regression object implementing `fit` and `predict`
        A regressor object implementing `fit` and `predict`.
    optimiser : str, optional
        The optimiser to use to find the nearest point on the curve. Can be
        either "brentq" or "halley". Defaults to "brentq". Use halley for
        polynomial or functions that when differentiated, their complexity
        doesn't blow up. Use brentq for more complex functions with fewer
        roots.

    Attributes
    ----------
    estimator_ : regressor
        The regressor actually fitted on the data.
    function_type : str
        The type of function used to fit the data. Dictates the method used
        to find the nearest point on the curve and the derivative.
    """
    def __init__(self, estimator, optimiser="brentq"):
        self.estimator = estimator
        self.optimiser = optimiser

    def fit(self, X, y):
        self.estimator_ = clone(self.estimator)
        self.estimator_.fit(X, y)

        self.p = sp.Symbol("p")
        self.q = sp.Symbol("q")

        self.circle_equation = (
            (self.estimator_.wrt_symbol - self.p) ** 2
            + (self.estimator_.sp_equation - self.q) ** 2
        )

        self.dgdx = self.circle_equation_derivative()
        self.d2gx2 = self.dgdx.diff(self.estimator_.wrt_symbol)
        self.d3gx3 = self.d2gx2.diff(self.estimator_.wrt_symbol)
        self.dgdx_lambda = sp.lambdify(
            [self.estimator_.wrt, self.p, self.q],
            self.dgdx,
        )
        self.d2gdx2_lambda = sp.lambdify(
            [self.estimator_.wrt, self.p, self.q],
            self.d2gx2,
        )
        self.d3gdx3_lambda = sp.lambdify(
            [self.estimator_.wrt, self.p, self.q],
            self.d3gx3,
        )
        return self

    def transform(self, X, y):
        return self.nearest_point_on_curve(X, y)

    def derivative(self):
        return self.estimator_.sp_equation.diff(self.estimator_.wrt)

    def nearest_point_on_curve(self, X, y):
        return self.analytical_nearest_point_on_curve(X, y)

    def analytical_nearest_point_on_curve(self, X, y):
        if self.optimiser == "brentq":
            def root(p, q):
                return root_scalar(
                    self.dgdx_lambda,
                    bracket=(0, 1),
                    method=self.optimiser,
                    x0=(p + q) / 2,
                    args=(p, q),
                ).root
        elif self.optimiser == "halley":
            def root(p, q):
                return root_scalar(
                    self.dgdx_lambda,
                    fprime=self.d2gdx2_lambda,
                    fprime2=self.d3gdx3_lambda,
                    method=self.optimiser,
                    x0=(p + q) / 2,
                    args=(p, q),
                ).root

        Xy = pd.DataFrame({"X": X.reshape(-1), "y": y.reshape(-1)})
        X_nearest = Xy.apply(lambda row: root(row[0], row[1]), axis=1)
        y_nearest = self.estimator_.predict(X_nearest)
        return X_nearest.values, y_nearest

    def circle_equation_derivative(self):
        return self.circle_equation.diff(self.estimator_.wrt_symbol)

    def get_feature_names_out(self):
        pass
