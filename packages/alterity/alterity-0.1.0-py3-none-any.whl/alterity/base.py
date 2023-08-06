#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Enter Project Name in Workspace Settings                                            #
# Version    : 0.1.19                                                                              #
# Python     : 3.10.10                                                                             #
# Filename   : /alterity/base.py                                                                   #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : Enter URL in Workspace Settings                                                     #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday May 19th 2023 07:04:25 am                                                    #
# Modified   : Friday May 19th 2023 12:48:22 pm                                                    #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from __future__ import annotations
from abc import ABC, abstractmethod
import logging

import numpy as np


# ------------------------------------------------------------------------------------------------ #
class Alterity(ABC):
    """Outlier detection base class"""

    def __init__(self) -> None:
        self._logger = logging.getLogger(f"{self.__class__.__name__}")

    @abstractmethod
    def fit(self, X: np.float32, y: np.float32 = None) -> Alterity:
        """Fits the outlier detector

        Args:
            X (array-like): Array of shape (n_samples, n_features). Input uses np.float32
                for maximum efficiency.

            y (None): Ignored. In place for scikit-learn API conformity.

        Returns: self (Alterity): The fitted estimator.

        """

    @abstractmethod
    def predict(X: np.float32) -> np.float32:
        """Predict whether each sample is an outlier.

        Args:
            X (np.float32): Array of shape (n_samples, n_features). Input samples
                will be converted to np.float32 dtype.

        Returns (np.float32): Binary ndarray of shape (n_samples,) indicating
            whether each sample is an outlier (+1) or not (0).

        """
