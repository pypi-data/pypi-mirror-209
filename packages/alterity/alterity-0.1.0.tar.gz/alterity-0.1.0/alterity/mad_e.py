#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Enter Project Name in Workspace Settings                                            #
# Version    : 0.1.19                                                                              #
# Python     : 3.10.10                                                                             #
# Filename   : /alterity/mad_e.py                                                                  #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : Enter URL in Workspace Settings                                                     #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday May 19th 2023 10:33:56 am                                                    #
# Modified   : Friday May 19th 2023 03:12:47 pm                                                    #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
import numpy as np

from alterity.base import Alterity


# ------------------------------------------------------------------------------------------------ #
class MADeOutlier(Alterity):
    r"""MADe methos is another variant of the modified Z-Score method

    MAD, or median absolute deviation from the median is an estimator of the spread in data with
    an approximate 50% breakdown pint like the median. MADe is obtained by scaling MAD by a factor
    of 1.483, similar to the standard deviation in a normal distribution.

    The two most common applications are:

        2 MADe: Median $\pm 2 MADe, and
        3 MADe: Median $\pm 3 MADe.


    Args:
        threshold (float): The scaling factor which produces the threshold beyond which
          an observation is considered a probable outlier. Default is 3.

    """
    __scaling_factor = 1.483

    def __init__(self, threshold: int = 3) -> None:
        super().__init__()
        self._threshold = threshold
        self._median = None
        self._mad = None
        self._mad_e = None

    @property
    def threshold(self) -> int:
        return self._threshold

    @property
    def median(self) -> np.float32:
        return self._median

    @property
    def mad_e(self) -> np.float32:
        return self._mad_e

    def fit(self, X: np.float32, y: np.float32 = None) -> Alterity:
        """Fits the outlier detector

        Args:
            X (array-like): Array of shape (n_samples, n_features). Input uses np.float32
                for maximum efficiency.

            y (None): Ignored. In place for scikit-learn API conformity.

        Returns: self (Alterity): The fitted estimator.

        """
        self._median = np.median(X, axis=0)
        self._mad = np.median(np.abs((X - np.median(X))))
        self._mad_e = self.__scaling_factor * self._mad
        return self

    def predict(self, X: np.float32) -> np.float32:
        """Predict whether each sample is an outlier.

        Args:
            X (np.float32): Array of shape (n_samples, n_features). Input samples
                will be converted to np.float32 dtype.

        Returns (np.float32): Binary ndarray of shape (n_samples,) indicating
            whether each sample is an outlier (+1) or not (0).

        """
        above = X > self._median - self._threshold * self._mad_e
        below = X < self._median + self._threshold * self._mad_e

        return np.where(above & below, 0, 1)
