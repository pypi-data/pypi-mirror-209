#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Enter Project Name in Workspace Settings                                            #
# Version    : 0.1.19                                                                              #
# Python     : 3.10.10                                                                             #
# Filename   : /alterity/zscore2.py                                                                #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : Enter URL in Workspace Settings                                                     #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday May 19th 2023 10:33:56 am                                                    #
# Modified   : Friday May 19th 2023 12:49:22 pm                                                    #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
import numpy as np

from alterity.base import Alterity


# ------------------------------------------------------------------------------------------------ #
class ZScoreOutlier2(Alterity):
    r"""Modified Z-Score Outlier Detection Algorithm

    The median and the median of the absolute deviation of the median (MAD) are employed in
    the outlier detection method called the modified Z-Score. The median absolute deviation of
    the median is computed as follows:

    $$MAD=median{|x_i-\mathbb{M}{x}|}$$

    where $x_i$ is the sample median. The modified Z-Score $(M_i)$ can now be computed as:

     $$M_i=\frac{0.6745(x_i-\mathbb{M}{X})}{MAD}$$

    Args:
        threshold (int): The threshold above which the absolute value of an observation
            is considered an outlier. The default is 3.5

    """
    __EMAD = 0.6745  # Expectation of the median absolute devaition

    def __init__(self, threshold: int = 3.5) -> None:
        super().__init__()
        self._threshold = threshold
        self._median = None
        self._mad = None
        self._mod_zscore = None

    @property
    def threshold(self) -> int:
        return self._threshold

    @property
    def median(self) -> np.float32:
        return self._median

    @property
    def mad(self) -> np.float32:
        return self._mad

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
        return self

    def predict(self, X: np.float32) -> np.float32:
        """Predict whether each sample is an outlier.

        Args:
            X (np.float32): Array of shape (n_samples, n_features). Input samples
                will be converted to np.float32 dtype.

        Returns (np.float32): Binary ndarray of shape (n_samples,) indicating
            whether each sample is an outlier (+1) or not (0).

        """
        self._mod_zscore = (self.__EMAD * (X - np.median(X))) / self._mad
        return np.where((np.abs(self._mod_zscore) > self._threshold), 1, 0)
