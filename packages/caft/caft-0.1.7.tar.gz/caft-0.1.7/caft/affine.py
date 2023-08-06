"""Affine transformation functions."""

import numpy as np
import sympy as sp
from sklearn.base import BaseEstimator, TransformerMixin, clone
from sklearn.utils.validation import column_or_1d

from caft.npoc import AnalyticalNPOCTransformer


def rotate(X, y, normal):

    Xy = np.hstack([X, y])
    theta = np.arctan(normal)
    rotate = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    rotate = np.transpose(rotate, (2, 0, 1,))
    Xy_ = Xy[:, None, :]
    rotated = np.matmul(Xy_, rotate)[:, 0, :]
    return rotated[:, 0], rotated[:, 1]


class ContinuousAffineFeatureTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, regressor, optimiser="brentq"):
        self.regressor = regressor
        self.optimiser = optimiser

    def fit(self, X, y):
        self.transformer_ = clone(
            AnalyticalNPOCTransformer(self.regressor, optimiser=self.optimiser)
        )
        self.transformer_.fit(X, y)
        return self

    def transform(self, X, y):
        X_ = column_or_1d(X).reshape(-1, 1)
        y_ = column_or_1d(y).reshape(-1, 1)
        X_trans, y_trans = self.transformer_.transform(X_, y_)
        fitted_regressor = self.transformer_.estimator_

        dfdx = self.transformer_.derivative()
        dfdx_lambda = sp.lambdify([fitted_regressor.wrt], dfdx,)

        X_centred = X_ - X_trans.reshape(-1, 1)
        y_centred = y_ - y_trans.reshape(-1, 1)
        grad = dfdx_lambda(X_trans).reshape(-1)

        X_rot, y_rot = rotate(X_centred, y_centred, grad)
        X_ = X_rot + X_trans
        return X_, y_rot

    def get_feature_names_out(self):
        pass
