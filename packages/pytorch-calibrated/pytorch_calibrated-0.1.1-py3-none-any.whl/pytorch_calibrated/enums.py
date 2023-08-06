# Copyright 2023 SOTAI Labs Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Enums used throughout the PyTorch Calibrated library."""
from enum import Enum, EnumMeta
from typing import Any


class _Metaclass(EnumMeta):
    """Base `EnumMeta` subclass for accessing enum members directly."""

    def __getattribute__(cls, __name: str) -> Any:
        value = super().__getattribute__(__name)
        if isinstance(value, Enum):
            value = value.value
        return value


class Monotonicity(str, Enum, metaclass=_Metaclass):
    """Type of monotonicity constraint.

    - NONE: no monotonicity constraint.
    - INCREASING: increasing monotonicity i.e. increasing input increases output.
    - DECREASING: decreasing monotonicity i.e. increasing input decreases output.
    """

    NONE = "none"
    INCREASING = "increasing"
    DECREASING = "decreasing"


class NumericalCalibratorInit(str, Enum, metaclass=_Metaclass):
    """Type of kernel initialization to use for NumericalCalibrator.

    - EQUAL_HEIGHTS: initialize the kernel such that all segments have the same height.
    - EQUAL_SLOPES: initialize the kernel such that all segments have the same slope.
    """

    EQUAL_HEIGHTS = "equal_heights"
    EQUAL_SLOPES = "equal_slopes"


class CategoricalCalibratorInit(str, Enum, metaclass=_Metaclass):
    """Type of kernel initialization to use for CategoricalCalibrator.

    - UNIFORM: initialize the kernel with uniformly distributed values. The sample range
        will be [`output_min`, `output_max`] if both are provided.
    - CONSTANT: initialize the kernel with a constant value for all categories. This
        value will be `(output_min + output_max) / 2` if both are provided.
    """

    UNIFORM = "uniform"
    CONSTANT = "constant"


class InputKeypointsInit(str, Enum, metaclass=_Metaclass):
    """Type of initialization to use for NumericalCalibrator input keypoints.

    - QUANTILES: initialize the input keypoints such that each segment will see the same
        number of examples.
    - UNIFORM: initialize the input keypoints uniformly spaced in the feature range.
    """

    QUANTILES = "quantiles"
    UNIFORM = "uniform"


class FeatureType(str, Enum, metaclass=_Metaclass):
    """Type of feature.

    - NUMERICAL: a numerical feature that should be calibrated using an instance of
        `NumericalCalibrator`.
    - CATEGORICAL: a categorical feature that should be calibrated using an instance of
        `CategoricalCalibrator`.
    """

    NUMERICAL = "numerical"
    CATEGORICAL = "categorical"
