#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Enter Project Name in Workspace Settings                                            #
# Version    : 0.1.19                                                                              #
# Python     : 3.10.10                                                                             #
# Filename   : /alterity/tukey.py                                                                  #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : Enter URL in Workspace Settings                                                     #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday May 19th 2023 10:33:56 am                                                    #
# Modified   : Friday May 19th 2023 01:00:19 pm                                                    #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
import numpy as np

from alterity.base import Alterity


# ------------------------------------------------------------------------------------------------ #
class TukeyOutlier(Alterity):
    r"""Tukey's Outlier (Boxplot) Detection Algorithm

    Tukey's (1977) method for detecting outliers in continuous univariate data employs information
    such as the median, and the lower and upper quantiles is less sensitive than other methods
    such as the ZScore to extreme values. The inter quartile range (IQR) of a continuous
    univariate distribution is the distance between the lower (Q1) and upper (Q3) quartiles.

    For this method, the upper and lower bounds are expressed in terms of the IQR as follows:
    - lower bound: Q1-3*IQR
    - upper bound: Q3+3*IQR
    where Q1 and Q3 are the 1st and 3rd quartiles respectively.

    Points beyond these bounds are considered 'probable' outliers.

    Args:
        threshold (float): A multiple of the IQR. Default = 3.

    """
    __EMAD = 0.6745  # Expectation of the median absolute devaition

    def __init__(self, threshold: int = 3) -> None:
        super().__init__()
        self._threshold = threshold
        self._q1 = None
        self._q3 = None
        self._iqr = None

    @property
    def threshold(self) -> int:
        return self._threshold

    @property
    def q1(self) -> np.float32:
        return self._q1

    @property
    def q3(self) -> np.float32:
        return self._q3

    @property
    def iqr(self) -> np.float32:
        return self._iqr

    def fit(self, X: np.float32, y: np.float32 = None) -> Alterity:
        """Fits the outlier detector

        Args:
            X (array-like): Array of shape (n_samples, n_features). Input uses np.float32
                for maximum efficiency.

            y (None): Ignored. In place for scikit-learn API conformity.

        Returns: self (Alterity): The fitted estimator.

        """
        self._q1 = np.quantile(a=X, q=0.25, axis=0)
        self._q3 = np.quantile(a=X, q=0.75, axis=0)
        self._iqr = self._q3 - self._q1
        return self

    def predict(self, X: np.float32) -> np.float32:
        """Predict whether each sample is an outlier.

        Args:
            X (np.float32): Array of shape (n_samples, n_features). Input samples
                will be converted to np.float32 dtype.

        Returns (np.float32): Binary ndarray of shape (n_samples,) indicating
            whether each sample is an outlier (+1) or not (0).

        """
        above = X > (self._q1 - self._threshold * self._iqr)
        below = X < (self._q3 + self._threshold * self._iqr)

        return np.where(above & below, 0, 1)
