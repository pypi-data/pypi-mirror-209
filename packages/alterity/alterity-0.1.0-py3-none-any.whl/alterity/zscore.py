#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Enter Project Name in Workspace Settings                                            #
# Version    : 0.1.19                                                                              #
# Python     : 3.10.10                                                                             #
# Filename   : /alterity/zscore.py                                                                 #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : Enter URL in Workspace Settings                                                     #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday May 19th 2023 10:33:56 am                                                    #
# Modified   : Friday May 19th 2023 12:49:12 pm                                                    #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
import numpy as np

from alterity.base import Alterity


# ------------------------------------------------------------------------------------------------ #
class ZScoreOutlier(Alterity):
    r"""ZScoreOutlier Outlier Detection Algorithm

    Standard outlier detection method based upon the sample mean and the sample standard deviation;
    whereas, an observation is considered an outlier if its value is outside of the
    interval formed by the sample mean +/- a threshold value * the Z-Score.

    This method is justified when X follows a normal distribution parameterized as $\mathbb{N}(\mu,\sigma^2)$.
    Then, Z follows a normal distribution, $\mathbb{N}(0,1)$ as follows:

    $$Z_i = \frac{x_i-\bar{x}}{sd}$$,

    where $X_i \near N(\mu,\sigma^2), and sd is the standard deviation of the data.


    Args:
        threshold (int): The optional threshold Z-Score above which an observation is considered an outlier.
            The default threshold value is based upon the sample size and it is computed as
            $(n-1)\sqrt(n).

    """

    def __init__(self, threshold: int = None, min_threshold: int = 3) -> None:
        super().__init__()
        self._threshold = threshold
        self._min_threshold = min_threshold
        self._mean = None
        self._std = None
        self._zscore = None

    @property
    def threshold(self) -> int:
        return self._threshold

    @property
    def mean(self) -> np.float32:
        return self._mean

    @property
    def std(self) -> np.float32:
        return self._std

    def fit(self, X: np.float32, y: np.float32 = None) -> Alterity:
        """Fits the outlier detector

        Args:
            X (array-like): Array of shape (n_samples, n_features). Input uses np.float32
                for maximum efficiency.

            y (None): Ignored. In place for scikit-learn API conformity.

        Returns: self (Alterity): The fitted estimator.

        """
        self._mean = np.mean(X, axis=0)
        self._std = np.std(X, axis=0)
        self._zscore = (X - self._mean) / self._std
        self._threshold = self._threshold or np.max(
            (self._zscore.any(), self._min_threshold), axis=0
        )
        return self

    def predict(self, X: np.float32) -> np.float32:
        """Predict whether each sample is an outlier.

        Args:
            X (np.float32): Array of shape (n_samples, n_features). Input samples
                will be converted to np.float32 dtype.

        Returns (np.float32): Binary ndarray of shape (n_samples,) indicating
            whether each sample is an outlier (+1) or not (0).

        """
        return np.where((np.abs(X) > self._threshold), 1, 0)
