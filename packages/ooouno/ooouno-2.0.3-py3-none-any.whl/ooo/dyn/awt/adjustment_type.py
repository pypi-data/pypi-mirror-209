# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.awt.AdjustmentType import ADJUST_ABS as ADJUSTMENT_TYPE_ADJUST_ABS
    from com.sun.star.awt.AdjustmentType import ADJUST_LINE as ADJUSTMENT_TYPE_ADJUST_LINE
    from com.sun.star.awt.AdjustmentType import ADJUST_PAGE as ADJUSTMENT_TYPE_ADJUST_PAGE

    class AdjustmentType(uno.Enum):
        """
        Enum Class


        See Also:
            `API AdjustmentType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#ae54d0c7f4237b639c3f45caa306457fd>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.awt.AdjustmentType', value)

        __ooo_ns__: str = 'com.sun.star.awt'
        __ooo_full_ns__: str = 'com.sun.star.awt.AdjustmentType'
        __ooo_type_name__: str = 'enum'

        ADJUST_ABS = cast("AdjustmentType", ADJUSTMENT_TYPE_ADJUST_ABS)
        """
        adjustment is originated by dragging the thumb.
        """
        ADJUST_LINE = cast("AdjustmentType", ADJUSTMENT_TYPE_ADJUST_LINE)
        """
        adjustment is originated by a line jump.
        """
        ADJUST_PAGE = cast("AdjustmentType", ADJUSTMENT_TYPE_ADJUST_PAGE)
        """
        adjustment is originated by a page jump.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class AdjustmentType(metaclass=UnoEnumMeta, type_name="com.sun.star.awt.AdjustmentType", name_space="com.sun.star.awt"):
        """Dynamically created class that represents ``com.sun.star.awt.AdjustmentType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['AdjustmentType']
